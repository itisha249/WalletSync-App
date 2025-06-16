import json
import random

# Define a wide range of intents with templates
intent_templates = {
    "category_expense": ["How much did I spend on {category} {time}?"],
    "income_vs_expense": ["Compare my income and expenses {time}."],
    "max_category": ["Which category had the highest expense {time}?"],
    "daily_summary": ["Show daily expenses for {time}."],
    "weekly_summary": ["Summarize my spending this week."],
    "monthly_summary": ["Summarize my spending this month."],
    "yearly_summary": ["What are my yearly expenses?"],
    "total_income": ["Show total income {time}."],
    "total_expense": ["Show total expenses {time}."],
    "savings_summary": ["How much did I save {time}?"],
    "highest_income_source": ["Which income source earned the most {time}?"],
    "lowest_income_source": ["Which income source earned the least {time}?"],
    "max_transaction": ["Show my largest transaction {time}."],
    "min_transaction": ["Show my smallest transaction {time}."],
    "transactions_by_category": ["List all {category} transactions {time}."],
    "transaction_count": ["How many transactions did I have {time}?"],
    "expenses_by_merchant": ["Show expenses at {merchant} {time}."],
    "income_by_source": ["Income from {source} {time}."],
    "refunds": ["List refunds received {time}."],
    "bills_due": ["What bills are due {time}?"],
    "upcoming_bills": ["What upcoming bills do I have?"],
    "loan_payments": ["How much did I pay in loans {time}?"],
    "credit_card_expense": ["Credit card expenses {time}."],
    "bank_balance": ["What is my current bank balance?"],
    "expense_trend": ["Show my expense trend over the last few months."],
    "income_trend": ["Show my income trend {time}."],
    "budget_status": ["How am I doing on my budget {time}?"],
    "budget_remaining": ["How much budget is left for {category}?"],
    "budget_exceeded": ["Did I exceed budget for {category}?"],
    "cash_flow": ["What was my cash flow {time}?"],
    "investment_summary": ["Summarize my investments {time}."],
    "net_worth": ["What's my net worth {time}?"],
    "frequent_expense": ["What do I spend money on the most?"],
    "frequent_income_source": ["Where does most of my income come from?"],
    "subscription_summary": ["What subscriptions do I have?"],
    "cancelled_subscriptions": ["Which subscriptions were cancelled?"],
    "active_subscriptions": ["List my active subscriptions."],
    "unusual_activity": ["Any unusual transactions {time}?"],
    "missed_payments": ["Did I miss any payments {time}?"],
    "tax_deductions": ["List tax deductible expenses {time}."],
    "charity_donations": ["Charity donations I made {time}?"],
    "travel_expenses": ["Travel related expenses {time}?"],
    "food_expenses": ["Food related spending {time}?"],
    "education_expenses": ["Education expenses {time}?"],
    "medical_expenses": ["Medical expenses {time}?"],
    "groceries_expenses": ["Money spent on groceries {time}?"],
    "utilities_expenses": ["Utility bill payments {time}?"],
    "transportation_expenses": ["Transportation expenses {time}?"],
    "entertainment_expenses": ["Entertainment spending {time}?"],
}

# Sample filler values
categories = ["food", "groceries", "entertainment", "travel", "utilities", "shopping", "education", "healthcare"]
times = ["last week", "this week", "last month", "this month", "in May", "in April", "yesterday", "today", "in 2024"]
merchants = ["Amazon", "Flipkart", "Zomato", "Uber", "Swiggy"]
sources = ["salary", "freelancing", "investments", "bonus", "rental income"]

examples = []

# Generate 10 examples per intent
for intent, templates in intent_templates.items():
    for _ in range(10):
        template = random.choice(templates)
        sentence = template
        if "{category}" in sentence:
            sentence = sentence.replace("{category}", random.choice(categories))
        if "{time}" in sentence:
            sentence = sentence.replace("{time}", random.choice(times))
        if "{merchant}" in sentence:
            sentence = sentence.replace("{merchant}", random.choice(merchants))
        if "{source}" in sentence:
            sentence = sentence.replace("{source}", random.choice(sources))
        examples.append([sentence, intent])

# Shuffle and save to JSON
random.shuffle(examples)
with open("robust_synthetic_intents.json", "w") as f:
    json.dump(examples, f, indent=2)

print(f" Generated {len(examples)} labeled queries in 'robust_synthetic_intents.json'")
