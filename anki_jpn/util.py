def delta_split(dictionary_form, conjugation):
    if dictionary_form == conjugation:
        # degenerate case for plain short form
        return conjugation, ''
    split_index = min(len(dictionary_form), len(conjugation))

    while True:
        if split_index == 0:
            break

        open_brackets = conjugation[split_index:].count('[')
        close_brackets = conjugation[split_index:].count(']')

        if dictionary_form[:split_index] != conjugation[:split_index] or \
            close_brackets > open_brackets or \
            conjugation[split_index] == '[':
        
            split_index -= 1
        else:
            break

    return conjugation[:split_index], conjugation[split_index:]