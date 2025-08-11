# ÖZEL EĞİTİM OKULU YÖNETİM SİSTEMİ

Bu uygulama özel eğitim okulları için geliştirilmiş kapsamlı bir yönetim sistemidir.

## ÖZELLİKLER

### 📚 Sınıf Yönetimi
- 40+ sınıf ekleme ve yönetme
- Sınıf kapasitesi belirleme
- Sınıf açıklamaları
- Öğretmen atamaları

### 👨‍🎓 Öğrenci Yönetimi
- Öğrenci ekleme/düzenleme/silme
- Farklı ders saatleri (2, 3, 4, 6 saat)
- Veli bilgileri
- Özel durum notları
- Sınıf atamaları

### 👩‍🏫 Öğretmen Yönetimi
- 100+ öğretmen kaydı
- Branş bilgileri
- Sınıf atamaları
- İletişim bilgileri

### 🔍 Öğrenci Arama
- Ad/soyad ile arama
- TC kimlik no ile arama
- Sınıfa göre filtreleme
- Ders saatine göre filtreleme

### 🔄 Transfer İşlemleri
- Öğrencileri sınıflar arası transfer
- Ders saati değişikliği
- Transfer geçmişi
- Transfer notları

### 📊 Yönetici Raporları
- Genel istatistikler
- Sınıf doluluk oranları
- Öğretmen atamaları
- Ders saati dağılımı
- CSV formatında rapor dışa aktarma

## KURULUM VE ÇALIŞTIRMA

1. **Gereksinimler:**
   - Python 3.6 veya üzeri
   - tkinter (Python ile birlikte gelir)
   - sqlite3 (Python ile birlikte gelir)

2. **Çalıştırma:**
   ```
   python main.py
   ```

## DOSYA YAPISI

```
ÖZTAKİP/
├── main.py                 # Ana uygulama dosyası
├── sinif_yonetimi.py      # Sınıf yönetimi modülü
├── ogrenci_yonetimi.py    # Öğrenci yönetimi modülü
├── ogretmen_yonetimi.py   # Öğretmen yönetimi modülü
├── ogrenci_arama.py       # Arama ve transfer modülü
├── yonetici_raporu.py     # Rapor modülü
├── okul_yonetim.db        # SQLite veritabanı (otomatik oluşur)
└── README.md              # Bu dosya
```

## VERİTABANI

Uygulama SQLite veritabanı kullanır. Veritabanı dosyası (`okul_yonetim.db`) ilk çalıştırmada otomatik olarak oluşturulur.

### Tablolar:
- **siniflar**: Sınıf bilgileri
- **ogrenciler**: Öğrenci bilgileri
- **ogretmenler**: Öğretmen bilgileri
- **sinif_ogretmen**: Sınıf-öğretmen eşleştirmeleri
- **transfer_gecmisi**: Transfer işlem geçmişi

## KULLANIM KILAVUZU

### 1. İlk Kullanım
- Uygulamayı başlattıktan sonra önce sınıfları oluşturun
- Öğretmenleri ekleyin
- Öğrencileri ekleyip sınıflara atayın

### 2. Sınıf Yönetimi
- "SINIF YÖNETİMİ" butonuna tıklayın
- Sınıf adı ve kapasite girin
- "Sınıf Ekle" butonuna tıklayın
- Listeden sınıf seçerek düzenleyebilir veya silebilirsiniz

### 3. Öğrenci Yönetimi
- "ÖĞRENCİ YÖNETİMİ" butonuna tıklayın
- Öğrenci bilgilerini doldurun
- Ders saatini seçin (2, 3, 4, 6 saat)
- Sınıf ataması yapın

### 4. Öğretmen Yönetimi
- "ÖĞRETMEN YÖNETİMİ" butonuna tıklayın
- Öğretmen bilgilerini girin
- Sınıf atama bölümünden sınıf ataması yapın

### 5. Arama Sistemi
- "ÖĞRENCİ ARAMA" butonuna tıklayın
- Farklı kriterlere göre arama yapın
- Sonuçları CSV olarak dışa aktarın

### 6. Transfer İşlemleri
- "TRANSFER İŞLEMLERİ" butonuna tıklayın
- Öğrenci seçin
- Yeni sınıf ve ders saati belirleyin
- Transfer notunu yazın

### 7. Raporlar
- "YÖNETİCİ RAPORU" butonuna tıklayın
- Farklı sekmeleri inceleyin
- İstediğiniz raporu CSV olarak kaydedin

## YEDEKLEME

Veritabanı dosyası (`okul_yonetim.db`) düzenli olarak yedeklenmelidir. Bu dosya tüm okul verilerini içerir.

## SORUN GİDERME

### Uygulama açılmıyor:
- Python'ın kurulu olduğundan emin olun
- Dosya yolunda Türkçe karakter varsa İngilizce klasöre taşıyın

### Veritabanı hatası:
- `okul_yonetim.db` dosyasını silin, tekrar oluşacaktır
- Yedek varsa eski dosyayı geri yükleyin

### Türkçe karakter sorunu:
- Dosyalar UTF-8 kodlamasında kaydedilmiştir
- Excel'de açarken "UTF-8" seçin

## DESTEK

Bu uygulama özel eğitim okullarının ihtiyaçları doğrultusunda geliştirilmiştir. 
Öneriler ve hata bildirimleri için lütfen iletişime geçin.

---
**Geliştirici:** GitHub Copilot  
**Versiyon:** 1.0  
**Tarih:** Ağustos 2025
