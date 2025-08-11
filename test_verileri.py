import sqlite3
import os
from db_utils import get_db, init_db

def test_verileri_ekle():
    """Test için örnek veriler ekler"""
    
    # Önce veritabanını başlat
    init_db()
    
    conn = get_db()
    c = conn.cursor()
    
    try:
        # Örnek sınıflar ekle
        siniflar = [
            ('1-A Sınıfı', 15, 'Matematik ağırlıklı sınıf'),
            ('1-B Sınıfı', 12, 'Türkçe ağırlıklı sınıf'),
            ('2-A Sınıfı', 18, 'Fen bilimleri ağırlıklı'),
            ('2-B Sınıfı', 14, 'Sosyal bilimler ağırlıklı'),
            ('3-A Sınıfı', 16, 'Sanat ağırlıklı sınıf'),
            ('Hazırlık Sınıfı', 10, 'Okula uyum sınıfı'),
            ('Destek Sınıfı', 8, 'Bireysel destek sınıfı')
        ]
        
        for sinif in siniflar:
            c.execute('INSERT OR IGNORE INTO siniflar (ad, kapasite, aciklama) VALUES (?, ?, ?)', sinif)
        
        # Örnek öğretmenler ekle
        ogretmenler = [
            ('Ayşe', 'Yılmaz', 'Matematik', '0532-111-1111', 'ayse.yilmaz@okul.edu'),
            ('Mehmet', 'Demir', 'Türkçe', '0533-222-2222', 'mehmet.demir@okul.edu'),
            ('Fatma', 'Kaya', 'Fen Bilimleri', '0534-333-3333', 'fatma.kaya@okul.edu'),
            ('Ali', 'Özkan', 'Sosyal Bilgiler', '0535-444-4444', 'ali.ozkan@okul.edu'),
            ('Zeynep', 'Çelik', 'Resim', '0536-555-5555', 'zeynep.celik@okul.edu'),
            ('Hasan', 'Acar', 'Müzik', '0537-666-6666', 'hasan.acar@okul.edu'),
            ('Elif', 'Şahin', 'Özel Eğitim', '0538-777-7777', 'elif.sahin@okul.edu'),
            ('Burak', 'Yıldız', 'Beden Eğitimi', '0539-888-8888', 'burak.yildiz@okul.edu'),
            ('Seda', 'Arslan', 'Psikoloji', '0530-999-9999', 'seda.arslan@okul.edu'),
            ('Okan', 'Turan', 'Rehberlik', '0541-111-2222', 'okan.turan@okul.edu')
        ]
        
        for ogretmen in ogretmenler:
            c.execute('INSERT OR IGNORE INTO ogretmenler (ad, soyad, brans, telefon, email) VALUES (?, ?, ?, ?, ?)', ogretmen)
        
        # Örnek öğrenciler ekle
        ogrenciler = [
            ('Ahmet', 'Yıldırım', '12345678901', '2015-03-15', 4, 1, 'Mustafa Yıldırım', '0542-111-1111', 'Disleksi'),
            ('Elif', 'Karaca', '12345678902', '2014-07-22', 6, 1, 'Ayşe Karaca', '0543-222-2222', ''),
            ('Murat', 'Özdemir', '12345678903', '2016-01-10', 3, 2, 'Hüseyin Özdemir', '0544-333-3333', 'Otizm spektrum'),
            ('Selin', 'Kılıç', '12345678904', '2015-09-05', 4, 2, 'Fatma Kılıç', '0545-444-4444', ''),
            ('Emirhan', 'Şen', '12345678905', '2017-02-28', 2, 3, 'Oğuz Şen', '0546-555-5555', 'Dikkat eksikliği'),
            ('Aysun', 'Polat', '12345678906', '2016-11-12', 4, 3, 'Melek Polat', '0547-666-6666', ''),
            ('Kemal', 'Erdoğan', '12345678907', '2015-05-18', 6, 4, 'İbrahim Erdoğan', '0548-777-7777', 'Down sendromu'),
            ('Deniz', 'Çakır', '12345678908', '2014-12-03', 3, 4, 'Songül Çakır', '0549-888-8888', ''),
            ('Yusuf', 'Koç', '12345678909', '2016-08-25', 4, 5, 'Ahmet Koç', '0540-999-9999', ''),
            ('Merve', 'Güneş', '12345678910', '2017-04-14', 2, 5, 'Emine Güneş', '0551-111-1111', 'Serebral palsi'),
            ('Berk', 'Aydın', '12345678911', '2015-10-07', 6, 6, 'Murat Aydın', '0552-222-2222', ''),
            ('İrem', 'Kara', '12345678912', '2016-06-30', 3, 6, 'Züleyha Kara', '0553-333-3333', 'Zihinsel yetersizlik'),
            ('Oğuz', 'Bulut', '12345678913', '2017-01-20', 2, 7, 'Hakan Bulut', '0554-444-4444', 'Öğrenme güçlüğü'),
            ('Aslı', 'Yurt', '12345678914', '2015-12-08', 4, 7, 'Sevil Yurt', '0555-555-5555', ''),
            ('Can', 'Özer', '12345678915', '2016-03-16', 6, 1, 'Tolga Özer', '0556-666-6666', '')
        ]
        
        for ogrenci in ogrenciler:
            c.execute('''INSERT OR IGNORE INTO ogrenciler 
                        (ad, soyad, tc_no, dogum_tarihi, ders_saati, sinif_id, veli_adi, veli_telefon, ozel_durum) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', ogrenci)
        
        # Sınıf-öğretmen atamaları
        atamalar = [
            (1, 1),  # 1-A Sınıfı - Ayşe Yılmaz (Matematik)
            (1, 7),  # 1-A Sınıfı - Elif Şahin (Özel Eğitim)
            (2, 2),  # 1-B Sınıfı - Mehmet Demir (Türkçe)
            (2, 9),  # 1-B Sınıfı - Seda Arslan (Psikoloji)
            (3, 3),  # 2-A Sınıfı - Fatma Kaya (Fen Bilimleri)
            (4, 4),  # 2-B Sınıfı - Ali Özkan (Sosyal Bilgiler)
            (5, 5),  # 3-A Sınıfı - Zeynep Çelik (Resim)
            (5, 6),  # 3-A Sınıfı - Hasan Acar (Müzik)
            (6, 7),  # Hazırlık Sınıfı - Elif Şahin (Özel Eğitim)
            (6, 10), # Hazırlık Sınıfı - Okan Turan (Rehberlik)
            (7, 7),  # Destek Sınıfı - Elif Şahin (Özel Eğitim)
            (7, 9)   # Destek Sınıfı - Seda Arslan (Psikoloji)
        ]
        
        for atama in atamalar:
            c.execute('INSERT OR IGNORE INTO sinif_ogretmen (sinif_id, ogretmen_id) VALUES (?, ?)', atama)
        
        conn.commit()
        print("✅ Test verileri başarıyla eklendi!")
        print(f"📚 {len(siniflar)} sınıf eklendi")
        print(f"👩‍🏫 {len(ogretmenler)} öğretmen eklendi")
        print(f"👨‍🎓 {len(ogrenciler)} öğrenci eklendi")
        print(f"🔗 {len(atamalar)} sınıf-öğretmen ataması yapıldı")
        
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    test_verileri_ekle()
