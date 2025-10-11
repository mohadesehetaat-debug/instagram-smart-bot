import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="کپشن‌ساز هوشمند اینستاگرام", page_icon="🎨")
st.title("🎨 کپشن‌ساز هوشمند اینستاگرام")

# دیتاست کپشن‌های طولانی
data = {
    "topic": ["شروع پروژه", "شروع پروژه", "شروع پروژه", "محصول جدید", "محصول جدید", "محصول جدید"],
    "tone": ["انگیزشی", "انگیزشی", "انگیزشی", "تبلیغاتی", "تبلیغاتی", "تبلیغاتی"],
    "caption": [
        "شروع هر پروژه یعنی شروع یه مسیر تازه. قراره با هم بسازیم، یاد بگیریم، و رشد کنیم. این فقط یه پست نیست، یه تعهده برای ساختن آینده‌ای که باورش داریم. هر قدمی که برمی‌داریم، ما رو به هدف نزدیک‌تر می‌کنه. اینجا نقطه‌ی شروعه، نه پایان.",
        "وقتی تصمیم می‌گیری شروع کنی، یعنی به خودت ایمان داری. این پروژه قراره نشون بده که با تلاش و خلاقیت، هر چیزی ممکنه. ما با هم می‌سازیم، با هم یاد می‌گیریم، و با هم موفق می‌شیم. این فقط یه پروژه نیست، یه مسیر الهام‌بخشه.",
        "شروع پروژه یعنی روشن‌کردن چراغی توی تاریکی. با هر قدم، مسیر واضح‌تر می‌شه. اینجا جاییه که رویاها به واقعیت نزدیک می‌شن. با انرژی، تعهد، و خلاقیت، قراره چیزی بسازیم که تأثیر بذاره.",
        "محصول جدیدمون با عشق ساخته شده. هر جزئیش با دقت طراحی شده تا تجربه‌ای خاص براتون بسازه. آماده‌اید برای یه چیز متفاوت؟ این محصول فقط یه ابزار نیست، یه حس جدیده که قراره روزتون رو بهتر کنه.",
        "ما فقط یه محصول نساختیم، یه حس جدید خلق کردیم. چیزی که قراره توی روزمرگی‌تون بدرخشه و حالتون رو بهتر کنه. طراحی خاص، کاربردی بودن، و انرژی مثبتش رو از دست ندید. این محصول برای شماست.",
        "محصول جدید یعنی یه فرصت تازه برای ارتباط با شما. طراحی خاص، کاربردی بودن، و انرژی مثبتش رو از دست ندید. هر جزئیش با فکر ساخته شده تا تجربه‌ای متفاوت بسازه. امتحانش کن، عاشقش می‌شی."
    ]
}
df = pd.DataFrame(data)

# انتخاب موضوع و لحن
topic = st.selectbox("📝 موضوع پست:", df['topic'].unique())
tone = st.selectbox("🎭 لحن کپشن:", df['tone'].unique())

# انتخاب منطقه
region = st.selectbox("📍 منطقه مورد نظر برای پیشنهاد ترند:", ["ایران", "ترکیه", "امارات", "آلمان", "آمریکا"])

# تابع پیشنهاد کپشن‌های طولانی
def get_captions(topic, tone):
    results = df[(df['topic'] == topic) & (df['tone'] == tone)]
    return results['caption'].tolist() if not results.empty else ["کپشن مناسب پیدا نشد."]

# تابع پیشنهاد هشتگ
def suggest_hashtags(topic):
    hashtags_dict = {
        "شروع پروژه": ["#شروع", "#انگیزه", "#پروژه", "#توسعه", "#هدف"],
        "محصول جدید": ["#محصول", "#جدید", "#معرفی", "#برند", "#خرید"]
    }
    return " ".join(hashtags_dict.get(topic, ["#ایده", "#کپشن", "#اینستاگرام"]))

# پیشنهاد آهنگ ترند + لینک واقعی
def trending_music(region):
    music_dict = {
        "ایران": [("زاکربرگ - صائب", "https://www.google.com/search?q=دانلود+آهنگ+زاکربرگ+صائب")],
        "ترکیه": [("Simge - Aşkın Olayım", "https://bibis.ir/simge-askin-olayim/")],
        "آمریکا": [("Doja Cat - Paint The Town Red", "https://bibis.ir/doja-cat-paint-the-town-red/")],
        "امارات": [("Balti - Ya Lili", "https://musicdel.ir/single-tracks/75313/")],
        "آلمان": [("Apache 207 - Roller", "https://www.youtube.com/watch?v=Fo3DAhiNKQo")]
    }
    return music_dict.get(region, [("آهنگ ترند یافت نشد", "#")])

# دکمه تولید کپشن
if st.button("✨ تولید کپشن"):
    captions = get_captions(topic, tone)
    hashtags = suggest_hashtags(topic)
    music, link = random.choice(trending_music(region))

    st.markdown("### 📋 کپشن‌های پیشنهادی:")
    for i, cap in enumerate(captions):
        final = f"{cap}\n🎶 آهنگ پیشنهادی: {music}\n{hashtags}"
        st.text_area(f"گزینه {i+1}:", final, height=180)

        st.markdown(f"""
        <a href="{link}" target="_blank">
            <button style="background-color:#2ecc71;color:white;padding:8px;border:none;border-radius:5px;cursor:pointer;">
                🎵 دانلود آهنگ پیشنهادی
            </button>
        </a>
        """, unsafe_allow_html=True)

# تحلیل عمومی بر اساس اسم پیج
st.markdown("---")
st.subheader("🔍 تحلیل عمومی بر اساس اسم پیج")

col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### @")
with col2:
    page_name = st.text_input("نام پیج اینستاگرام را وارد کنید:")

if page_name:
    if st.button("✅ اینتر"):
        full_name = f"@{page_name}"
        st.success(f"در حال بررسی پیج {full_name} ...")

        def analyze_page(name):
            tips = [
                f"📌 بررسی پیج: {name}",
                "✅ از ریلزهای کوتاه با آهنگ‌های وایرال استفاده کن",
                "🎯 کپشن‌هات رو با CTA واضح بنویس (مثلاً 'نظر بده' یا 'سیو کن')",
                "📅 زمان پست‌گذاری رو با رفتار مخاطب هماهنگ کن",
                "📈 از هشتگ‌های ترند و محلی استفاده کن",
                "🧠 از پشت‌صحنه‌ی پروژه‌هات محتوا بساز تا اعتماد ایجاد بشه",
                "🎨 از طراحی‌های شخصی و برندت در قالب استوری و هایلایت استفاده کن"
            ]
            return tips

        tips = analyze_page(full_name)
        st.markdown("### 📈 راهکارهای پیشنهادی برای رشد پیج:")
        for tip in tips:
            st.markdown(f"- {tip}")
