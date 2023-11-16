def find_first_in_records(records, key: str):
    for record in records:
        if record[key]:
            return record[key]


def records_key_has_value(records, key: str):
    for record in records:
        if record[key]:
            return True
    else:
        return False


def get_specific_record_that_has_value(records, key, value):
    for record in records:
        if record[key] == value:
            return record


def get_meaning_of_part_of_speech(word, part_of_speech: str):
    record = get_specific_record_that_has_value(word.meanings, 'partOfSpeech', part_of_speech)
    if record:
        return record['definitions']


def get_definitions_list(meaning):
    if meaning:
        definitions = []
        for record in meaning:
            definitions.append(record['definition'])
        return definitions


def get_example_list(meaning):
    if meaning:
        examples = []
        for record in meaning:
            try:
                examples.append(record['example'])
            except KeyError:
                continue
        return examples


english_parts_of_speech = [
    'noun',
    'pronoun',
    'verb',
    'adjective',
    'adverb',
    'preposition',
    'conjunction',
    'interjection'
]


class PartsOfSpeech:
    NOUN = 'noun'
    PRONOUN = 'pronoun'
    VERB = 'verb'
    ADJECTIVE = 'adjective'
    ADVERB = 'adverb'
    PREPOSITION = 'preposition'
    CONJUNCTION = 'conjunction'
    INTERJECTION = 'interjection'
