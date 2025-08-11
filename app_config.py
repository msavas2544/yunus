# -*- coding: utf-8 -*-
"""
Özel Eğitim Okulu Yönetim Sistemi
Masaüstü Uygulaması Ayarları
"""

# Bu dosya PyInstaller için özel ayarları içerir
import sys
import os

# Kaynak dosyaların yolunu ekle
if hasattr(sys, '_MEIPASS'):
    # PyInstaller ile paketlenmiş durumda
    base_path = sys._MEIPASS
else:
    # Normal Python çalıştırma durumunda
    base_path = os.path.dirname(os.path.abspath(__file__))

# Veritabanı dosyasının yolunu ayarla
DB_PATH = os.path.join(base_path, 'okul_yonetim.db')

# Eğer paketlenmiş uygulamada veritabanı dosyası yoksa, kullanıcı dizininde oluştur
if hasattr(sys, '_MEIPASS') and not os.path.exists(DB_PATH):
    import tempfile
    user_data_dir = os.path.join(os.path.expanduser('~'), 'OkulYonetimSistemi')
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)
    DB_PATH = os.path.join(user_data_dir, 'okul_yonetim.db')
