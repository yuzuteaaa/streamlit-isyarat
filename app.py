import streamlit as st
from pymongo import MongoClient
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime

#config mongo
def get_data():
    client = MongoClient("mongodb+srv://baisyufan:nzPoNISBiZxLIKbn@bais.5y9mhli.mongodb.net/")
    db = client["backend-capstone"]
    collection = db["articles"]
    data = list(collection.find())
    return pd.DataFrame(data)

st.title("📊 Analisis Artikel Bahasa Isyarat")
df = get_data()

if df.empty:
    st.warning("Belum ada data artikel.")
else:
    df['scraped_at'] = pd.to_datetime(df['scraped_at'])
    df['date'] = df['scraped_at'].dt.date

    
    st.subheader("📑 Daftar Artikel")
    st.dataframe(df[['title', 'link', 'scraped_at']])

    st.subheader("📆 Frekuensi Artikel per Hari")
    daily_count = df.groupby('date').size()
    st.bar_chart(daily_count)

    st.subheader("☁️ WordCloud Judul Artikel")
    all_titles = " ".join(df['title'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


    st.subheader("🔍 Kata Kunci Paling Sering Muncul")
    from collections import Counter
    import re

    words = re.findall(r'\w+', all_titles.lower())
    common_words = Counter(words).most_common(10)
    common_df = pd.DataFrame(common_words, columns=['Kata', 'Frekuensi'])
    st.bar_chart(common_df.set_index('Kata'))
    