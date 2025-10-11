import streamlit as st

st.set_page_config(page_title="🎯 کپشن‌ساز هوشمند", page_icon="🚀")
st.title("🎯 تولید کپشن، هشتگ و موسیقی بر اساس متن و کشور")

# دیتابیس موضوعات، کپشن‌ها، هشتگ‌ها و موسیقی
caption_db = {
    "آموزشی": {
        "keywords": ["آموزش", "یادگیری", "درس", "مهارت", "نکته"],
        "captions": [
            "یادگیری یعنی قدرت.\nهر روز یه نکته، یه رشد.",
            "با آموزش، آینده‌تو بساز.\nدانش همیشه باهاته.",
            "هر مهارت، یه در جدیده.\nامروز چی یاد گرفتی؟",
            "نکته امروز رو از دست نده!\nیه جمله، یه تغییر."
        ],
        "hashtags": ["#آموزش", "#یادگیری", "#دانش", "#مهارت", "#رشد", "#education", "#learn", "#skills"],
        "music": "https://musicsweb.ir/content/63531/"
    },
    "انگیزشی": {
        "keywords": ["هدف", "موفقیت", "پیشرفت", "دستاورد", "انگیزه"],
        "captions": [
            "تو قوی‌تری از چیزی که فکر می‌کنی.\nهر قدم، یه پیروزیه.",
            "شکست؟ فقط یه قدم به جلو.\nادامه بده.",
            "امروزت رو بساز.\nفردا خودش میاد.",
            "دستاورد کوچیک، مسیر بزرگ.\nتو در راهی."
        ],
        "hashtags": ["#انگیزه", "#موفقیت", "#پیشرفت", "#هدف", "#مثبت_اندیشی", "#motivation", "#success", "#growth"],
        "music": "https://dl.radioahang.site/Music/2025/9/Misha%20-%20MishaOrdibehesht-e3fc.mp3"
    },
    "هنری": {
        "keywords": ["طراحی", "نقاشی", "رنگ", "خلاقیت", "اثر"],
        "captions": [
            "با رنگ‌ها حرف می‌زنیم.\nهر اثر، یه تکه از روحه.",
            "خلق یعنی زنده بودن.\nزیبایی توی سادگیه.",
            "وقتی خلق می‌کنی، آروم می‌شی.\nاین یعنی هنر.",
            "هر خط، یه داستان.\nهر رنگ، یه حس."
        ],
        "hashtags": ["#هنر", "#خلاقیت", "#طراحی", "#نقاشی", "#زیبایی", "#art", "#design", "#creativity"],
        "music": "https://dl.radioahang.site/Music/2025/7/Hamid%20Rakhshandeh%20-%20Nejatam%20Bede-835a.mp3"
    },
    "پشت‌صحنه": {
        "keywords": ["پشت‌صحنه", "ساخت", "تمرین", "آماده‌سازی", "فرآیند"],
        "captions": [
            "پشت هر پست، یه داستانه.\nماجرا از اینجا شروع شد.",
            "جادو اینجاست.\nپشت‌پرده رو ببین.",
            "تمرین، تلاش، تکرار.\nاین یعنی مسیر واقعی.",
            "واقعیت همیشه جذابه.\nیه نگاه پشت‌صحنه بنداز."
        ],
        "hashtags": ["#پشت_صحنه", "#واقعی", "#تیم", "#فرآیند", "#داستان", "#behindthescenes", "#workflow", "#team"],
        "music": "https://dl.radioahang.site/Music/2025/6/Ahange%20Migam%20Tamom%20Shaera-2b41.mp3"
    },
    "سبک زندگی": {
        "keywords": ["زندگی", "روتین", "آرامش", "لایف‌استایل", "سالم"],
        "captions": [
            "زندگی یعنی لذت از لحظه‌ها.\nتفاوت توی جزئیاته.",
            "سبک زندگی = امضای شخصیت.\nبا آرامش زندگی کن.",
            "زندگی سالم، ذهن آروم.\nروتینت رو بساز.",
            "هر انتخاب، یه سبک.\nتو انتخاب می‌کنی."
        ],
        "hashtags": ["#سبک_زندگی", "#لایف_استایل", "#زندگی_سالم", "#آرامش", "#انتخاب", "#lifestyle", "#wellness", "#routine"],
        "music": "https://dl.radioahang.site/Music/2025/6/Ahange%20Migam%20Tamom%20Shaera-2b41.mp3"
    },
    "طنز": {
        "keywords": ["شوخی", "طنز", "خنده", "لبخند", "با مزه"],
        "captions": [
            "اگه نخندیدی، دوباره بخونش!\nطنز یعنی زاویه خنده‌دار.",
            "زندگی بدون شوخی؟\nجدی نیست!",
            "شوخی کوچیک، حال خوب بزرگ.\nبخند، زندگی کوتاهه.",
            "طنز یعنی بازی با واقعیت.\nهمه‌چی آسون‌تر می‌شه."
        ],
        "hashtags": ["#طنز", "#شوخی", "#لبخند", "#حال_خوب", "#خنده", "#funny", "#humor", "#smile"],
        "music": "https://dl.radioahang.site/Music/2025/7/Saeb%20Sadeghi%20-%20Zuckerberg%20-9f72.mp3"
    },
    "ماشین": {
        "keywords": ["ماشین", "خودرو", "رانندگی", "سرعت", "جاده", "اتومبیل"],
        "captions": [
            "ماشینت حرف می‌زنه؟\nگوش بده، جاده منتظره.",
            "سرعت خوبه،\nوقتی کنترل دست توئه.",
            "ماشین فقط وسیله نیست.\nیه حس آزادیه.",
            "هر رانندگی، یه سفره.\nهر سفر، یه داستان."
        ],
        "hashtags": ["#ماشین", "#خودرو", "#جاده", "#رانندگی", "#اتومبیل", "#car", "#drive", "#roadtrip"],
        "music": "https://www.jenabmusic.com/آهنگ-پر-انرژی-شاد-ماشین"
    }
}

# ورودی‌ها
country = st.selectbox("🌍 کشور مورد نظر:", ["ایران", "ترکیه", "آلمان", "امارات", "آمریکا"])
user_input = st.text_input("✍️ چند کلمه درباره پستت بنویس:")
search_input = st.text_input("🔍 جست‌وجوی موضوع:")

# تشخیص موضوع
def detect_topic(text):
    for topic, data in caption_db.items():
        for word in data["keywords"]:
            if word in text:
                return topic
    return None

filtered_topics = [topic for topic in caption_db if search_input.lower() in topic.lower()]
selected_topic = st.selectbox("📌 انتخاب موضوع:", filtered_topics if filtered_topics else list(caption_db.keys()))
final_topic = detect_topic(user_input) if user_input else selected_topic

# نمایش خروجی‌ها
if final_topic:
    st.success(f"موضوع انتخاب‌شده: {final_topic}")

    if st.button("✍️ نمایش کپشن‌ها"):
        for i, caption in enumerate(caption_db[final_topic]["captions"], 1):
            st.markdown(f"*{i}.* {caption}")

    if st.button("🏷️ نمایش هشتگ‌ها"):
        st.write(" ".join(caption_db[final_topic]["hashtags"]))

    if st.button("🎵 نمایش موسیقی ترند"):
        st.markdown(f"[🎵 دانلود مستقیم آهنگ ترند برای موضوع {final_topic}]({caption_db[final_topic]['music']})")
