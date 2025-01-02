import anki.notes
from typing import List, Tuple, Optional

from anki_jpn.enums import Form, Formality

class DeckUpdater:

    def __init__(self, col, deck_id, model, combo_list, field_map):
        self._col = col
        self._deck_id = deck_id
        self._model = model
        self._combo_list = combo_list
        self._field_map = field_map

    def add_note_to_deck(self, source_note, conjugations):
        new_note = anki.notes.Note(self._col, self._model)
        self._rollover_note(source_note, new_note)
        self._expand_note(new_note, conjugations)
        self._col.add_note(new_note, self._deck_id)

    def _rollover_note(self, old_note: anki.notes.Note, new_note: anki.notes.Note) -> None:
        """Copy relevant fields from an old note into a new note

        Parameters
        ----------
        old_note : anki.notes.Note
            Old note from which information will be copied
        new_note : anki.notes.Note
            New note where information will be added
        """

        new_note.fields = [
            old_note.fields[self._field_map['expression']],
            old_note.fields[self._field_map['meaning']],
            old_note.fields[self._field_map['reading']]
        ]

    def _expand_note(self, note: anki.notes.Note,
                    forms: List[Tuple[str, Optional[Formality], Form]]) -> None:
        """Expand a note with the provided conjugations

        Parameters
        ----------
        note : anki.notes.Note
            Note to be expanded with conjugations
        combo_list : List[Tuple[Optional[Formality], Form]]
            List of combos. The expectation is that the combo_list follows the same order as the fields
            that are expected for the target Note type
        forms : List[Tuple[str, Optional[Formality], Form]]
            List of conjugations and their corresponding formality and form information.
        """

        note_fields = ['']*len(self._combo_list)

        for conjugation, form, formality in forms:
            note_fields[self._combo_list.index((formality, form))] = conjugation

        note.fields.extend(note_fields)
        for t in note.tags:
            note.add_tag(t)