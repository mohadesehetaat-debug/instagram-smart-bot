import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="کپشن‌ساز هوشمند اینستاگرام", page_icon="🎨")

# عنوان اصلی
st.title("🎨 کپشن‌ساز هوشمند اینستاگرام")

# دیتاست ساده کپشن‌ها
data = {
    "topic": ["شروع پروژه", "محصول جدید", "پشت‌صحنه", "نقل‌قول انگیزشی"],
    "tone": ["انگیزشی", "تبلیغاتی", "دوستانه", "شاعرانه"],
    "caption": [
        "هر شروعی یک فرصت تازه‌ست.",
        "محصول جدیدمون رسید! منتظر نظرتون هستیم.",
        "پشت‌صحنه‌ی تلاش‌های ما همیشه پر از عشق و خنده‌ست.",
        "در دل تاریکی، نور رویاها می‌درخشه."
    ]
}
df = pd.DataFrame(data)

# انتخاب موضوع و لحن
topic = st.selectbox("📝 موضوع پست:", df['topic'].unique())
tone = st.selectbox("🎭 لحن کپشن:", df['tone'].unique())

# انتخاب منطقه
region = st.selectbox(
    "📍 منطقه مورد نظر برای پیشنهاد ترند:",
    ["ایران", "ترکیه", "امارات", "آلمان", "آمریکا"]
)

# تابع تولید کپشن
def get_caption(topic, tone):
    result = df[(df['topic'] == topic) & (df['tone'] == tone)]
    if not result.empty:
        return result.iloc[0]['caption']
    else:
        return "کپشن مناسب پیدا نشد."

# تابع پیشنهاد هشتگ
def suggest_hashtags(topic):
    hashtags_dict = {
        "شروع پروژه": ["#شروع", "#انگیزه", "#پروژه", "#توسعه", "#هدف"],
        "محصول جدید": ["#محصول", "#جدید", "#معرفی", "#برند", "#خرید"],
        "پشت‌صحنه": ["#پشت_صحنه", "#تیم", "#کار", "#خنده", "#تلاش"],
        "نقل‌قول انگیزشی": ["#انگیزشی", "#موفقیت", "#الهام", "#رویا", "#پیشرفت"]
    }
    return " ".join(hashtags_dict.get(topic, ["#ایده", "#کپشن", "#اینستاگرام"]))

# پیشنهاد آهنگ ترند
def trending_music(region):
    music_dict = {
        "ایران": ["زاکربرگ - صائب", "به دادم برس - رخشنده", "تموم شاعرا - عرفان"],
        "ترکیه": ["Simge - Aşkın Olayım", "Tarkan - Yolla"],
        "آمریکا": ["Taylor Swift - Cruel Summer", "Doja Cat - Paint The Town Red"],
        "امارات": ["Balti - Ya Lili", "Hussain Al Jassmi - Boshret Kheir"],
        "آلمان": ["Apache 207 - Roller", "Rammstein - Deutschland"]
    }
    return music_dict.get(region, ["آهنگ ترند یافت نشد"])

# دکمه تولید کپشن
if st.button("✨ تولید کپشن"):
    caption = get_caption(topic, tone)
    hashtags = suggest_hashtags(topic)
    music = random.choice(trending_music(region))
    final = f"{caption}\n🎶 آهنگ پیشنهادی: {music}\n{hashtags}"

    st.text_area("📋 کپشن نهایی:", final, height=120)

    st.markdown(f"""
    <button onclick="navigator.clipboard.writeText({final})" style="background-color:#4CAF50;color:white;padding:10px;border:none;border-radius:5px;cursor:pointer;">
        📎 کپی در کلیپ‌بورد
    </button>
    """, unsafe_allow_html=True)

# آپلود فایل گزارش پیج
uploaded_file = st.file_uploader("📊 آپلود گزارش پیج (CSV یا JSON)", type=["csv", "json"])
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df_report = pd.read_csv(uploaded_file)
        else:
            df_report = pd.read_json(uploaded_file)

        st.success("✅ فایل با موفقیت بارگذاری شد.")
        st.write("میانگین ریچ:", round(df_report["reach"].mean(), 2))
        st.write("میانگین تعامل:", round(df_report["engagement"].mean(), 2))

        def growth_tips(reach, engagement):
            tips = []
            if engagement < 5:
                tips.append("🔁 از CTA واضح مثل 'نظر بده' یا 'سیو کن' استفاده کن")
            if reach < 1000:
                tips.append("🎯 از هشتگ‌های محلی و ترند استفاده کن")
            tips.append("🎵 از آهنگ‌های وایرال در ریلز استفاده کن")
            tips.append("📅 زمان پست‌گذاری رو با رفتار مخاطب هماهنگ کن")
            return tips

        tips = growth_tips(df_report["reach"].mean(), df_report["engagement"].mean())
        st.markdown("### 📈 راهکارهای پیشنهادی برای رشد پیج:")
        for tip in tips:
            st.markdown(f"- {tip}")

    except Exception as e:
        st.error("❌ خطا در خواندن فایل: لطفاً مطمئن شو فایل ساختار درستی داره.")

# ورودی نوشتاری برای تحلیل دستی
st.markdown("---")
st.subheader("✍️ وارد کردن داده‌ی گزارش به‌صورت نوشتاری")

raw_text = st.text_area("لطفاً داده‌ها را به‌صورت زیر وارد کنید:\nreach: عدد\nengagement: عدد")

if raw_text:
    try:
        lines = raw_text.split("\n")
        reach = float([l for l in lines if "reach" in l][0].split(":")[1].strip())
        engagement = float([l for l in lines if "engagement" in l][0].split(":")[1].strip())

        st.success("✅ داده‌ها با موفقیت خوانده شدند.")
        st.write("ریچ:", reach)
        st.write("تعامل:", engagement)

        tips = growth_tips(reach, engagement)
        st.markdown("### 📈 راهکارهای پیشنهادی برای رشد پیج:")
        for tip in tips:
            st.markdown(f"- {tip}")

    except:
        st.error("❌ فرمت داده‌ها درست نیست. لطفاً مثل نمونه وارد کن.")

# تحلیل عمومی بر اساس اسم پیج
st.markdown("---")
st.subheader("🔍 تحلیل عمومی بر اساس اسم پیج")

page_name = st.text_input("اسم پیج اینستاگرام (بدون @):")

if page_name:
    st.info(f"در حال بررسی پیج {page_name} ...")

    def analyze_page(name):
        tips = []
        tips.append(f"📌 بررسی پیج: {name}")
        tips.append("✅ از ریلزهای کوتاه با آهنگ‌های وایرال استفاده کن")
        tips.append("🎯 کپشن‌هات رو با CTA واضح بنویس (مثلاً 'نظر بده' یا 'سیو کن')")
        tips.append("📅 زمان پست‌گذاری رو با رفتار مخاطب هماهنگ کن")
        tips.append("📈 از هشتگ‌های ترند و محلی استفاده کن")
        return tips

    tips = analyze_page(page_name)
    st.markdown("### 📈 راهکارهای پیشنهادی برای رشد پیج:")
    for tip in tips:
        st.markdown(f"- {tip}")
