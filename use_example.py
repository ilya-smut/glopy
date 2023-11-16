from new_glossary import ProcessedWord
import glossary_utils

word = ProcessedWord('clingy')
pos_preset = glossary_utils.PartsOfSpeech()
print(word.spelling)
print(word.transcription)
print(word.audio)
for pos in word.pos:
    definitions = word.get_pos_definitions(pos)
    examples = word.get_pos_examples(pos)
    print(pos)
    if definitions:
        print('Definitions:')
        for definition in definitions:
            print(definition)
    if examples:
        print('Examples')
        for example in examples:
            print(example)
