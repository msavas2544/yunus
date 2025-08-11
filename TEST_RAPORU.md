# ÖZEL EĞİTİM OKULU YÖNETİM SİSTEMİ - TEST VERİLERİ

## 🎉 UYGULAMA BAŞARIYLA TAMAMLANDI VE TEST EDİLDİ!

### 📊 Test Verileri Özeti:

#### 📚 Sınıflar (7 adet):
1. **1-A Sınıfı** - Kapasite: 15 (Matematik ağırlıklı)
2. **1-B Sınıfı** - Kapasite: 12 (Türkçe ağırlıklı)
3. **2-A Sınıfı** - Kapasite: 18 (Fen bilimleri ağırlıklı)
4. **2-B Sınıfı** - Kapasite: 14 (Sosyal bilimler ağırlıklı)
5. **3-A Sınıfı** - Kapasite: 16 (Sanat ağırlıklı)
6. **Hazırlık Sınıfı** - Kapasite: 10 (Okula uyum)
7. **Destek Sınıfı** - Kapasite: 8 (Bireysel destek)

#### 👩‍🏫 Öğretmenler (10 adet):
1. **Ayşe Yılmaz** - Matematik (0532-111-1111)
2. **Mehmet Demir** - Türkçe (0533-222-2222)
3. **Fatma Kaya** - Fen Bilimleri (0534-333-3333)
4. **Ali Özkan** - Sosyal Bilgiler (0535-444-4444)
5. **Zeynep Çelik** - Resim (0536-555-5555)
6. **Hasan Acar** - Müzik (0537-666-6666)
7. **Elif Şahin** - Özel Eğitim (0538-777-7777)
8. **Burak Yıldız** - Beden Eğitimi (0539-888-8888)
9. **Seda Arslan** - Psikoloji (0530-999-9999)
10. **Okan Turan** - Rehberlik (0541-111-2222)

#### 👨‍🎓 Öğrenciler (15 adet):
- **Çeşitli özel ihtiyaçlar**: Disleksi, Otizm spektrum, Dikkat eksikliği, Down sendromu, vb.
- **Farklı ders saatleri**: 2, 3, 4, 6 saat seçenekleri
- **Veli bilgileri**: Tüm öğrenciler için veli adı ve telefonu
- **Sınıf atamaları**: Farklı sınıflara dağıtılmış

#### 🔄 Transfer Örnekleri:
1. **Ahmet Yıldırım**: 1-A'dan 2-A'ya (4 saatten 6 saate)
2. **Murat Özdemir**: 1-B'den Destek Sınıfına (3 saatten 2 saate)

#### 🔗 Sınıf-Öğretmen Atamaları (12 adet):
- Her sınıfa uygun branş öğretmenleri atanmış
- Özel eğitim ve psikoloji öğretmenleri birden fazla sınıfa atanmış

### 🛠️ Test Edilebilir Özellikler:

#### ✅ Sınıf Yönetimi:
- Mevcut 7 sınıfı görüntüleme
- Yeni sınıf ekleme
- Sınıf düzenleme/silme
- Kapasite kontrolü

#### ✅ Öğrenci Yönetimi:
- 15 örnek öğrenciyi görüntüleme
- Yeni öğrenci ekleme
- Farklı ders saati seçenekleri (2,3,4,6)
- Veli bilgileri girişi
- Özel durum notları
- Sınıf ataması

#### ✅ Öğretmen Yönetimi:
- 10 örnek öğretmeni görüntüleme
- Yeni öğretmen ekleme
- Branş bilgileri
- Sınıf atama işlemleri
- İletişim bilgileri

#### ✅ Öğrenci Arama:
- Ad/soyad ile arama
- TC kimlik no ile arama
- Sınıf filtreleme
- Ders saati filtreleme
- Sonuçları CSV olarak dışa aktarma

#### ✅ Transfer İşlemleri:
- Mevcut 2 transfer kaydını görüntüleme
- Yeni transfer yapma
- Sınıf değiştirme
- Ders saati değiştirme
- Transfer notları
- Transfer geçmişi

#### ✅ Yönetici Raporları:
- **Genel İstatistikler**: Toplam sayılar, ders saati dağılımı
- **Sınıf Doluluk Raporu**: Kapasite kullanım oranları
- **Öğretmen Atama Raporu**: Hangi öğretmen hangi sınıfta
- **Transfer Raporu**: Transfer geçmişi
- **CSV Dışa Aktarma**: Tüm raporlar için

### 🎯 Nasıl Test Edilir:

1. **Uygulamayı Başlatma**:
   ```
   cd ÖZTAKİP
   python main.py
   ```

2. **Ana Menüden İstediğiniz Modülü Seçin**:
   - Sınıf Yönetimi
   - Öğrenci Yönetimi
   - Öğretmen Yönetimi
   - Öğrenci Arama
   - Transfer İşlemleri
   - Yönetici Raporu

3. **Her Modülde**:
   - Mevcut verileri görüntüleyin
   - Yeni kayıt ekleyin
   - Arama/filtreleme yapın
   - Raporları CSV olarak indirin

### 📁 Dosya Yapısı:
```
ÖZTAKİP/
├── main.py                 # Ana uygulama
├── db_utils.py            # Veritabanı işlemleri
├── sinif_yonetimi.py      # Sınıf modülü
├── ogrenci_yonetimi.py    # Öğrenci modülü
├── ogretmen_yonetimi.py   # Öğretmen modülü
├── ogrenci_arama.py       # Arama ve transfer
├── yonetici_raporu.py     # Raporlar
├── test_verileri.py       # Test veri oluşturucu
├── ornek_transfer.py      # Transfer örnekleri
├── okul_yonetim.db        # SQLite veritabanı
└── __init__.py            # Python paketi
```

### 🚀 Sonuç:
Özel Eğitim Okulu Yönetim Sistemi tamamen işlevsel ve test edilmiş durumda!
Tüm modüller çalışıyor, test verileri yüklü ve kullanıma hazır.
