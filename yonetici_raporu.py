import tkinter as tk
from tkinter import messagebox, ttk
import csv
from db_utils import get_db

def genel_istatistikler():
    conn = get_db()
    c = conn.cursor()
    
    # Toplam öğrenci sayısı
    c.execute('SELECT COUNT(*) FROM ogrenciler')
    toplam_ogrenci = c.fetchone()[0]
    
    # Toplam öğretmen sayısı
    c.execute('SELECT COUNT(*) FROM ogretmenler')
    toplam_ogretmen = c.fetchone()[0]
    
    # Toplam sınıf sayısı
    c.execute('SELECT COUNT(*) FROM siniflar')
    toplam_sinif = c.fetchone()[0]
    
    # Ders saatine göre dağılım
    c.execute('SELECT ders_saati, COUNT(*) FROM ogrenciler GROUP BY ders_saati')
    ders_saati_dagilim = c.fetchall()
    
    conn.close()
    
    return {
        'toplam_ogrenci': toplam_ogrenci,
        'toplam_ogretmen': toplam_ogretmen,
        'toplam_sinif': toplam_sinif,
        'ders_saati_dagilim': ders_saati_dagilim
    }

def sinif_doluluk_raporu():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT s.ad, s.kapasite, COUNT(o.id) as mevcut_ogrenci,
                 ROUND((COUNT(o.id) * 100.0 / s.kapasite), 2) as doluluk_orani
                 FROM siniflar s
                 LEFT JOIN ogrenciler o ON s.id = o.sinif_id
                 GROUP BY s.id, s.ad, s.kapasite''')
    rows = c.fetchall()
    conn.close()
    return rows

def ogretmen_atama_raporu():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT o.ad || ' ' || o.soyad as ogretmen, o.brans,
                 GROUP_CONCAT(s.ad) as atanan_siniflar
                 FROM ogretmenler o
                 LEFT JOIN sinif_ogretmen so ON o.id = so.ogretmen_id
                 LEFT JOIN siniflar s ON so.sinif_id = s.id
                 GROUP BY o.id, o.ad, o.soyad, o.brans''')
    rows = c.fetchall()
    conn.close()
    return rows

def transfer_raporu():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT o.ad || ' ' || o.soyad as ogrenci,
                 es.ad as eski_sinif, ys.ad as yeni_sinif,
                 tg.eski_ders_saati, tg.yeni_ders_saati, tg.tarih
                 FROM transfer_gecmisi tg
                 JOIN ogrenciler o ON tg.ogrenci_id = o.id
                 LEFT JOIN siniflar es ON tg.eski_sinif_id = es.id
                 LEFT JOIN siniflar ys ON tg.yeni_sinif_id = ys.id
                 ORDER BY tg.tarih DESC''')
    rows = c.fetchall()
    conn.close()
    return rows

def csv_rapor_export(data, headers, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
        return True
    except Exception:
        return False
