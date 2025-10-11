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

import streamlit as st
import random

st.set_page_config(page_title="تحلیل هوشمند پیج اینستاگرام", page_icon="📊")
st.title("📊 تحلیل هوشمند پیج اینستاگرام")

# ورودی اسم پیج
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### @")
with col2:
    page_name = st.text_input("نام پیج اینستاگرام را وارد کنید:")

# دکمه سبز اینتر
if page_name:
    if st.button("✅ اینتر"):
        full_name = f"@{page_name}"
        st.success(f"در حال بررسی پیج {full_name} ...")

        # تحلیل فرضی بر اساس سرچ عمومی
        def auto_analysis(name):
            # داده‌های فرضی برای نمایش
            followers = random.randint(500, 5000)
            posts = random.randint(20, 150)
            bio = "طراح خلاق | آموزش رایگان | لینک دوره در بیو"
            link = "https://mohadeseh.design"

            # ایرادها
            issues = []
            if followers < 1000:
                issues.append("📉 تعداد فالوور پایین‌تر از حد استاندارد برای رشد ارگانیک")
            if posts < 30:
                issues.append("📦 تعداد پست کم؛ نیاز به تولید محتوای منظم‌تر")
            if "لینک" not in bio.lower():
                issues.append("🔗 بیو بدون لینک مستقیم به محصول یا دوره")
            if not link.startswith("https://"):
                issues.append("⚠️ لینک بیو ناقص یا غیرفعال")

            # نوع محتوا فرضی
            content_type = random.choice(["آموزشی", "شخصی", "برندینگ", "هنری"])
            engagement = random.uniform(2.5, 6.5)

            # راهکارها
            tips = []
            tips.append(f"📌 نوع محتوا: {content_type}")
            if engagement < 4:
                tips.append("🔁 تعامل پایین؛ از CTA واضح مثل 'نظر بده' یا 'سیو کن' استفاده کن")
            tips.append("🎵 از آهنگ‌های وایرال در ریلز استفاده کن")
            tips.append("📅 زمان پست‌گذاری رو با رفتار مخاطب هماهنگ کن")
            tips.append("🎯 از هشتگ‌های ترند و محلی استفاده کن")
            tips.append("🧠 از پشت‌صحنه‌ی پروژه‌هات محتوا بساز تا اعتماد ایجاد بشه")
            tips.append("🎨 از طراحی‌های شخصی و برندت در قالب استوری و هایلایت استفاده کن")

            return followers, posts, bio, link, issues, tips

        followers, posts, bio, link, issues, tips = auto_analysis(full_name)

        st.markdown("### 📊 اطلاعات عمومی پیج:")
        st.write("👥 تعداد فالوور:", followers)
        st.write("📦 تعداد پست:", posts)
        st.write("📝 بیو:", bio)
        st.write("🔗 لینک بیو:", link)

        st.markdown("### ⚠️ ایرادهای احتمالی:")
        for issue in issues:
            st.markdown(f"- {issue}")

        st.markdown("### ✅ راهکارهای پیشنهادی برای رشد پیج:")
        for tip in tips:
            st.markdown(f"- {tip}")
