import anki.notes
from typing import List, Tuple, Optional

from anki_jpn.enums import Form, Formality
from anki_jpn.models import combo_to_field_name

class DeckUpdater:

    def __init__(self, col, deck_id, model, combo_list, field_map):
        self._col = col
        self._deck_id = deck_id
        self._deck_name = self._col.decks.get(did=self._deck_id)['name']
        self._model = model
        self._model_field_map = self._col.models.field_map(self._model)
        self._combo_list = combo_list
        self._source_field_map = field_map

    def add_note_to_deck(self, source_note, conjugations):
        expression = source_note.fields[self._source_field_map['expression']]
        meaning = source_note.fields[self._source_field_map['meaning']]
        reading = source_note.fields[self._source_field_map['reading']]

        query = f'"Expression:{expression}" "Meaning:{meaning}" "Reading:{reading}" "deck:{self._deck_name}"'
        existing_notes = self._col.find_notes(query)
        if existing_notes:
            note = self._col.get_note(existing_notes[0])
        else:
            note = anki.notes.Note(self._col, self._model)
            note.fields[self._model_field_map['Expression'][0]] = expression
            note.fields[self._model_field_map['Meaning'][0]] = meaning
            note.fields[self._model_field_map['Reading'][0]] = reading

        for t in source_note.tags:
            note.add_tag(t)

        self._expand_note(note, conjugations)
        
        if existing_notes:
            self._col.update_note(note)
        else:
            self._col.add_note(note, self._deck_id)

    def _expand_note(self, note: anki.notes.Note,
                    forms: List[Tuple[str, Optional[Formality], Form]]) -> None:
        """Expand a note with the provided conjugations

        Parameters
        ----------
        note : anki.notes.Note
            Note to be expanded with conjugations
        forms : List[Tuple[str, Optional[Formality], Form]]
            List of conjugations and their corresponding formality and form information.
        """

        for conjugation, form, formality in forms:
            field_name = combo_to_field_name(form, formality)
            if field_name in self._model_field_map:
                field_index = self._model_field_map[field_name][0]
                note.fields[field_index] = conjugation
