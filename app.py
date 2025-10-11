import streamlit as st
import pandas as pd

# دیتاست ساده
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

# فرم ورودی
st.title("🎨 کپشن‌ساز اینستاگرام")
topic = st.selectbox("موضوع پست:", df['topic'].unique())
tone = st.selectbox("لحن کپشن:", df['tone'].unique())

# تابع‌ها
def get_caption(topic, tone):
    result = df[(df['topic'] == topic) & (df['tone'] == tone)]
    if not result.empty:
        return result.iloc[0]['caption']
    else:
        return "کپشن مناسب پیدا نشد."

def suggest_hashtags(topic):
    hashtags_dict = {
        "شروع پروژه": ["#شروع", "#انگیزه", "#پروژه", "#توسعه", "#هدف"],
        "محصول جدید": ["#محصول", "#جدید", "#معرفی", "#برند", "#خرید"],
        "پشت‌صحنه": ["#پشت_صحنه", "#تیم", "#کار", "#خنده", "#تلاش"],
        "نقل‌قول انگیزشی": ["#انگیزشی", "#موفقیت", "#الهام", "#رویا", "#پیشرفت"]
    }
    return " ".join(hashtags_dict.get(topic, ["#ایده", "#کپشن", "#اینستاگرام"]))

# تولید خروجی
if st.button("تولید کپشن"):
    caption = get_caption(topic, tone)
    hashtags = suggest_hashtags(topic)
    final = caption + "\n" + hashtags
    st.text_area("کپشن نهایی:", final, height=100)

    # دکمه کپی در کلیپ‌بورد
    st.code(final, language='markdown')

    # ذخیره به فایل
    with open("caption.txt", "w", encoding="utf-8") as f:
        f.write(final)
    st.download_button("📥 دانلود فایل TXT", data=final, file_name="caption.txt")

    # برای PDF یا Word نیاز به کتابخانه‌های اضافی هست (در ادامه توضیح می‌دم)
