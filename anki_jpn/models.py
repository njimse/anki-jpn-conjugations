import copy
from typing import List, Dict, Optional, Tuple, Union
import importlib.resources

import genanki

import anki_jpn.resources as anki_jpn_resources
from anki_jpn.enums import Form, Formality, ModelType, VERB_COMBOS, ADJECTIVE_COMBOS

def resolve_placeholders(template: str, formality: Optional[Formality] = None, form: Optional[Form] = None,
         field_name: Optional[str] = None) -> str:
    result = template
    if formality:
        result = result.replace('FORMALITY', formality.value)
    if form:
        result = result.replace('FORM_NAME', form.value)
    if field_name:
        result = result.replace('FIELD_NAME', field_name)
    return result

def get_model(model_id: int, model_name: str, model_type: ModelType = ModelType.VERB) -> genanki.Model:
    css_file = importlib.resources.files(anki_jpn_resources)/'style.css'
    with css_file.open("rt") as f:
        card_css = f.read()
    front_template_file = importlib.resources.files(anki_jpn_resources)/'front_template.html'
    with front_template_file.open("rt") as f:
        front_template = f.read()
    back_template_file = importlib.resources.files(anki_jpn_resources)/'back_template.html'
    with back_template_file.open("rt") as f:
        back_template = f.read()
    insert_ending_spans_file = importlib.resources.files(anki_jpn_resources)/'insert_ending_spans.js'
    with insert_ending_spans_file.open("rt") as f:
        insert_ending_spans_text = f.read()
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
    set_fields_and_cards(new_model, base_fields, front_template, back_template, combos)

    return new_model

def set_fields_and_cards(model: genanki.Model, base_fields: List[Dict[str, str]],
                              front_template: str, back_template: str, combos: List[Tuple[Union[Formality,None], Form]]) -> None:
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
                "qfmt": resolve_placeholders(front_template, formality=formality, form=form),
                "afmt": resolve_placeholders(back_template, field_name=formatted_name)
            }
        )
    model.set_fields(fields)
    model.set_templates(templates)
