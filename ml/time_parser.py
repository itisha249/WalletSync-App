import dateparser
from datetime import datetime, timedelta
from dateparser.search import search_dates

def parse_time_range(text):
    text = text.lower()

    if "last month" in text:
        today = datetime.today()
        first = today.replace(day=1)
        last_month_end = first - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)
        return {
            "start": last_month_start.strftime("%Y-%m-%d"),
            "end": last_month_end.strftime("%Y-%m-%d")
        }

    elif "this week" in text:
        today = datetime.today()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return {
            "start": start.strftime("%Y-%m-%d"),
            "end": end.strftime("%Y-%m-%d")
        }


    date_range = search_dates(text)
    if date_range and len(date_range) >= 2:
        start = date_range[0][1].strftime("%Y-%m-%d")
        end = date_range[1][1].strftime("%Y-%m-%d")
        return {"start": start, "end": end}

    today = datetime.today()
    return {
        "start": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
        "end": today.strftime("%Y-%m-%d")
    }
