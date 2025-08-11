from db_utils import get_db
from datetime import datetime

def ornek_transfer_yap():
    """Örnek transfer işlemi yapar"""
    conn = get_db()
    c = conn.cursor()
    
    try:
        # Ahmet Yıldırım'ı (id=1) 1-A'dan 2-A'ya transfer edelim
        # Ders saatini 4'ten 6'ya çıkaralım
        
        # Önce mevcut bilgileri alalım
        c.execute('SELECT ad, soyad, sinif_id, ders_saati FROM ogrenciler WHERE id=1')
        ogrenci = c.fetchone()
        
        if ogrenci:
            ad, soyad, eski_sinif_id, eski_ders_saati = ogrenci
            yeni_sinif_id = 3  # 2-A Sınıfı
            yeni_ders_saati = 6
            
            # Transfer geçmişine kaydet
            tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c.execute('''INSERT INTO transfer_gecmisi 
                        (ogrenci_id, eski_sinif_id, yeni_sinif_id, eski_ders_saati, yeni_ders_saati, tarih, aciklama)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                     (1, eski_sinif_id, yeni_sinif_id, eski_ders_saati, yeni_ders_saati, tarih, 
                      'Matematik alanında ilerleme gösterdiği için 2-A sınıfına transfer edildi.'))
            
            # Öğrenci bilgilerini güncelle
            c.execute('UPDATE ogrenciler SET sinif_id=?, ders_saati=? WHERE id=1',
                     (yeni_sinif_id, yeni_ders_saati))
            
            conn.commit()
            print(f"✅ {ad} {soyad} başarıyla transfer edildi!")
            print(f"📝 Eski: Sınıf {eski_sinif_id}, {eski_ders_saati} saat")
            print(f"📝 Yeni: Sınıf {yeni_sinif_id}, {yeni_ders_saati} saat")
            
        # Bir tane daha transfer yapalım - Murat Özdemir'i destek sınıfına alalım
        c.execute('SELECT ad, soyad, sinif_id, ders_saati FROM ogrenciler WHERE id=3')
        ogrenci2 = c.fetchone()
        
        if ogrenci2:
            ad2, soyad2, eski_sinif_id2, eski_ders_saati2 = ogrenci2
            yeni_sinif_id2 = 7  # Destek Sınıfı
            yeni_ders_saati2 = 2
            
            # Transfer geçmişine kaydet
            tarih2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            c.execute('''INSERT INTO transfer_gecmisi 
                        (ogrenci_id, eski_sinif_id, yeni_sinif_id, eski_ders_saati, yeni_ders_saati, tarih, aciklama)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                     (3, eski_sinif_id2, yeni_sinif_id2, eski_ders_saati2, yeni_ders_saati2, tarih2, 
                      'Özel ihtiyaçları nedeniyle bireysel destek için transfer edildi.'))
            
            # Öğrenci bilgilerini güncelle
            c.execute('UPDATE ogrenciler SET sinif_id=?, ders_saati=? WHERE id=3',
                     (yeni_sinif_id2, yeni_ders_saati2))
            
            conn.commit()
            print(f"✅ {ad2} {soyad2} başarıyla transfer edildi!")
            print(f"📝 Eski: Sınıf {eski_sinif_id2}, {eski_ders_saati2} saat")
            print(f"📝 Yeni: Sınıf {yeni_sinif_id2}, {yeni_ders_saati2} saat")
            
    except Exception as e:
        print(f"❌ Transfer hatası: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    ornek_transfer_yap()
