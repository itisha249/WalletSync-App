# from transformers import pipeline
# from difflib import get_close_matches

# class EntityExtractor:
#     def __init__(self):
#         self.ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
#         self.categories = [
#             "food", "entertainment", "groceries", "shopping",
#             "bills", "transport", "travel", "utilities", "rent", "salary"
#         ]

#     def extract_entities(self, text):
#         ner_results = self.ner(text)
#         for ent in ner_results:
#             word = ent["word"].lower()
#             match = get_close_matches(word, self.categories, n=1, cutoff=0.8)
#             if match:
#                 return {"category": match[0]}
        
#         # fallback: fuzzy scan full text
#         for cat in self.categories:
#             if cat in text.lower():
#                 return {"category": cat}

#         return {"category": None}

# import spacy
# from spacy.matcher import PhraseMatcher
# #import nltk as nlp

# class EntityExtractor:
#     def __init__(self):
#         self.nlp = spacy.load("en_core_web_sm")
#         self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")

#         self.categories = [
#             "food", "entertainment", "groceries", "shopping",
#             "bills", "transport", "travel", "utilities", "rent", "salary"
#         ]

#         patterns = [self.nlp.make_doc(cat) for cat in self.categories]
#         self.matcher.add("CATEGORY", patterns)

#     def extract_entities(self, text):
#         doc = self.nlp(text)
#         matches = self.matcher(doc)
#         matched = None
#         for match_id, start, end in matches:
#             matched = doc[start:end].text.lower()
#             break  # Return first match for now
#         return {"category": matched}

import spacy
from spacy.matcher import PhraseMatcher
from rapidfuzz import process

class EntityExtractor:
    def __init__(self):  # Correct constructor
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")

        self.categories = {
            "food": ["restaurant", "dining", "meal", "breakfast", "lunch", "dinner", "snack"],
            "entertainment": ["cinema", "movies", "concert", "game", "netflix", "theater"],
            "groceries": ["supermarket", "vegetables", "fruits", "grocery"],
            "shopping": ["clothes", "apparel", "shoes", "fashion"],
            "bills": ["electricity", "water", "gas", "mobile", "internet", "bill"],
            "transport": ["bus", "train", "metro", "uber", "taxi", "cab"],
            "travel": ["flight", "hotel", "trip", "vacation", "journey"],
            #"utilities": ["electricity", "water", "internet", "gas"],
            "rent": ["house rent", "apartment", "rental"],
            "salary": ["income", "paycheck", "wage", "payment"]
        }

        self.synonym_map = {}
        self.all_terms = []
        patterns = []

        for category, synonyms in self.categories.items():
            # Add category itself
            self.synonym_map[category] = category
            self.all_terms.append(category)
            patterns.append(self.nlp.make_doc(category))

            # Add each synonym
            for synonym in synonyms:
                self.synonym_map[synonym.lower()] = category
                self.all_terms.append(synonym.lower())
                patterns.append(self.nlp.make_doc(synonym))

        self.matcher.add("CATEGORY", patterns)

    def extract_entities(self, text):
        doc = self.nlp(text)

        # Exact match
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            term = doc[start:end].text.lower()
            print(f"[Exact Match] Found: {term}")
            if term in self.synonym_map:
                return {"category": self.synonym_map[term]}

        # Fuzzy fallback
        words = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]
        print(f"[Tokens for Fuzzy Matching]: {words}")
        for word in words:
            best_match, score, _ = process.extractOne(word, self.all_terms)
            print(f"[Fuzzy] Word: '{word}' → Match: '{best_match}' (Score: {score})")
            if score > 80:
                return {"category": self.synonym_map[best_match]}

        return {"category": None}
