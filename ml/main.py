from intent_classifier import IntentClassifier
from entity_extractor import EntityExtractor
from time_parser import parse_time_range
from api_mapper import map_to_api

intent_clf = IntentClassifier()
ner = EntityExtractor()

def handle_query(query):
    intent = intent_clf.predict(query)
    entities = ner.extract_entities(query)
    time_range = parse_time_range(query)
    parsed = {
        "intent": intent,
        **entities,
        "time_range": time_range
    }
    api_url = map_to_api(parsed)
    return parsed, api_url

if __name__ == "__main__":
    while True:
        q = input("\n💬 Enter your financial query (or 'exit'): ")
        if q.lower() == "exit":
            break
        parsed, url = handle_query(q)
        print("\n📦 Parsed Output:", parsed)
        print("🔗 API URL:", url)

# “What was my income vs expense last month?”
# “Which category had the highest spending in May?”
# “How much did I spend on entertainment this week?”
# “Show daily expenses for the last 7 days.”
#"How much did I spend on restraunt this week?"