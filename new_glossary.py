import json
import requests
from pydantic import BaseModel
import glossary_utils


class ProcessedWord:
    DEFAULT_PRINT_LIMIT = 5

    def __init__(self, input_word: str):
        parsed_word = ParsedWord.from_json(
            json.dumps(requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{input_word}').json()[0])
        )
        self.spelling = parsed_word.word
        self.transcription = parsed_word.phonetic
        self.audio = parsed_word.get_audio()
        self.definitions_mapping = parsed_word.get_definitions_mapping()
        self.examples_mapping = parsed_word.get_example_mapping()
        self.pos = list(self.definitions_mapping.keys())
        self.print_limit = self.DEFAULT_PRINT_LIMIT

    def set_print_limit(self, limit: int):
        self.print_limit = limit

    def get_pos_definitions(self, requested_pos):
        if requested_pos in self.pos:
            return self.definitions_mapping[requested_pos][0: self.print_limit]

    def get_pos_examples(self, requested_pos):
        if requested_pos in self.pos:
            example_list = self.examples_mapping[requested_pos][0: self.print_limit]
            if example_list:
                return example_list


class ParsedWord(BaseModel):
    word: str
    phonetic: str
    phonetics: list
    meanings: list
    license: dict
    sourceUrls: list

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return cls(**data)

    def has_audio(self):
        return glossary_utils.records_key_has_value(self.phonetics, 'audio')

    def get_audio(self):
        if self.has_audio():
            return glossary_utils.find_first_in_records(self.phonetics, 'audio')

    def get_definitions_mapping(self):
        mapping = {}
        for p_o_s in glossary_utils.english_parts_of_speech:
            meaning = glossary_utils.get_meaning_of_part_of_speech(self, p_o_s)
            if meaning:
                mapping[p_o_s] = glossary_utils.get_definitions_list(meaning)
        return mapping

    def get_example_mapping(self):
        mapping = {}
        for p_o_s in glossary_utils.english_parts_of_speech:
            meaning = glossary_utils.get_meaning_of_part_of_speech(self, p_o_s)
            if meaning:
                mapping[p_o_s] = glossary_utils.get_example_list(meaning)
        return mapping
