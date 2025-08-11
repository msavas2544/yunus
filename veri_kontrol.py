import sqlite3
import os

# Veritabanı dosyasını kontrol et
db_path = os.path.join(os.path.dirname(__file__), 'okul_yonetim.db')

if os.path.exists(db_path):
    print(f"✅ Veritabanı dosyası mevcut: {db_path}")
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    try:
        # Sınıf sayısını kontrol et
        c.execute('SELECT COUNT(*) FROM siniflar')
        sinif_sayisi = c.fetchone()[0]
        print(f"📚 Toplam sınıf sayısı: {sinif_sayisi}")
        
        # Öğrenci sayısını kontrol et
        c.execute('SELECT COUNT(*) FROM ogrenciler')
        ogrenci_sayisi = c.fetchone()[0]
        print(f"👨‍🎓 Toplam öğrenci sayısı: {ogrenci_sayisi}")
        
        # Öğretmen sayısını kontrol et
        c.execute('SELECT COUNT(*) FROM ogretmenler')
        ogretmen_sayisi = c.fetchone()[0]
        print(f"👩‍🏫 Toplam öğretmen sayısı: {ogretmen_sayisi}")
        
        # Transfer sayısını kontrol et
        c.execute('SELECT COUNT(*) FROM transfer_gecmisi')
        transfer_sayisi = c.fetchone()[0]
        print(f"🔄 Toplam transfer sayısı: {transfer_sayisi}")
        
        # Örnek birkaç öğrenci adını göster
        c.execute('SELECT ad, soyad FROM ogrenciler LIMIT 5')
        ogrenciler = c.fetchall()
        print(f"\n📝 Örnek öğrenciler:")
        for ad, soyad in ogrenciler:
            print(f"   - {ad} {soyad}")
        
        # Örnek birkaç sınıf adını göster
        c.execute('SELECT ad, kapasite FROM siniflar LIMIT 5')
        siniflar = c.fetchall()
        print(f"\n🏫 Örnek sınıflar:")
        for ad, kapasite in siniflar:
            print(f"   - {ad} (Kapasite: {kapasite})")
            
        print(f"\n🎉 Tüm veriler kalıcı olarak saklanıyor!")
        print(f"💾 Veritabanı dosya boyutu: {os.path.getsize(db_path)} byte")
        
    except Exception as e:
        print(f"❌ Veritabanı okuma hatası: {e}")
    finally:
        conn.close()
else:
    print(f"❌ Veritabanı dosyası bulunamadı: {db_path}")
