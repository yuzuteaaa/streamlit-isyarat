import schedule
import time
from scraper.article_scraper import scrape_and_store_articles

def run_scheduler():
    # Jadwalkan scraping setiap hari pukul 08:00
    schedule.every().day.at("15:22").do(scrape_and_store_articles)

    print("📅 Scheduler aktif. Menunggu waktu eksekusi...")

    while True:
        schedule.run_pending()
        time.sleep(60)
