
# WalletSync: Natural Language Financial Query Parser

This project is an intelligent financial query parser that extracts structured information (intent, category, and time range) from user questions like:

> "How much did I spend on restrunt this week?"

The system can handle:
- **Misspellings** (e.g., "restrunt" → "restaurant")
- **Synonyms** (e.g., "dining" → "food")
- **Natural language time ranges** (e.g., "last month", "this week")

---

example:

How much did I spend on electricity this week?


Parsed Output: {'intent': 'category_expense',
                'category': 'utilities',
                'time_range': {'start': '2025-06-16', 'end': '2025-06-22'}
                }
🔗 API URL: /report/by-category?category=utilities&start=2025-06-16&end=2025-06-22

Features

-  **Intent Detection** — Understands user intent (e.g., asking for expense report)
-  **Category Extraction** — Detects categories like `food`, `shopping`, `bills` using phrase matching and fuzzy logic
-  **Date Range Extraction** — Converts phrases like "this week" to actual date ranges
-  **Misspelling Handling** — Uses fuzzy matching (via RapidFuzz) to correct typos

---

##  Tech Stack

- [Python](https://www.python.org/)
- [spaCy](https://spacy.io/) (NLP & tokenization)
- [PhraseMatcher](https://spacy.io/api/phrasematcher) (for exact/synonym matching)
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) (for fuzzy string matching)

---

## Installation

git clone https://github.com/yourusername/walletsync-parser.git
cd walletsync-parser
pip install -r requirements.txt
Also run:

python -m spacy download en_core_web_sm


Project Structure


walletsync-parser/
├── api_mapper.py    # For API mapping
├── intent_classifier.py    # Intent detection module
├── time_parser.py          # Extracts and formats time ranges
├── entity_extractor.py     # for category mapping    
|__ intent_generation.py    # intents with templates
|__main.py                  # Combines all logic into one function
└── README.md               # Project overview


 Example Queries
"How much did I spend on restrunt this week?"

"Show my bills for last month"

"Groceries expenses in April"

"What was my travel cost in May?"




Itisha Patel
AI/NLP Engineer in Progress 👩‍💻
Email: itishahmt@gmal.com

