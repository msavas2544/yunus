import tkinter as tk
from tkinter import messagebox, ttk
from db_utils import get_db

def ogrenci_ekle(ad, soyad, tc_no, dogum_tarihi, ders_saati, sinif_id, veli_adi, veli_telefon, ozel_durum):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO ogrenciler 
                    (ad, soyad, tc_no, dogum_tarihi, ders_saati, sinif_id, veli_adi, veli_telefon, ozel_durum) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                 (ad, soyad, tc_no, dogum_tarihi, ders_saati, sinif_id, veli_adi, veli_telefon, ozel_durum))
        conn.commit()
        return True
    except Exception as e:
        return False
    finally:
        conn.close()

def ogrencileri_listele():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT o.id, o.ad, o.soyad, o.tc_no, o.ders_saati, s.ad as sinif_adi, o.veli_adi 
                 FROM ogrenciler o 
                 LEFT JOIN siniflar s ON o.sinif_id = s.id''')
    rows = c.fetchall()
    conn.close()
    return rows

def ogrenci_sil(ogrenci_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM ogrenciler WHERE id=?', (ogrenci_id,))
    conn.commit()
    conn.close()

def siniflari_getir():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, ad FROM siniflar')
    rows = c.fetchall()
    conn.close()
    return rows
