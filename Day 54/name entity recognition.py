import nltk
from nltk.tokenize import word_tokenize

text = "John Doe is the CEO of OPenAI. He lives in San Francisco."
person_lexicon = {"John Doe", "Alice", "Bob"}
organisation_lexicon = {"OpenAI", "Google", "Microsoft"}
location_lexicon = {"San Francisco", "New York", "Los Angeles"}

def lexicon_based_ner(text):
    entities = []
    tokens = word_tokenize(text)
    
    # Join tokens to reconstruct original words
    for lexicon, label in [(organisation_lexicon, "ORG")]:
        for entity in lexicon:
            if entity in text:
                entities.append((label, entity))
    
    return entities

print("Lexicon-based NER: ")
print(lexicon_based_ner(text))