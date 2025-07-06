import os
import sys

def run_scraper():
    # src/scraper.py'yi çalıştır
    scraper_path = os.path.join("src", "scraper.py")
    if os.path.exists(scraper_path):
        os.system(f"python {scraper_path}")
    else:
        print("Hata: scraper.py bulunamadı!")

if __name__ == "__main__":
    run_scraper()
    
