def map_to_api(parsed):
    base_url = "/report"
    intent = parsed.get("intent")

    if intent == "category_expense":
        category = parsed.get("category", "all")
        start = parsed["time_range"]["start"]
        end = parsed["time_range"]["end"]
        return f"{base_url}/by-category?category={category}&start={start}&end={end}"

    elif intent == "income_vs_expense":
        start = parsed["time_range"]["start"]
        end = parsed["time_range"]["end"]
        return f"{base_url}/income-vs-expense?start={start}&end={end}"

    elif intent == "max_category":
        start = parsed["time_range"]["start"]
        end = parsed["time_range"]["end"]
        return f"{base_url}/max-category?start={start}&end={end}"

    elif intent == "daily_summary":
        start = parsed["time_range"]["start"]
        end = parsed["time_range"]["end"]
        return f"{base_url}/daily-summary?start={start}&end={end}"

    return base_url + "/unknown"
