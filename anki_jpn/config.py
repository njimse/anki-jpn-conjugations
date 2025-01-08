"""classes and functions focused on managing the Addon configuration"""
from typing import Dict, Any, Union, List, Tuple

from anki_jpn.enums import VerbClass, AdjectiveClass

class ConfigManager:
    """Object for managing and querying the Addon configuration

    Parameters
    ----------
    cfg : Dict[str, Any]
        Settings obtained for the Addon
    """

    def __init__(self, cfg: Dict[str, Any]):
        if isinstance(cfg, dict):
            self._cfg = cfg
        else:
            self._cfg = {}

        if 'tags' not in self._cfg:
            self._cfg['tags'] = {}
        if 'note_types' not in self._cfg:
            self._cfg['note_types'] = {}

    def dump(self) -> Dict[str, Any]:
        """
        Returns
        -------
        Dict[str, Any]
            Latest settings for the Addon
        """

        return self._cfg

    def verb_model_name(self) -> str:
        """Retrieve the name of the verb conjugation model

        Returns
        -------
        str
            Name to use for the verb conjugation note type
        """

        return self._cfg.get('verb_conjugation_note_type', "Japanese Verb Conjugation")

    def adjective_model_name(self) -> str:
        """Retrieve the name of the adjective conjugation model

        Returns
        -------
        str
            Name to use for the adjective conjugation note type
        """

        return self._cfg.get('adjective_conjugation_note_type', "Japanese Adjective Conjugation")

    def verb_tags_empty(self, deck_name: str) -> bool:
        """Determine if the tag specification is populated for finding verbs

        Parameters
        ----------
        deck_name : str
            Name of the source deck for which the tags should be specified

        Returns
        -------
        bool
            True if the tag specification is incomplete/empty
        """

        if deck_name not in self._cfg['tags']:
            return True

        ichidan_tags = self._cfg['tags'][deck_name].get(VerbClass.ICHIDAN.value, [])
        godan_tags = self._cfg['tags'][deck_name].get(VerbClass.GODAN.value, [])
        irregular_tags = self._cfg['tags'][deck_name].get(VerbClass.IRREGULAR.value, [])
        general_tags = self._cfg['tags'][deck_name].get(VerbClass.GENERAL.value, [])

        if not any(tag_list for tag_list in [ichidan_tags, godan_tags,
                                             irregular_tags, general_tags]):
            return True

        return False

    def adjective_tags_empty(self, deck_name: str) -> bool:
        """Determine if the tag specification is populated for finding adjectives

        Parameters
        ----------
        deck_name : str
            Name of the source deck for which the tags should be specified

        Returns
        -------
        bool
            True if the tag specification is incomplete/empty
        """

        if deck_name not in self._cfg['tags']:
            return True

        i_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.I.value, [])
        na_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.NA.value, [])
        general_tags = self._cfg['tags'][deck_name].get(AdjectiveClass.GENERAL.value, [])

        if not any(tag_list for tag_list in [i_tags, na_tags, general_tags]):
            return True

        return False

    def model_fields_empty(self, model_name: str) -> bool:
        """Determine if the field specification is populated for the specified model

        Parameters
        ----------
        model_name : str
            Name of the model for which the fields should be specified

        Returns
        -------
        bool
            True if the field specification is incomplete/empty for the specified model
        """

        if model_name not in self._cfg['note_types']:
            return True

        for key in ['expression', 'meaning', 'reading']:
            if not self._cfg['note_types'][model_name].get(key, ''):
                return True

        return False

    def add_tag(self, deck_name: str, tag: str, word_type: Union[VerbClass, AdjectiveClass]) \
        -> None:
        """Register a tag for a source deck

        Parameters
        ----------
        deck_name : str
            Name of the source deck with which the tag will be associated
        tag: str
            Tag string to be registered
        word_type : Union[VerbClass, AdjectiveClass]
            Type of word that the tag indicates
        """

        if deck_name not in self._cfg['tags']:
            self._cfg['tags'][deck_name] = {}
        if word_type.value not in self._cfg['tags'][deck_name]:
            self._cfg['tags'][deck_name][word_type.value] = []
        if tag is not None and tag not in self._cfg['tags'][deck_name][word_type.value]:
            self._cfg['tags'][deck_name][word_type.value].append(tag)

    def add_model_fields(self, model_name: str,
                         expression: str, meaning: str, reading: str) -> None:
        """Register which fields are relevant for the specified model

        Parameters
        ----------
        model_name : str
            Name of the model (a.k.a. Note Type) for which fields are being registered
        expression : str
            Field name that indicates the expression for a note
        meaning : str
            Field name that indicates the meaning/translation for a note
        reading : str
            Field name that indicates the reading for a note
        """

        if model_name not in self._cfg['note_types']:
            self._cfg['note_types'][model_name] = {}

        self._cfg['note_types'][model_name]['expression'] = expression
        self._cfg['note_types'][model_name]['meaning'] = meaning
        self._cfg['note_types'][model_name]['reading'] = reading

    def get_tags(self, deck_name: str, word_type: Union[VerbClass, AdjectiveClass]) -> List[str]:
        """Retrieve the tags that label a particular word type for a given deck

        Parameters
        ----------
        deck_name : str
            Name of the relevant source deck
        word_type : Union[VerbClass, AdjectiveClass]
            Word type for which tags are requested

        Returns
        -------
        List[str]
            List of tags associated with the requested word type. Note that this list may be
            empty if no tags have been registered for the given word type.
        """

        if deck_name not in self._cfg['tags']:
            return []

        return self._cfg['tags'][deck_name].get(word_type.value, [])

    def get_model_fields(self, model_name: str) -> Tuple[str, str, str]:
        """Retrieve the relevant fields for the requested model

        Parameters
        ----------
        model_name : str
            Name of the model for which fields are requested

        Returns
        -------
        Tuple[str, str, str]
            Three elements indicating theexpression, meaning, and reading field
            names (respectively).
        """

        if model_name is None:
            raise ValueError("Model name must be provided as a string. Found None.")
        if model_name in self._cfg['note_types']:
            fields = self._cfg['note_types'][model_name]
            return fields['expression'], fields['meaning'], fields['reading']
        return None, None, None
