import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config.db import get_db

def scrape_and_store_articles():
    print("⏳ Scraping dimulai...")
    url = "https://news.google.com/search?q=bahasa%20isyarat&hl=id&gl=ID&ceid=ID:id"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Gagal mengakses halaman.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select("article")

    results = []
    for article in articles[:100]:  # Ambil maksimal 10
        title = article.text.strip()
        link_tag = article.find("a")
        if link_tag:
            full_link = "https://news.google.com" + link_tag["href"][1:]
            results.append({
                "title": title,
                "link": full_link,
                "scraped_at": datetime.now()
            })

    # Simpan ke MongoDB
    db = get_db()
    collection = db["articles"]
    if results:
        collection.insert_many(results)
        print(f"✅ {len(results)} artikel berhasil disimpan ke MongoDB.")
    else:
        print("⚠️ Tidak ada artikel yang ditemukan.")
