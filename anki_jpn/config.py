"""classes and functions focused on managing the Addon configuration"""
from typing import Dict, Any

from anki_jpn.enums import VerbClass, AdjectiveClass

class ConfigManager:
    """Object for managing and querying the Addon configuration"""

    def __init__(self, cfg: Dict[str, Any]):
        if isinstance(cfg, dict):
            self._cfg = cfg
        else:
            self._cfg = {}

        if 'tags' not in self._cfg:
            self._cfg['tags'] = {}
        if 'note_types' not in self._cfg:
            self._cfg['note_types'] = {}

    def dump(self):
        return self._cfg

    def verb_tags_empty(self, deck_name):
        if deck_name not in self._cfg['tags']:
            return True
        
        ichidan_tags = self._cfg['tags'][deck_name].get(VerbClass.ICHIDAN.value, [])
        godan_tags = self._cfg['tags'][deck_name].get(VerbClass.GODAN.value, [])
        irregular_tags = self._cfg['tags'][deck_name].get(VerbClass.IRREGULAR.value, [])
        general_tags = self._cfg['tags'][deck_name].get(VerbClass.GENERAL.value, [])
        
        if any(tag_list for tag_list in [ichidan_tags, godan_tags, irregular_tags, general_tags]):
            return False
        else:
            return True
        
    def adjective_tags_empty(self, deck_name):
        if deck_name not in self._cfg['tags']:
            return True
        
        i_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.I.value, [])
        na_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.NA.value, [])
        general_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.GENERAL.value, [])
        
        if any(tag_list for tag_list in [i_tags, na_tags, general_tags]):
            return False
        else:
            return True
    
    def model_fields_empty(self, model_name):
        if model_name not in self._cfg['note_types']:
            return True
        
        for key in ['expression', 'meaning', 'reading']:
            if not self._cfg['note_types'][model_name].get(key, ''):
                return True

    def add_tag(self, deck_name, tag, word_type):
        if deck_name not in self._cfg['tags']:
            self._cfg['tags'][deck_name] = {}
        if word_type.value not in self._cfg['tags'][deck_name]:
            self._cfg['tags'][deck_name][word_type.value] = []
        if tag is not None and tag not in self._cfg['tags'][deck_name][word_type.value]:
            self._cfg['tags'][deck_name][word_type.value].append(tag)

    def add_model_fields(self, model_name, expression_field, meaning_field, reading_field):
        if model_name not in self._cfg['note_types']:
            self._cfg['note_types'][model_name] = {}
        
        self._cfg['note_types'][model_name]['expression'] = expression_field
        self._cfg['note_types'][model_name]['meaning'] = meaning_field
        self._cfg['note_types'][model_name]['reading'] = reading_field

    def get_tags(self, deck_name, word_type):
        if deck_name not in self._cfg['tags']:
            return []
        else:
            return self._cfg['tags'][deck_name].get(word_type.value, [])

    def get_model_fields(self, model_name):
        if model_name is None:
            raise ValueError("Model name must be provided as a string. Found None.")
        return self._cfg['note_types'].get(model_name, {})
