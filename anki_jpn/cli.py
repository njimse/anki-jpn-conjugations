"""Command Line Interface (CLI) methods"""
import os
import json
import shutil
import tempfile
import zipfile
import argparse

import anki.collection
import anki.stdmodels
import anki.notes
import anki.exporting

from anki_jpn.config import ConfigManager
from anki_jpn.decks import DeckSearcher, DeckUpdater
from anki_jpn.models import (
    add_or_update_verb_model, add_or_update_adjective_model
)

def main(args): # pylint: disable=R0914
    """Main function for generating verb and adjective conjugation decks"""

    with open(args.config, 'r') as handle: # pylint: disable=W1514
        config = ConfigManager(json.load(handle))

    temp_dir_name = tempfile.mkdtemp()
    with zipfile.ZipFile(args.input, 'r') as zip_ref:
        zip_ref.extractall(temp_dir_name)
    if not os.path.exists(os.path.join(temp_dir_name, 'collection.media')):
        os.makedirs(os.path.join(temp_dir_name, 'collection.media'))
    collection_file = os.path.join(temp_dir_name, "collection.anki21")

    col = anki.collection.Collection(collection_file) # pylint: disable=E1101
    col.media._dir = os.path.join(temp_dir_name, 'collection.media') # pylint: disable=W0212
    adj_model_name = config.adjective_model_name()
    verb_model_name = config.verb_model_name()
    add_or_update_verb_model(col.models, verb_model_name)
    add_or_update_adjective_model(col.models, adj_model_name)
    verb_model = col.models.by_name(verb_model_name)
    adj_model = col.models.by_name(adj_model_name)
    verb_deck_id = col.decks.id(args.verb_deck_name, create=True)
    adj_deck_id = col.decks.id(args.adj_deck_name, create=True)

    verb_updater = DeckUpdater(col, verb_deck_id, verb_model, config)
    adj_updater = DeckUpdater(col, adj_deck_id, adj_model, config)

    source_deck_id = col.decks.id(args.source_deck_name)
    deck_searcher = DeckSearcher(col, source_deck_id, config)

    # get the adjectives
    adj_note_ids, relevant_models = deck_searcher.find_adjectives(adj_model['name'])

    for model_name in relevant_models:
        if config.model_fields_empty(model_name):
            raise ValueError("Please specify the relevant fields for the '{model_name}' note type")

    verb_note_ids, relevant_models = deck_searcher.find_verbs(verb_model['name'])
    for model_name in relevant_models:
        if config.model_fields_empty(model_name):
            raise ValueError("Please specify the relevant fields for the '{model_name}' note type")

    for adj_type, note_id_list in adj_note_ids.items():
        for note_id in note_id_list:
            note = col.get_note(note_id)
            adj_updater.add_note_to_deck(note, adj_type)

    for verb_type, note_id_list in verb_note_ids.items():
        for note_id in note_id_list:
            note = col.get_note(note_id)
            verb_updater.add_note_to_deck(note, verb_type)

    outdir = os.path.dirname(os.path.abspath(args.output))
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    col.decks.remove([source_deck_id])
    exporter = anki.exporting.AnkiPackageExporter(col)
    exporter.exportInto(args.output)
    col.close()
    shutil.rmtree(temp_dir_name)

def main_cli():
    """Console script for generating verb and adjective decks"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    parser.add_argument('--source-deck-name', dest='source_deck_name', required=True)
    parser.add_argument('--verb-deck-name', dest='verb_deck_name',
                        default="Japanese Verb Conjugations")
    parser.add_argument('--adj-deck-name', dest='adj_deck_name',
                        default="Japanese Adjective Conjugations")

    parser.add_argument('--config')
    args = parser.parse_args()

    main(args)
