import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime
from db_utils import get_db

def ogrenci_ara(arama_kriteri, arama_metni, sinif_filtre=None, ders_saati_filtre=None):
    conn = get_db()
    c = conn.cursor()
    
    query = '''SELECT o.id, o.ad, o.soyad, o.tc_no, o.ders_saati, s.ad as sinif_adi, 
               o.veli_adi, o.veli_telefon, o.ozel_durum
               FROM ogrenciler o 
               LEFT JOIN siniflar s ON o.sinif_id = s.id WHERE 1=1'''
    
    params = []
    
    if arama_metni:
        if arama_kriteri == 'ad_soyad':
            query += ' AND (o.ad LIKE ? OR o.soyad LIKE ?)'
            params.extend([f'%{arama_metni}%', f'%{arama_metni}%'])
        elif arama_kriteri == 'tc_no':
            query += ' AND o.tc_no LIKE ?'
            params.append(f'%{arama_metni}%')
    
    if sinif_filtre:
        query += ' AND o.sinif_id = ?'
        params.append(sinif_filtre)
    
    if ders_saati_filtre:
        query += ' AND o.ders_saati = ?'
        params.append(ders_saati_filtre)
    
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows

def ogrenci_transfer(ogrenci_id, yeni_sinif_id, yeni_ders_saati, transfer_notu):
    conn = get_db()
    c = conn.cursor()
    
    try:
        # Mevcut bilgileri al
        c.execute('SELECT sinif_id, ders_saati FROM ogrenciler WHERE id=?', (ogrenci_id,))
        eski_bilgiler = c.fetchone()
        
        if eski_bilgiler:
            eski_sinif_id, eski_ders_saati = eski_bilgiler
            
            # Transfer geçmişine kaydet
            tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c.execute('''INSERT INTO transfer_gecmisi 
                        (ogrenci_id, eski_sinif_id, yeni_sinif_id, eski_ders_saati, yeni_ders_saati, tarih, aciklama)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                     (ogrenci_id, eski_sinif_id, yeni_sinif_id, eski_ders_saati, yeni_ders_saati, tarih, transfer_notu))
            
            # Öğrenci bilgilerini güncelle
            c.execute('UPDATE ogrenciler SET sinif_id=?, ders_saati=? WHERE id=?',
                     (yeni_sinif_id, yeni_ders_saati, ogrenci_id))
            
            conn.commit()
            return True
    except Exception:
        conn.rollback()
        return False
    finally:
        conn.close()

def csv_export(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Ad', 'Soyad', 'TC No', 'Ders Saati', 'Sınıf', 'Veli Adı', 'Veli Telefon', 'Özel Durum'])
            writer.writerows(data)
        return True
    except Exception:
        return False

def transfer_gecmisini_getir():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT tg.id, o.ad || ' ' || o.soyad as ogrenci, 
                 es.ad as eski_sinif, ys.ad as yeni_sinif,
                 tg.eski_ders_saati, tg.yeni_ders_saati, tg.tarih, tg.aciklama
                 FROM transfer_gecmisi tg
                 JOIN ogrenciler o ON tg.ogrenci_id = o.id
                 LEFT JOIN siniflar es ON tg.eski_sinif_id = es.id
                 LEFT JOIN siniflar ys ON tg.yeni_sinif_id = ys.id
                 ORDER BY tg.tarih DESC''')
    rows = c.fetchall()
    conn.close()
    return rows
