"""Methods for defining models (a.k.a. Notes)"""
from copy import deepcopy
import re
from typing import List, Dict, Tuple, Union
import importlib.resources

import anki.collection
import anki.models

from . import resources as anki_jpn_resources
from .enums import Form, Formality

COMBO_HASHES = {
    (Formality.POLITE, Form.NON_PAST): 'uNCk',
    (Formality.POLITE, Form.NON_PAST_NEG): 'pyJD',
    (Formality.POLITE, Form.PAST): 'FWhU',
    (Formality.POLITE, Form.PAST_NEG): 'OfA3',
    (Formality.POLITE, Form.VOLITIONAL): 'TiKs',
    (None, Form.TE): 'g1G0',
    (Formality.PLAIN, Form.NON_PAST): 'AUXG',
    (Formality.PLAIN, Form.NON_PAST_NEG): '5hRQ',
    (Formality.PLAIN, Form.PAST): 'wlxY',
    (Formality.PLAIN, Form.PAST_NEG): 'X9LC',
    (Formality.POLITE, Form.POTENTIAL_NON_PAST): 'asc6',
    (Formality.POLITE, Form.POTENTIAL_NON_PAST_NEG): 'TqmV',
    (Formality.POLITE, Form.POTENTIAL_PAST): 'r5s9',
    (Formality.POLITE, Form.POTENTIAL_PAST_NEG): '1Ut6',
    (None, Form.POTENTIAL_TE): 'mUs0',
    (Formality.PLAIN, Form.POTENTIAL_NON_PAST): 'fJQR',
    (Formality.PLAIN, Form.POTENTIAL_NON_PAST_NEG): '0uSU',
    (Formality.PLAIN, Form.POTENTIAL_PAST): 'h8MI',
    (Formality.PLAIN, Form.POTENTIAL_PAST_NEG): 'xisC',
    (Formality.POLITE, Form.TAI_NON_PAST): '9Rq6',
    (Formality.POLITE, Form.TAI_NON_PAST_NEG): 'MZD6',
    (Formality.POLITE, Form.TAI_PAST): 'F3Ve',
    (Formality.POLITE, Form.TAI_PAST_NEG): 'mwjc',
    (None, Form.TAI_TE): 'kHaM',
    (Formality.PLAIN, Form.TAI_NON_PAST): '1lct',
    (Formality.PLAIN, Form.TAI_NON_PAST_NEG): 'L0D7',
    (Formality.PLAIN, Form.TAI_PAST): 'uRpq',
    (Formality.PLAIN, Form.TAI_PAST_NEG): 'EgRi'
}

VERB_COMBOS = [
    (Formality.POLITE, Form.NON_PAST),
    (Formality.POLITE, Form.NON_PAST_NEG),
    (Formality.POLITE, Form.PAST),
    (Formality.POLITE, Form.PAST_NEG),
    (Formality.POLITE, Form.VOLITIONAL),
    (None, Form.TE),
    (Formality.PLAIN, Form.NON_PAST),
    (Formality.PLAIN, Form.NON_PAST_NEG),
    (Formality.PLAIN, Form.PAST),
    (Formality.PLAIN, Form.PAST_NEG),
    (Formality.POLITE, Form.POTENTIAL_NON_PAST),
    (Formality.POLITE, Form.POTENTIAL_NON_PAST_NEG),
    (Formality.POLITE, Form.POTENTIAL_PAST),
    (Formality.POLITE, Form.POTENTIAL_PAST_NEG),
    (None, Form.POTENTIAL_TE),
    (Formality.PLAIN, Form.POTENTIAL_NON_PAST),
    (Formality.PLAIN, Form.POTENTIAL_NON_PAST_NEG),
    (Formality.PLAIN, Form.POTENTIAL_PAST),
    (Formality.PLAIN, Form.POTENTIAL_PAST_NEG),
    (Formality.POLITE, Form.TAI_NON_PAST),
    (Formality.POLITE, Form.TAI_NON_PAST_NEG),
    (Formality.POLITE, Form.TAI_PAST),
    (Formality.POLITE, Form.TAI_PAST_NEG),
    (None, Form.TAI_TE),
    (Formality.PLAIN, Form.TAI_NON_PAST),
    (Formality.PLAIN, Form.TAI_NON_PAST_NEG),
    (Formality.PLAIN, Form.TAI_PAST),
    (Formality.PLAIN, Form.TAI_PAST_NEG),
]

ADJECTIVE_COMBOS = [
    (Formality.POLITE, Form.NON_PAST),
    (Formality.POLITE, Form.NON_PAST_NEG),
    (Formality.POLITE, Form.PAST),
    (Formality.POLITE, Form.PAST_NEG),
    (None, Form.TE),
    (Formality.PLAIN, Form.NON_PAST),
    (Formality.PLAIN, Form.NON_PAST_NEG),
    (Formality.PLAIN, Form.PAST),
    (Formality.PLAIN, Form.PAST_NEG)
]

def combo_to_field_name(form: Form, formality: Union[Formality, None]) -> str:
    """Using the form and formality, generate a formatted name suitable for labeling a field

    Parameters
    ----------
    form : Form
        Form name for the conjugation
    formality : Formality
        Formality level of the conjugation
    """
    hash_str = COMBO_HASHES[(formality, form)]
    if formality is None:
        formatted_name = f"{form.label().title()} <{hash_str}>"
    else:
        formatted_name = f"{formality.value.title()} {form.label().title()} <{hash_str}>"
    return formatted_name

def add_or_update_verb_model(model_manager: anki.models.ModelManager, model_name: str,
                             color_dict: Dict[str, Dict[str, str]]=None) -> None:
    """Ensure that the model manager is aware of an up-to-date version of the verb model

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        ModelManager for the collection to be updated with the verb model
    model_name : str
        Name to be used for the verb model
    color_dict : Dict[str, Dict[str, str]]
        Configuration for colors to use for the style sheet
    """

    _add_or_update_model(model_manager, model_name, VERB_COMBOS, color_dict)

def add_or_update_adjective_model(model_manager: anki.models.ModelManager, model_name: str,
                                  color_dict: Dict[str, Dict[str, str]]=None) -> None:
    """Ensure that the model manager is aware of an up-to-date version of the adjective model

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        ModelManager for the collection to be updated with the verb model
    model_name : str
        Name to be used for the verb model
    color_dict : Dict[str, Dict[str, str]]
        Configuration for colors to use for the style sheet
    """

    _add_or_update_model(model_manager, model_name, ADJECTIVE_COMBOS, color_dict)

def _add_or_update_model(
        model_manager: anki.models.ModelManager, model_name: str,
        combos: List[Tuple[Formality, Form]], color_dict: Dict[str, Dict[str, str]]=None) -> None:
    """Ensure that the model manager is aware of an up-to-date version of the adjective model

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        ModelManager for the collection to be updated with the verb model
    model_name : str
        Name to be used for the verb model
    color_dict : Dict[str, Dict[str, str]]
        Configuration for colors to use for the style sheet
    """

    model = model_manager.new(model_name)
    _create_model(model_manager, model, combos, color_dict)
    existing_model = model_manager.by_name(model_name)
    if existing_model is None:
        # Simply add the newly created model
        model_manager.add(model)
    elif _model_diffs(model, existing_model):
        # resolve the differences
        updated_model = _resolve_model_diffs(model_manager, existing_model, model)
        _ensure_order(model_manager, updated_model, model)
        model_manager.update_dict(updated_model)


def _model_diffs(a: anki.models.NotetypeDict, b: anki.models.NotetypeDict) -> bool:
    """Compare two models and determine if there are relevant differences

    Parameters
    ----------
    a : anki.models.NotetypeDict
        The first of the models to be compared
    b : anki.models.NotetypeDict
        The second of the models to be compared

    Returns
    -------
    bool
        True if differences were detected. False otherwise.
    """

    if a['css'] != b['css']:
        return True
    if len(a['flds']) != len(b['flds']):
        return True
    for a_field, b_field in zip(a['flds'], b['flds']):
        if a_field['name'] != b_field['name']:
            return True
    if len(a['tmpls']) != len(b['tmpls']):
        return True
    for a_template, b_template in zip(a['tmpls'], b['tmpls']):
        if a_template['name'] != b_template['name'] \
            or a_template['qfmt'] != b_template['qfmt'] \
            or a_template['afmt'] != b_template['afmt']:

            return True

    return False

def _hash_match(left: str, right: str) -> bool:
    """Check if the hashes in two inputs match

    Parameters
    ----------
    left : str
        Left side of the comparison
    right : str
        Right side of the comparison

    Returns
    -------
    bool
        True if the hashes are equivalent, False if not equivalent. If hashes
        are not detected in both the left and right inputs, then a simple string
        comparison is performed.
    """

    try:
        left_hash = re.search('<([^>]+)>$', left).group(1)
        right_hash = re.search('<([^>]+)>$', right).group(1)
    except AttributeError:
        return left == right
    return left_hash == right_hash

def _resolve_model_diffs( # pylint: disable=R0912
        model_manager: anki.models.ModelManager, existing_model: anki.models.NotetypeDict,
        target_model: anki.models.NotetypeDict) -> anki.models.NotetypeDict:
    """Resolve the differences between an existing model and a target model

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        ModelManager for the collection to be updated with the verb model
    existing_model : anki.models.NotetypeDict
        The existing model that is to be updated
    target_model : anki.models.NotetypeDict
        A model representing the most up-to-date expectations for fields and templates

    Returns
    -------
    anki.models.NotetypeDict
        Updated model with necessary changes
    """
    updated_model = deepcopy(existing_model)

    updated_model['css'] = target_model['css']

    # Remove any fields that are not in the target model
    for field_dict in list(updated_model['flds']):
        has_match = False
        for target_field_dict in target_model['flds']:
            if _hash_match(target_field_dict['name'], field_dict['name']):
                if target_field_dict['name'] != field_dict['name']:
                    model_manager.rename_field(
                        existing_model, field_dict, target_field_dict['name'])
                has_match = True
                continue
        if not has_match:
            model_manager.remove_field(updated_model, field_dict)

    # Add any templates that are missing in the existing model.
    # Note that we do this before removing templates to ensure that we never
    # reduce the template count to 0
    for template_dict in target_model['tmpls']:
        has_match = False
        for updated_template in updated_model['tmpls']:
            if _hash_match(updated_template['name'], template_dict['name']):

                # Note that as long as the hashes match, we want to pick up
                # any updates to the name or the front/back templates
                updated_template['name'] = template_dict['name']
                updated_template['qfmt'] = template_dict['qfmt']
                updated_template['afmt'] = template_dict['afmt']

                has_match = True
                continue

        if not has_match:
            model_manager.add_template(updated_model, template_dict)

    # Remove any templates that are not in the target model
    for template_dict in list(updated_model['tmpls']):
        has_match = False
        for target_template in target_model['tmpls']:
            if target_template['name'] == template_dict['name'] \
                and target_template['qfmt'] == template_dict['qfmt'] \
                and target_template['afmt'] == template_dict['afmt']:

                has_match = True
        if not has_match:
            model_manager.remove_template(updated_model, template_dict)

    # Add any fields that are missing in the existing model
    for field_dict in target_model['flds']:
        if not any(existing_field_dict['name'] == field_dict['name'] \
                   for existing_field_dict in updated_model['flds']):
            model_manager.add_field(updated_model, field_dict)

    return updated_model

def _ensure_order(
        model_manager: anki.models.ModelManager, updated_model: anki.models.NotetypeDict,
        target_model: anki.models.NotetypeDict) -> None:
    """Ensure that the order of the fields and templates matches the expectations of
    the target model

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        ModelManager for the collection to be updated with the verb model
    updated_model : anki.models.NotetypeDict
        The updated model which may be modified in-place to align with the target model
    target_model : anki.models.NotetypeDict
        A model representing the most up-to-date expectations for fields and templates

    """

    index = 0
    while index < len(updated_model['flds']):
        target_field = target_model['flds'][index]
        for updated_field in list(updated_model['flds'][index+1:]):
            if updated_field['name'] == target_field['name']:
                model_manager.reposition_field(updated_model, updated_field, index)
        index += 1

    index = 0
    while index < len(updated_model['tmpls']):
        target_template = target_model['tmpls'][index]
        for updated_template in list(updated_model['tmpls'][index+1:]):
            if updated_template['name'] == target_template['name']:
                model_manager.reposition_template(updated_model, updated_template, index)
        index += 1


def _resolve_placeholders(template: str, substitutions: Dict[str, str]) -> str:
    """Resolve the placeholders in the card template definitions

    Parameters
    ----------
    template : str
        Card template with placeholders to be replaced
    substitutions : Dict[str, str]
        Placeholder strings and the corresponding replacements

    Returns
    -------
    str
        Card template text with placeholders resolved
    """

    result = template
    for placeholder, replacement in substitutions.items():
        if replacement is not None:
            result = result.replace(placeholder, replacement)
    return result

def _create_model(model_manager: anki.models.ModelManager, model: anki.models.NotetypeDict,
               combos: List[Tuple[Formality, Form]], color_dict: Dict[str, Dict[str, str]]=None) \
                -> anki.models.NotetypeDict:
    """Get a model for tracking conjugations

    Parameters
    ----------
    model_manager : anki.models.ModelManager
        Model manager for the collection being modified
    model : anki.models.NotetypeDict
        Empty model to be filled out with content
    combos : List[Tuple[Formality, Form]]
        List of combos, used to define which conjugation fields should be added
    color_dict : Dict[str, Dict[str, str]]
        Configuration for colors to use for the style sheet

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

    if color_dict:
        color_overrides = color_dict
    else:
        color_overrides = {}
    css_subs = {
        "POLITE_DAY": color_overrides.get('day', {}).get('polite', '#4DB01C'),
        "POLITE_NIGHT": color_overrides.get('night', {}).get('polite', '#4DB01C'),
        "PLAIN_DAY": color_overrides.get('day', {}).get('plain', '#2A6DEC'),
        "PLAIN_NIGHT": color_overrides.get('night', {}).get('plain', '#2A6DEC')
    }
    model['css'] = _resolve_placeholders(card_css, css_subs)
    all_fields, all_templates = get_fields_and_templates(["Expression", "Meaning", "Reading"],
                                                         front_template, back_template, combos)
    for field_name in all_fields:
        model_manager.add_field(model, model_manager.new_field(field_name))
    for template in all_templates:
        template_dict = model_manager.new_template(template['name'])
        template_dict['qfmt'] = template['qfmt']
        template_dict['afmt'] = template['afmt']
        model_manager.add_template(model, template_dict)
    return model

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
        formatted_name = combo_to_field_name(form, formality)
        fields.append(formatted_name)
        subs = {
            "FIELD_NAME": formatted_name,
            "FORMALITY": formality.value.title() if formality is not None else 'Polite',
            "FORM_NAME": form.label().title(),
        }
        templates.append(
            {
                "name": formatted_name,
                "qfmt": _resolve_placeholders(front_template, subs),
                "afmt": _resolve_placeholders(back_template, subs)
            }
        )
    return fields, templates
