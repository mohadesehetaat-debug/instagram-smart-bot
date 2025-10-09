from datetime import datetime

def suggest_post_time():
    now = datetime.now()
    hour = now.hour
    if 6 <= hour <= 9:
        return "🕕 بهترین زمان: صبح زود (۶ تا ۹)"
    elif 17 <= hour <= 20:
        return "🕔 بهترین زمان: عصر (۵ تا ۸)"
    else:
        return "🕘 بهترین زمان: فردا صبح یا عصر"
