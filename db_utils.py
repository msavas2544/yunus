import sqlite3
import os
import sys

# Masaüstü uygulaması için veritabanı yolu ayarları
if hasattr(sys, '_MEIPASS'):
    # PyInstaller ile paketlenmiş durumda
    user_data_dir = os.path.join(os.path.expanduser('~'), 'OkulYonetimSistemi')
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)
    DB_PATH = os.path.join(user_data_dir, 'okul_yonetim.db')
else:
    # Normal Python çalıştırma durumunda
    DB_PATH = os.path.join(os.path.dirname(__file__), 'okul_yonetim.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    
    # Sınıflar tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS siniflar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        kapasite INTEGER,
        aciklama TEXT
    )''')
    
    # Öğrenciler tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS ogrenciler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        tc_no TEXT UNIQUE,
        dogum_tarihi TEXT,
        ders_saati INTEGER CHECK(ders_saati IN (2, 3, 4, 6)),
        sinif_id INTEGER,
        veli_adi TEXT,
        veli_telefon TEXT,
        ozel_durum TEXT,
        FOREIGN KEY (sinif_id) REFERENCES siniflar (id)
    )''')
    
    # Öğretmenler tablosu
    c.execute('''CREATE TABLE IF NOT EXISTS ogretmenler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        soyad TEXT NOT NULL,
        brans TEXT,
        telefon TEXT,
        email TEXT
    )''')
    
    # Sınıf-öğretmen eşleştirmesi
    c.execute('''CREATE TABLE IF NOT EXISTS sinif_ogretmen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sinif_id INTEGER,
        ogretmen_id INTEGER,
        FOREIGN KEY (sinif_id) REFERENCES siniflar (id),
        FOREIGN KEY (ogretmen_id) REFERENCES ogretmenler (id)
    )''')
    
    # Transfer geçmişi
    c.execute('''CREATE TABLE IF NOT EXISTS transfer_gecmisi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ogrenci_id INTEGER,
        eski_sinif_id INTEGER,
        yeni_sinif_id INTEGER,
        eski_ders_saati INTEGER,
        yeni_ders_saati INTEGER,
        tarih TEXT,
        aciklama TEXT,
        FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler (id),
        FOREIGN KEY (eski_sinif_id) REFERENCES siniflar (id),
        FOREIGN KEY (yeni_sinif_id) REFERENCES siniflar (id)
    )''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
