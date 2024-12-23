"""Methods for defining models (a.k.a. Notes)"""
from typing import List, Dict, Optional, Tuple, Union
import importlib.resources

import genanki

import anki_jpn.resources as anki_jpn_resources
from anki_jpn.enums import Form, Formality, ModelType, VERB_COMBOS, ADJECTIVE_COMBOS

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

def get_model(model_id: int, model_name: str, model_type: ModelType = ModelType.VERB)\
    -> genanki.Model:
    """Get a model for tracking conjugations
    
    Parameters
    ----------
    model_id : int
        Integer ID for the model to be created
    model_name : str
        Name for the model to be created
    model_type : ModelType
        Type of the model to be created
    
    Returns
    -------
    genanki.Model
        Model object for defining a Note type
    """

    card_css = importlib.resources.read_text(anki_jpn_resources, 'style.css')
    front_template = importlib.resources.read_text(anki_jpn_resources, 'front_template.html')
    back_template = importlib.resources.read_text(anki_jpn_resources, 'back_template.html')
    insert_ending_spans_text = importlib.resources.read_text(anki_jpn_resources,
                                                             'insert_ending_spans.js')
    back_template = back_template.replace('INSERT_ENDING_SPANS_FUNCTION', insert_ending_spans_text)
    new_model = genanki.Model(model_id, model_name, css=card_css)
    base_fields = [
        {"name": "expression"},
        {"name": "meaning"},
        {"name": "reading"}
    ]
    if model_type == ModelType.VERB:
        combos = VERB_COMBOS
    else:
        combos = ADJECTIVE_COMBOS
    _set_fields_and_templates(new_model, base_fields, front_template, back_template, combos)

    return new_model

def _set_fields_and_templates(
        model: genanki.Model, base_fields: List[Dict[str, str]], front_template: str,
        back_template: str, combos: List[Tuple[Union[Formality,None], Form]]) -> None:
    """Configure the fields and templates for a Model
    
    Parameters
    ----------
    model : genanki.Model
        Model to be updated with fields and card templates. NOTE: this method modifies
        the model in-place!
    base_fields : List[Dict[str, str]]
        Base list of fields which will be extended with more fields appropriate to the
        model type.
    front_template : str
        Card template for the front of a card (including placeholders)
    back_template : str
        Card template for the back of a card (including placeholders)
    combos : List[Tuple[Formality|None, Form]]
        List of Formality+Form combinations for which fields and cards should be generated
    """

    fields = []
    fields.extend(base_fields)
    templates = []

    for formality, form in combos:
        if formality is None:
            formatted_name = form.value.title()
        else:
            formatted_name = f"{formality.value} {form.value}".title()
        fields.append({"name": formatted_name})
        templates.append(
            {
                "name": formatted_name,
                "qfmt": _resolve_placeholders(front_template, formality=formality, form=form),
                "afmt": _resolve_placeholders(back_template, field_name=formatted_name)
            }
        )
    model.set_fields(fields)
    model.set_templates(templates)
