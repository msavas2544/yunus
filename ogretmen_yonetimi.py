import tkinter as tk
from tkinter import messagebox, ttk
from db_utils import get_db

def ogretmen_ekle(ad, soyad, brans, telefon, email):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO ogretmenler (ad, soyad, brans, telefon, email) 
                    VALUES (?, ?, ?, ?, ?)''', (ad, soyad, brans, telefon, email))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def ogretmenleri_listele():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT id, ad, soyad, brans, telefon, email FROM ogretmenler')
    rows = c.fetchall()
    conn.close()
    return rows

def ogretmen_sil(ogretmen_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM ogretmenler WHERE id=?', (ogretmen_id,))
    conn.commit()
    conn.close()

def sinif_ogretmen_ata(sinif_id, ogretmen_id):
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO sinif_ogretmen (sinif_id, ogretmen_id) VALUES (?, ?)', 
                 (sinif_id, ogretmen_id))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def sinif_ogretmen_listele():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT so.id, s.ad as sinif_adi, o.ad as ogretmen_adi, o.soyad 
                 FROM sinif_ogretmen so 
                 JOIN siniflar s ON so.sinif_id = s.id 
                 JOIN ogretmenler o ON so.ogretmen_id = o.id''')
    rows = c.fetchall()
    conn.close()
    return rows
