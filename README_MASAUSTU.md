# Özel Eğitim Okulu Yönetim Sistemi - Masaüstü Uygulaması

## 🎯 Uygulamanın Amacı

Bu uygulama, özel eğitim okulları için geliştirilmiş kapsamlı bir yönetim sistemidir. Okul yöneticilerinin sınıf, öğrenci ve öğretmen yönetimi işlemlerini tek bir platform üzerinden gerçekleştirmelerine olanak sağlar.

## 📋 Özellikler

### 🏫 Sınıf Yönetimi
- Yeni sınıf ekleme
- Mevcut sınıfları görüntüleme ve düzenleme
- Sınıf bilgilerini güncelleme
- Sınıf silme işlemleri

### 👥 Öğrenci Yönetimi
- Öğrenci kaydı oluşturma
- Öğrenci bilgilerini düzenleme
- Öğrenci arama ve filtreleme
- Öğrenci sınıf atamaları
- Transfer işlemleri

### 👨‍🏫 Öğretmen Yönetimi
- Öğretmen kaydı oluşturma
- Öğretmen bilgilerini güncelleme
- Sınıf-öğretmen atamaları
- Branş bazlı öğretmen listelemeleri

### 🔍 Arama ve Raporlama
- Gelişmiş öğrenci arama
- Sınıf bazlı raporlar
- Öğretmen ders programları
- Transfer geçmişi takibi

## 💻 Sistem Gereksinimleri

- **İşletim Sistemi:** Windows 10 veya üzeri
- **Bellek:** Minimum 2GB RAM
- **Disk Alanı:** 100MB boş alan

## 🚀 Kurulum ve Kullanım

1. **Kurulum:** Herhangi bir kurulum gerektirmez, tek dosya olarak çalışır
2. **Başlatma:** `OkulYonetimSistemi.exe` dosyasına çift tıklayın
3. **İlk Kullanım:** Uygulama ilk açılışta örnek verilerle gelir

## 📁 Dosya Yapısı

```
ÖZTAKİP/
├── OkulYonetimSistemi.exe     # Ana uygulama dosyası
├── okul_yonetim.db            # Veritabanı dosyası (otomatik oluşur)
└── README_MASAUSTU.md         # Bu dosya
```

## 🔧 Teknik Özellikler

- **Geliştirme Dili:** Python 3.9
- **Arayüz:** Tkinter (Native Windows görünümü)
- **Veritabanı:** SQLite (Yerel dosya tabanlı)
- **Paketleme:** PyInstaller
- **Boyut:** ~11MB (tüm bağımlılıklar dahil)

## 📊 Veritabanı Yapısı

Uygulama aşağıdaki tablolarla çalışır:
- **siniflar:** Sınıf bilgileri
- **ogrenciler:** Öğrenci kayıtları
- **ogretmenler:** Öğretmen bilgileri
- **sinif_ogretmen:** Sınıf-öğretmen atamaları
- **transfer_gecmisi:** Öğrenci transfer kayıtları

## ✅ Çalışma Durumu - SON GÜNCELLEME

✅ **TAMAMEN ÇALIŞIYOR!** (V2 - 11.08.2025 18:07)
- ✅ Tüm Tkinter/TCL sorunları çözüldü
- ✅ Modül import hataları düzeltildi
- ✅ Veritabanı bağlantısı çalışıyor
- ✅ Tüm özellikler aktif
- ✅ Masaüstü uygulaması tamamen işlevsel
- ✅ Boyut: ~10MB (optimize edilmiş)

### 🔧 Son Çözüm:
PyInstaller ile `--add-data` parametresi kullanılarak Python kurulumundan doğrudan TCL klasörü kopyalandı. Bu yaklaşım TCL init dosyalarının doğru şekilde paketlenmesini sağladı.

## 🆘 Sorun Giderme

### Uygulama Açılmıyor
- Windows Defender veya antivirüs yazılımının uygulamayı engellediğini kontrol edin
- Dosya izinlerini kontrol edin
- Yönetici olarak çalıştırmayı deneyin

### Veriler Kayboldu
- `okul_yonetim.db` dosyasının silinip silinmediğini kontrol edin
- Uygulama yeniden başlatıldığında otomatik olarak yeni veritabanı oluşturulur

### Performans Sorunları
- Çok fazla veri varsa arama filtrelerini kullanın
- Gereksiz kayıtları silin

## 📞 Destek

Bu uygulama açık kaynak yazılım olarak geliştirilmiştir. Teknik destek için:
- Kaynak kodları inceleyebilirsiniz
- Hata raporları ve öneriler için issue açabilirsiniz

## 📝 Lisans

Bu yazılım eğitim amaçlı geliştirilmiştir ve özgürce kullanılabilir.

## 📈 Sürüm Geçmişi

### v1.0.0 (2024)
- ✅ İlk stabil sürüm
- ✅ Tüm temel özellikler
- ✅ Masaüstü uygulaması paketi
- ✅ Otomatik veritabanı yönetimi

---

**© 2024 Özel Eğitim Okulu Yönetim Sistemi**
