"""Methods for defining models (a.k.a. Notes)"""
from typing import List, Dict, Optional, Tuple, Union
import importlib.resources

import anki.collection
import anki.models

import anki_jpn.resources as anki_jpn_resources
from anki_jpn.enums import Form, Formality, VERB_COMBOS, ADJECTIVE_COMBOS

VERB_MODEL_NAME = "Japanese Verb Conjugation"
ADJECTIVE_MODEL_NAME = "Japanese Adjective Conjugation"

def _resolve_placeholders(template: str, formality: Optional[Formality] = None,
                          form: Optional[Form] = None, field_name: Optional[str] = None) -> str:
    """Resolve the placeholders in the card template definitions

    Parameters
    ----------
    template : str
        Card template with placeholders to be replaced
    formality : Formality | None
        Formality level for the conjugation relevant to the card
    form : Form | None
        Form name for the conjugation relevant to the card
    field_name : str | None
        Name of the Note/Model field containing the conjugation relevant to the card

    Returns
    -------
    str
        Card template text with placeholders resolved
    """

    result = template
    if formality:
        result = result.replace('FORMALITY', formality.value)
    if form:
        result = result.replace('FORM_NAME', form.value)
    if field_name:
        result = result.replace('FIELD_NAME', field_name)
    return result

def add_verb_conjugation_model(col: anki.collection.Collection) -> anki.models.NotetypeDict:
    """Add the Note type for a Japanese Verb Conjugation

    Parameters
    ----------
    col : anki.collection.Collection
        Collection to which the Note type should be added

    Returns
    -------
    anki.models.NotetypeDict
        Dictionary representing information for the Japanese Verb Conjugation Note type
    """

    return _get_model(col, VERB_MODEL_NAME, VERB_COMBOS)

def add_adjective_conjugation_model(col: anki.collection.Collection) -> anki.models.NotetypeDict:
    """Add the Note type for a Japanese Adjective Conjugation

    Parameters
    ----------
    col : anki.collection.Collection
        Collection to which the Note type should be added

    Returns
    -------
    anki.models.NotetypeDict
        Dictionary representing information for the Japanese Adjective Conjugation Note type
    """

    return _get_model(col, ADJECTIVE_MODEL_NAME, ADJECTIVE_COMBOS)

def _get_model(col: anki.collection.Collection, model_name: str,
               combos: List[Tuple[Formality, Form]]) -> anki.models.NotetypeDict:
    """Get a model for tracking conjugations

    Parameters
    ----------
    col : anki.collection.Collection
        Anki Collection
    model_name : str
        Name for the model to be created
    combos : List[Tuple[Formality, Form]]
        List of combos, used to define which conjugation fields should be added

    Returns
    -------
    anki.models.NotetypeDict
        Dictionary representing information for the new Note type
    """

    card_css = importlib.resources.read_text(anki_jpn_resources, 'style.css') # pylint: disable=W4902
    front_template = importlib.resources.read_text(anki_jpn_resources, 'front_template.html') # pylint: disable=W4902
    back_template = importlib.resources.read_text(anki_jpn_resources, 'back_template.html') # pylint: disable=W4902
    insert_ending_spans_text = importlib.resources.read_text(anki_jpn_resources,  # pylint: disable=W4902
                                                             'insert_ending_spans.js')
    back_template = back_template.replace('INSERT_ENDING_SPANS_FUNCTION', insert_ending_spans_text)

    new_model = col.models.new(model_name)
    new_model['css'] = card_css
    base_fields = [
        "Expression",
        "Meaning",
        "Reading"
    ]
    all_fields, all_templates = get_fields_and_templates(base_fields, front_template,
                                                         back_template, combos)
    for field_name in all_fields:
        field_dict = col.models.new_field(field_name)
        col.models.add_field(new_model, field_dict)
    for template in all_templates:
        template_dict = col.models.new_template(template['name'])
        template_dict['qfmt'] = template['qfmt']
        template_dict['afmt'] = template['afmt']
        col.models.add_template(new_model, template_dict)
    return new_model

def get_fields_and_templates(
        base_fields: List[Dict[str, str]], front_template: str,
        back_template: str, combos: List[Tuple[Union[Formality,None], Form]])\
             -> Tuple[List[str], List[Dict[str, str]]]:
    """Configure the fields and templates for a Model

    Parameters
    ----------
    base_fields : List[Dict[str, str]]
        Base list of fields which will be extended with more fields appropriate to the
        model type.
    front_template : str
        Card template for the front of a card (including placeholders)
    back_template : str
        Card template for the back of a card (including placeholders)
    combos : List[Tuple[Formality|None, Form]]
        List of Formality+Form combinations for which fields and cards should be generated

    Returns
    -------
    Tuple[List[str], List[Dict[str, str]]]
        Returns a tuple of the list of field names and a list of templates for cards
    """

    fields = []
    fields.extend(base_fields)
    templates = []

    for formality, form in combos:
        if formality is None:
            formatted_name = form.value.title()
        else:
            formatted_name = f"{formality.value} {form.value}".title()
        fields.append(formatted_name)
        templates.append(
            {
                "name": formatted_name,
                "qfmt": _resolve_placeholders(front_template, formality=formality, form=form),
                "afmt": _resolve_placeholders(back_template, field_name=formatted_name)
            }
        )
    return fields, templates
