def suggest_hashtags(topic):
    topic = topic.lower()
    base_tags = {
        "قهوه": ["#قهوه", "#کافه", "#صبحانه", "#coffee", "#morningvibes"],
        "موفقیت": ["#موفقیت", "#انگیزشی", "#هدف", "#success", "#mindset"],
        "طبیعت": ["#طبیعت", "#کوه", "#سفر", "#nature", "#explore"]
    }
    return " ".join(base_tags.get(topic, ["#ایران", "#زندگی", "#عشق", "#instadaily"]))
