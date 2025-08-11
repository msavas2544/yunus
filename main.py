import os
import sys

# PyInstaller için Tkinter düzeltmesi
if hasattr(sys, '_MEIPASS'):
    # PyInstaller paketlenmiş uygulama
    base_path = sys._MEIPASS
    
    # Tüm olası TCL/TK konumlarını dene
    possible_paths = [
        os.path.join(base_path, 'tcl', 'tcl8.6'),
        os.path.join(base_path, 'tcl', 'tk8.6'),
        os.path.join(base_path, 'tcl'),
        os.path.join(base_path, 'tcl8.6'),
        os.path.join(base_path, 'tk8.6'),
        os.path.join(base_path, '_internal', 'tcl'),
        os.path.join(base_path, '_internal', 'tcl8.6'),
    ]
    
    # init.tcl dosyasını özel olarak ara
    init_tcl_found = False
    for root, dirs, files in os.walk(base_path):
        if 'init.tcl' in files:
            tcl_dir = root
            os.environ['TCL_LIBRARY'] = tcl_dir
            print(f"Found init.tcl in: {tcl_dir}")
            init_tcl_found = True
            break
    
    # Eğer init.tcl bulunamazsa standart yolları dene
    if not init_tcl_found:
        # TCL_LIBRARY ayarla
        for path in possible_paths:
            if os.path.exists(path):
                init_tcl_path = os.path.join(path, 'init.tcl')
                if os.path.exists(init_tcl_path):
                    os.environ['TCL_LIBRARY'] = path
                    print(f"TCL_LIBRARY set to: {path}")
                    break
                elif 'tcl' in path.lower():
                    os.environ['TCL_LIBRARY'] = path
                    print(f"Fallback TCL_LIBRARY set to: {path}")
                    break
    
    # TK_LIBRARY ayarla
    for path in possible_paths:
        if os.path.exists(path) and 'tk' in path.lower():
            os.environ['TK_LIBRARY'] = path
            print(f"TK_LIBRARY set to: {path}")
            break
    
    # Son çare: tcl klasörünün tamamını kullan
    tcl_base = os.path.join(base_path, 'tcl')
    if os.path.exists(tcl_base):
        if 'TCL_LIBRARY' not in os.environ:
            os.environ['TCL_LIBRARY'] = tcl_base
            print(f"Final fallback TCL_LIBRARY set to: {tcl_base}")
        if 'TK_LIBRARY' not in os.environ:
            os.environ['TK_LIBRARY'] = tcl_base
            print(f"Final fallback TK_LIBRARY set to: {tcl_base}")
    
    # PATH'e de ekle
    if tcl_base and os.path.exists(tcl_base):
        current_path = os.environ.get('PATH', '')
        if tcl_base not in current_path:
            os.environ['PATH'] = tcl_base + os.pathsep + current_path
    
    # Ortam değişkenlerini kontrol et
    print(f"TCL_LIBRARY = {os.environ.get('TCL_LIBRARY', 'NOT SET')}")
    print(f"TK_LIBRARY = {os.environ.get('TK_LIBRARY', 'NOT SET')}")
    
    # init.tcl dosyasının varlığını kontrol et
    tcl_lib = os.environ.get('TCL_LIBRARY')
    if tcl_lib:
        init_path = os.path.join(tcl_lib, 'init.tcl')
        print(f"Checking init.tcl at: {init_path}")
        print(f"init.tcl exists: {os.path.exists(init_path)}")
        if os.path.exists(init_path):
            print("✅ init.tcl found successfully!")
        else:
            print("❌ init.tcl not found!")
            # Tcl klasöründeki dosyaları listele
            if os.path.exists(tcl_lib):
                files = os.listdir(tcl_lib)[:10]  # İlk 10 dosyayı göster
                print(f"Files in TCL_LIBRARY: {files}")

# Tkinter import'undan önce biraz bekle
import time
time.sleep(0.1)

import tkinter as tk
from tkinter import messagebox, ttk, filedialog

# Modül yolunu ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Tüm modülleri import et
try:
    from db_utils import init_db
    from sinif_yonetimi import sinif_ekle, siniflari_listele, sinif_sil
    from ogrenci_yonetimi import ogrenci_ekle, ogrencileri_listele, ogrenci_sil, siniflari_getir
    from ogretmen_yonetimi import ogretmen_ekle, ogretmenleri_listele, ogretmen_sil, sinif_ogretmen_ata, sinif_ogretmen_listele
    from ogrenci_arama import ogrenci_ara, csv_export, ogrenci_transfer, transfer_gecmisini_getir
    from yonetici_raporu import genel_istatistikler, sinif_doluluk_raporu, ogretmen_atama_raporu, transfer_raporu, csv_rapor_export
    
    # Veritabanını başlat
    init_db()
    print("✅ Tüm modüller başarıyla yüklendi!")
    
except ImportError as e:
    print(f"❌ Modül yükleme hatası: {e}")
    messagebox.showerror("Hata", f"Gerekli modüller yüklenemiyor: {e}")
    sys.exit(1)

class OkulYonetimApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Özel Eğitim Okulu Yönetim Sistemi')
        self.geometry('600x400')
        self.resizable(True, True)
        self.create_main_menu()

    def create_main_menu(self):
        # Başlık
        tk.Label(self, text='Özel Eğitim Okulu Yönetim Sistemi', 
                font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Butonlar
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)
        
        buttons = [
            ('SINIF YÖNETİMİ', self.open_sinif_yonetimi),
            ('ÖĞRENCİ YÖNETİMİ', self.open_ogrenci_yonetimi),
            ('ÖĞRETMEN YÖNETİMİ', self.open_ogretmen_yonetimi),
            ('ÖĞRENCİ ARAMA', self.open_ogrenci_arama),
            ('TRANSFER İŞLEMLERİ', self.open_transfer_islemleri),
            ('YÖNETİCİ RAPORU', self.open_yonetici_raporu)
        ]
        
        for text, command in buttons:
            tk.Button(button_frame, text=text, width=25, height=2, 
                     font=('Arial', 10), command=command).pack(pady=5)

    def open_sinif_yonetimi(self):
        win = tk.Toplevel(self)
        win.title('Sınıf Yönetimi')
        win.geometry('600x500')

        def refresh_list():
            for row in tree.get_children():
                tree.delete(row)
            for s in siniflari_listele():
                tree.insert('', 'end', values=s)

        def ekle():
            ad = entry_ad.get()
            kapasite = entry_kapasite.get()
            aciklama = entry_aciklama.get()
            if ad and kapasite.isdigit():
                sinif_ekle(ad, int(kapasite), aciklama)
                refresh_list()
                entry_ad.delete(0, 'end')
                entry_kapasite.delete(0, 'end')
                entry_aciklama.delete(0, 'end')
                messagebox.showinfo('Başarılı', 'Sınıf başarıyla eklendi!')
            else:
                messagebox.showerror('Hata', 'Sınıf adı ve kapasite gereklidir.')

        def sil():
            selected = tree.selection()
            if selected:
                result = messagebox.askyesno('Onay', 'Seçili sınıfı silmek istediğinizden emin misiniz?')
                if result:
                    sinif_id = tree.item(selected[0])['values'][0]
                    sinif_sil(sinif_id)
                    refresh_list()
                    messagebox.showinfo('Başarılı', 'Sınıf başarıyla silindi!')

        # Form
        form_frame = tk.LabelFrame(win, text='Yeni Sınıf Ekle', padx=10, pady=10)
        form_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(form_frame, text='Sınıf Adı:').grid(row=0, column=0, sticky='w', pady=2)
        entry_ad = tk.Entry(form_frame, width=30)
        entry_ad.grid(row=0, column=1, pady=2, padx=5)
        
        tk.Label(form_frame, text='Kapasite:').grid(row=1, column=0, sticky='w', pady=2)
        entry_kapasite = tk.Entry(form_frame, width=30)
        entry_kapasite.grid(row=1, column=1, pady=2, padx=5)
        
        tk.Label(form_frame, text='Açıklama:').grid(row=2, column=0, sticky='w', pady=2)
        entry_aciklama = tk.Entry(form_frame, width=30)
        entry_aciklama.grid(row=2, column=1, pady=2, padx=5)
        
        tk.Button(form_frame, text='Sınıf Ekle', command=ekle, bg='green', fg='white').grid(row=3, column=0, columnspan=2, pady=10)

        # Liste
        list_frame = tk.LabelFrame(win, text='Mevcut Sınıflar', padx=10, pady=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tree = ttk.Treeview(list_frame, columns=('id', 'ad', 'kapasite', 'aciklama'), show='headings')
        tree.heading('id', text='ID')
        tree.heading('ad', text='Sınıf Adı')
        tree.heading('kapasite', text='Kapasite')
        tree.heading('aciklama', text='Açıklama')
        
        tree.column('id', width=50)
        tree.column('ad', width=150)
        tree.column('kapasite', width=100)
        tree.column('aciklama', width=200)
        
        tree.pack(fill='both', expand=True)
        
        tk.Button(list_frame, text='Seçili Sınıfı Sil', command=sil, bg='red', fg='white').pack(pady=5)
        
        refresh_list()

    def open_ogrenci_yonetimi(self):
        win = tk.Toplevel(self)
        win.title('Öğrenci Yönetimi')
        win.geometry('1000x700')

        def refresh_list():
            for row in tree.get_children():
                tree.delete(row)
            for o in ogrencileri_listele():
                tree.insert('', 'end', values=o)

        def ekle():
            ad = entry_ad.get()
            soyad = entry_soyad.get()
            tc_no = entry_tc.get()
            dogum_tarihi = entry_dogum.get()
            ders_saati = combo_ders_saati.get()
            sinif_secim = combo_sinif.get()
            sinif_id = sinif_secim.split(' - ')[0] if sinif_secim else None
            veli_adi = entry_veli_adi.get()
            veli_telefon = entry_veli_tel.get()
            ozel_durum = entry_ozel_durum.get()
            
            if ad and soyad and ders_saati:
                if ogrenci_ekle(ad, soyad, tc_no, dogum_tarihi, int(ders_saati), 
                               int(sinif_id) if sinif_id else None, veli_adi, veli_telefon, ozel_durum):
                    refresh_list()
                    # Alanları temizle
                    for entry in [entry_ad, entry_soyad, entry_tc, entry_dogum, entry_veli_adi, entry_veli_tel, entry_ozel_durum]:
                        entry.delete(0, 'end')
                    combo_ders_saati.set('')
                    combo_sinif.set('')
                    messagebox.showinfo('Başarılı', 'Öğrenci başarıyla eklendi!')
                else:
                    messagebox.showerror('Hata', 'Öğrenci eklenirken hata oluştu.')
            else:
                messagebox.showerror('Hata', 'Ad, soyad ve ders saati gereklidir.')

        def sil():
            selected = tree.selection()
            if selected:
                result = messagebox.askyesno('Onay', 'Seçili öğrenciyi silmek istediğinizden emin misiniz?')
                if result:
                    ogrenci_id = tree.item(selected[0])['values'][0]
                    ogrenci_sil(ogrenci_id)
                    refresh_list()
                    messagebox.showinfo('Başarılı', 'Öğrenci başarıyla silindi!')

        # Form
        form_frame = tk.LabelFrame(win, text='Yeni Öğrenci Ekle', padx=10, pady=10)
        form_frame.pack(fill='x', padx=10, pady=5)
        
        # İlk satır
        tk.Label(form_frame, text='Ad:').grid(row=0, column=0, sticky='w', pady=2)
        entry_ad = tk.Entry(form_frame, width=15)
        entry_ad.grid(row=0, column=1, pady=2, padx=2)
        
        tk.Label(form_frame, text='Soyad:').grid(row=0, column=2, sticky='w', pady=2)
        entry_soyad = tk.Entry(form_frame, width=15)
        entry_soyad.grid(row=0, column=3, pady=2, padx=2)
        
        # İkinci satır
        tk.Label(form_frame, text='TC No:').grid(row=1, column=0, sticky='w', pady=2)
        entry_tc = tk.Entry(form_frame, width=15)
        entry_tc.grid(row=1, column=1, pady=2, padx=2)
        
        tk.Label(form_frame, text='Doğum Tarihi:').grid(row=1, column=2, sticky='w', pady=2)
        entry_dogum = tk.Entry(form_frame, width=15)
        entry_dogum.grid(row=1, column=3, pady=2, padx=2)
        
        # Üçüncü satır
        tk.Label(form_frame, text='Ders Saati:').grid(row=2, column=0, sticky='w', pady=2)
        combo_ders_saati = ttk.Combobox(form_frame, values=['2', '3', '4', '6'], state='readonly', width=12)
        combo_ders_saati.grid(row=2, column=1, pady=2, padx=2)
        
        tk.Label(form_frame, text='Sınıf:').grid(row=2, column=2, sticky='w', pady=2)
        siniflar = [f"{s[0]} - {s[1]}" for s in siniflari_getir()]
        combo_sinif = ttk.Combobox(form_frame, values=siniflar, state='readonly', width=12)
        combo_sinif.grid(row=2, column=3, pady=2, padx=2)
        
        # Dördüncü satır
        tk.Label(form_frame, text='Veli Adı:').grid(row=3, column=0, sticky='w', pady=2)
        entry_veli_adi = tk.Entry(form_frame, width=15)
        entry_veli_adi.grid(row=3, column=1, pady=2, padx=2)
        
        tk.Label(form_frame, text='Veli Tel:').grid(row=3, column=2, sticky='w', pady=2)
        entry_veli_tel = tk.Entry(form_frame, width=15)
        entry_veli_tel.grid(row=3, column=3, pady=2, padx=2)
        
        # Beşinci satır
        tk.Label(form_frame, text='Özel Durum:').grid(row=4, column=0, sticky='w', pady=2)
        entry_ozel_durum = tk.Entry(form_frame, width=50)
        entry_ozel_durum.grid(row=4, column=1, columnspan=3, pady=2, padx=2, sticky='ew')
        
        tk.Button(form_frame, text='Öğrenci Ekle', command=ekle, bg='green', fg='white').grid(row=5, column=0, columnspan=4, pady=10)

        # Liste
        list_frame = tk.LabelFrame(win, text='Mevcut Öğrenciler', padx=10, pady=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tree = ttk.Treeview(list_frame, columns=('id', 'ad', 'soyad', 'tc', 'ders_saati', 'sinif', 'veli'), show='headings')
        tree.heading('id', text='ID')
        tree.heading('ad', text='Ad')
        tree.heading('soyad', text='Soyad')
        tree.heading('tc', text='TC No')
        tree.heading('ders_saati', text='Ders Saati')
        tree.heading('sinif', text='Sınıf')
        tree.heading('veli', text='Veli')
        
        for col in ['id', 'ad', 'soyad', 'tc', 'ders_saati', 'sinif', 'veli']:
            tree.column(col, width=120)
        
        tree.pack(fill='both', expand=True)
        
        tk.Button(list_frame, text='Seçili Öğrenciyi Sil', command=sil, bg='red', fg='white').pack(pady=5)
        
        refresh_list()

    def open_ogretmen_yonetimi(self):
        win = tk.Toplevel(self)
        win.title('Öğretmen Yönetimi')
        win.geometry('900x700')

        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Öğretmen Ekleme Sekmesi
        tab1 = tk.Frame(notebook)
        notebook.add(tab1, text='Öğretmen Ekleme')

        def refresh_ogretmen_list():
            for row in tree_ogretmen.get_children():
                tree_ogretmen.delete(row)
            for o in ogretmenleri_listele():
                tree_ogretmen.insert('', 'end', values=o)

        def ekle_ogretmen():
            ad = entry_og_ad.get()
            soyad = entry_og_soyad.get()
            brans = entry_og_brans.get()
            telefon = entry_og_telefon.get()
            email = entry_og_email.get()
            
            if ad and soyad:
                if ogretmen_ekle(ad, soyad, brans, telefon, email):
                    refresh_ogretmen_list()
                    for entry in [entry_og_ad, entry_og_soyad, entry_og_brans, entry_og_telefon, entry_og_email]:
                        entry.delete(0, 'end')
                    messagebox.showinfo('Başarılı', 'Öğretmen başarıyla eklendi!')
                else:
                    messagebox.showerror('Hata', 'Öğretmen eklenirken hata oluştu.')
            else:
                messagebox.showerror('Hata', 'Ad ve soyad gereklidir.')

        def sil_ogretmen():
            selected = tree_ogretmen.selection()
            if selected:
                result = messagebox.askyesno('Onay', 'Seçili öğretmeni silmek istediğinizden emin misiniz?')
                if result:
                    ogretmen_id = tree_ogretmen.item(selected[0])['values'][0]
                    ogretmen_sil(ogretmen_id)
                    refresh_ogretmen_list()
                    messagebox.showinfo('Başarılı', 'Öğretmen başarıyla silindi!')

        # Form
        form_frame = tk.LabelFrame(tab1, text='Yeni Öğretmen Ekle', padx=10, pady=10)
        form_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(form_frame, text='Ad:').grid(row=0, column=0, sticky='w', pady=2)
        entry_og_ad = tk.Entry(form_frame, width=20)
        entry_og_ad.grid(row=0, column=1, pady=2, padx=5)
        
        tk.Label(form_frame, text='Soyad:').grid(row=0, column=2, sticky='w', pady=2)
        entry_og_soyad = tk.Entry(form_frame, width=20)
        entry_og_soyad.grid(row=0, column=3, pady=2, padx=5)
        
        tk.Label(form_frame, text='Branş:').grid(row=1, column=0, sticky='w', pady=2)
        entry_og_brans = tk.Entry(form_frame, width=20)
        entry_og_brans.grid(row=1, column=1, pady=2, padx=5)
        
        tk.Label(form_frame, text='Telefon:').grid(row=1, column=2, sticky='w', pady=2)
        entry_og_telefon = tk.Entry(form_frame, width=20)
        entry_og_telefon.grid(row=1, column=3, pady=2, padx=5)
        
        tk.Label(form_frame, text='Email:').grid(row=2, column=0, sticky='w', pady=2)
        entry_og_email = tk.Entry(form_frame, width=40)
        entry_og_email.grid(row=2, column=1, columnspan=2, pady=2, padx=5, sticky='ew')
        
        tk.Button(form_frame, text='Öğretmen Ekle', command=ekle_ogretmen, bg='green', fg='white').grid(row=3, column=0, columnspan=4, pady=10)

        # Liste
        list_frame = tk.LabelFrame(tab1, text='Mevcut Öğretmenler', padx=10, pady=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_ogretmen = ttk.Treeview(list_frame, columns=('id', 'ad', 'soyad', 'brans', 'telefon', 'email'), show='headings')
        tree_ogretmen.heading('id', text='ID')
        tree_ogretmen.heading('ad', text='Ad')
        tree_ogretmen.heading('soyad', text='Soyad')
        tree_ogretmen.heading('brans', text='Branş')
        tree_ogretmen.heading('telefon', text='Telefon')
        tree_ogretmen.heading('email', text='Email')
        
        for col in ['id', 'ad', 'soyad', 'brans', 'telefon', 'email']:
            tree_ogretmen.column(col, width=130)
        
        tree_ogretmen.pack(fill='both', expand=True)
        
        tk.Button(list_frame, text='Seçili Öğretmeni Sil', command=sil_ogretmen, bg='red', fg='white').pack(pady=5)

        # Sınıf Atama Sekmesi
        tab2 = tk.Frame(notebook)
        notebook.add(tab2, text='Sınıf Atama')

        def refresh_atama_list():
            for row in tree_atama.get_children():
                tree_atama.delete(row)
            for a in sinif_ogretmen_listele():
                tree_atama.insert('', 'end', values=a)

        def sinif_ata():
            sinif_secim = combo_atama_sinif.get()
            ogretmen_secim = combo_atama_ogretmen.get()
            
            sinif_id = sinif_secim.split(' - ')[0] if sinif_secim else None
            ogretmen_id = ogretmen_secim.split(' - ')[0] if ogretmen_secim else None
            
            if sinif_id and ogretmen_id:
                if sinif_ogretmen_ata(int(sinif_id), int(ogretmen_id)):
                    refresh_atama_list()
                    combo_atama_sinif.set('')
                    combo_atama_ogretmen.set('')
                    messagebox.showinfo('Başarılı', 'Atama başarıyla yapıldı!')
                else:
                    messagebox.showerror('Hata', 'Atama yapılırken hata oluştu (Bu atama zaten mevcut olabilir).')
            else:
                messagebox.showerror('Hata', 'Sınıf ve öğretmen seçimi gereklidir.')

        # Atama formu
        atama_frame = tk.LabelFrame(tab2, text='Sınıf-Öğretmen Ataması', padx=10, pady=10)
        atama_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(atama_frame, text='Sınıf:').grid(row=0, column=0, sticky='w', pady=5)
        siniflar = [f"{s[0]} - {s[1]}" for s in siniflari_getir()]
        combo_atama_sinif = ttk.Combobox(atama_frame, values=siniflar, state='readonly', width=25)
        combo_atama_sinif.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(atama_frame, text='Öğretmen:').grid(row=0, column=2, sticky='w', pady=5)
        ogretmenler = [f"{o[0]} - {o[1]} {o[2]}" for o in ogretmenleri_listele()]
        combo_atama_ogretmen = ttk.Combobox(atama_frame, values=ogretmenler, state='readonly', width=25)
        combo_atama_ogretmen.grid(row=0, column=3, pady=5, padx=5)
        
        tk.Button(atama_frame, text='Sınıf Ata', command=sinif_ata, bg='blue', fg='white').grid(row=1, column=0, columnspan=4, pady=10)

        # Atama listesi
        list_frame2 = tk.LabelFrame(tab2, text='Mevcut Atamalar', padx=10, pady=10)
        list_frame2.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_atama = ttk.Treeview(list_frame2, columns=('id', 'sinif', 'ogretmen_ad', 'ogretmen_soyad'), show='headings')
        tree_atama.heading('id', text='ID')
        tree_atama.heading('sinif', text='Sınıf')
        tree_atama.heading('ogretmen_ad', text='Öğretmen Adı')
        tree_atama.heading('ogretmen_soyad', text='Soyadı')
        
        for col in ['id', 'sinif', 'ogretmen_ad', 'ogretmen_soyad']:
            tree_atama.column(col, width=200)
        
        tree_atama.pack(fill='both', expand=True)

        refresh_ogretmen_list()
        refresh_atama_list()

    def open_ogrenci_arama(self):
        win = tk.Toplevel(self)
        win.title('Öğrenci Arama')
        win.geometry('1000x600')

        def ara():
            arama_kriteri = combo_kriter.get()
            arama_metni = entry_arama.get()
            sinif_secim = combo_sinif_filtre.get()
            sinif_filtre = sinif_secim.split(' - ')[0] if sinif_secim else None
            ders_saati_filtre = combo_ders_saati_filtre.get() if combo_ders_saati_filtre.get() else None
            
            for row in tree_arama.get_children():
                tree_arama.delete(row)
            
            results = ogrenci_ara(arama_kriteri, arama_metni, 
                                int(sinif_filtre) if sinif_filtre else None,
                                int(ders_saati_filtre) if ders_saati_filtre else None)
            
            for result in results:
                tree_arama.insert('', 'end', values=result)
            
            status_label.config(text=f"Bulunan öğrenci sayısı: {len(results)}")

        def export_csv():
            data = []
            for item in tree_arama.get_children():
                data.append(tree_arama.item(item)['values'])
            
            if data:
                filename = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                    title="Arama Sonuçlarını Kaydet"
                )
                if filename:
                    if csv_export(data, filename):
                        messagebox.showinfo('Başarılı', f'Rapor başarıyla kaydedildi: {filename}')
                    else:
                        messagebox.showerror('Hata', 'Rapor kaydedilirken hata oluştu.')
            else:
                messagebox.showwarning('Uyarı', 'Dışa aktarılacak veri bulunmamaktadır.')

        # Arama formu
        form_frame = tk.LabelFrame(win, text='Arama Kriterleri', padx=10, pady=10)
        form_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(form_frame, text='Arama Kriteri:').grid(row=0, column=0, sticky='w', pady=2)
        combo_kriter = ttk.Combobox(form_frame, values=['ad_soyad', 'tc_no'], state='readonly', width=15)
        combo_kriter.grid(row=0, column=1, pady=2, padx=5)
        combo_kriter.set('ad_soyad')
        
        tk.Label(form_frame, text='Arama Metni:').grid(row=0, column=2, sticky='w', pady=2)
        entry_arama = tk.Entry(form_frame, width=20)
        entry_arama.grid(row=0, column=3, pady=2, padx=5)
        
        tk.Label(form_frame, text='Sınıf Filtresi:').grid(row=1, column=0, sticky='w', pady=2)
        siniflar = [''] + [f"{s[0]} - {s[1]}" for s in siniflari_getir()]
        combo_sinif_filtre = ttk.Combobox(form_frame, values=siniflar, state='readonly', width=15)
        combo_sinif_filtre.grid(row=1, column=1, pady=2, padx=5)
        
        tk.Label(form_frame, text='Ders Saati Filtresi:').grid(row=1, column=2, sticky='w', pady=2)
        combo_ders_saati_filtre = ttk.Combobox(form_frame, values=['', '2', '3', '4', '6'], state='readonly', width=15)
        combo_ders_saati_filtre.grid(row=1, column=3, pady=2, padx=5)
        
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        tk.Button(button_frame, text='Ara', command=ara, bg='blue', fg='white', width=10).pack(side='left', padx=5)
        tk.Button(button_frame, text='CSV Dışa Aktar', command=export_csv, bg='green', fg='white', width=15).pack(side='left', padx=5)

        # Sonuç listesi
        result_frame = tk.LabelFrame(win, text='Arama Sonuçları', padx=10, pady=10)
        result_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tree_arama = ttk.Treeview(result_frame, columns=('id', 'ad', 'soyad', 'tc', 'ders_saati', 'sinif', 'veli_adi', 'veli_tel', 'ozel_durum'), show='headings')
        tree_arama.heading('id', text='ID')
        tree_arama.heading('ad', text='Ad')
        tree_arama.heading('soyad', text='Soyad')
        tree_arama.heading('tc', text='TC No')
        tree_arama.heading('ders_saati', text='Ders Saati')
        tree_arama.heading('sinif', text='Sınıf')
        tree_arama.heading('veli_adi', text='Veli Adı')
        tree_arama.heading('veli_tel', text='Veli Tel')
        tree_arama.heading('ozel_durum', text='Özel Durum')
        
        for col in ['id', 'ad', 'soyad', 'tc', 'ders_saati', 'sinif', 'veli_adi', 'veli_tel', 'ozel_durum']:
            tree_arama.column(col, width=100)
        
        tree_arama.pack(fill='both', expand=True)
        
        status_label = tk.Label(result_frame, text="Arama yapmak için yukarıdaki kriterleri kullanın", fg='gray')
        status_label.pack(pady=5)

    def open_transfer_islemleri(self):
        win = tk.Toplevel(self)
        win.title('Transfer İşlemleri')
        win.geometry('900x600')

        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Transfer Yapma Sekmesi
        tab1 = tk.Frame(notebook)
        notebook.add(tab1, text='Transfer Yap')

        def transfer_yap():
            ogrenci_secim = combo_ogrenci.get()
            sinif_secim = combo_yeni_sinif.get()
            yeni_ders_saati = combo_yeni_ders_saati.get()
            transfer_notu = text_transfer_notu.get('1.0', 'end-1c')
            
            ogrenci_id = ogrenci_secim.split(' - ')[0] if ogrenci_secim else None
            yeni_sinif_id = sinif_secim.split(' - ')[0] if sinif_secim else None
            
            if ogrenci_id and yeni_sinif_id and yeni_ders_saati:
                if ogrenci_transfer(int(ogrenci_id), int(yeni_sinif_id), int(yeni_ders_saati), transfer_notu):
                    messagebox.showinfo('Başarılı', 'Transfer işlemi başarıyla tamamlandı!')
                    combo_ogrenci.set('')
                    combo_yeni_sinif.set('')
                    combo_yeni_ders_saati.set('')
                    text_transfer_notu.delete('1.0', 'end')
                    refresh_transfer_gecmisi()
                else:
                    messagebox.showerror('Hata', 'Transfer işlemi sırasında hata oluştu.')
            else:
                messagebox.showerror('Hata', 'Öğrenci, yeni sınıf ve ders saati seçimi gereklidir.')

        # Transfer formu
        form_frame = tk.LabelFrame(tab1, text='Transfer İşlemi', padx=10, pady=10)
        form_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(form_frame, text='Öğrenci:').grid(row=0, column=0, sticky='w', pady=5)
        ogrenciler = [f"{o[0]} - {o[1]} {o[2]}" for o in ogrencileri_listele()]
        combo_ogrenci = ttk.Combobox(form_frame, values=ogrenciler, state='readonly', width=40)
        combo_ogrenci.grid(row=0, column=1, pady=5, padx=5, columnspan=2)
        
        tk.Label(form_frame, text='Yeni Sınıf:').grid(row=1, column=0, sticky='w', pady=5)
        siniflar = [f"{s[0]} - {s[1]}" for s in siniflari_getir()]
        combo_yeni_sinif = ttk.Combobox(form_frame, values=siniflar, state='readonly', width=25)
        combo_yeni_sinif.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Label(form_frame, text='Yeni Ders Saati:').grid(row=1, column=2, sticky='w', pady=5)
        combo_yeni_ders_saati = ttk.Combobox(form_frame, values=['2', '3', '4', '6'], state='readonly', width=10)
        combo_yeni_ders_saati.grid(row=1, column=3, pady=5, padx=5)
        
        tk.Label(form_frame, text='Transfer Notu:').grid(row=2, column=0, sticky='nw', pady=5)
        text_transfer_notu = tk.Text(form_frame, height=4, width=50)
        text_transfer_notu.grid(row=2, column=1, columnspan=3, pady=5, padx=5)
        
        tk.Button(form_frame, text='Transfer Yap', command=transfer_yap, bg='orange', fg='white', width=20).grid(row=3, column=0, columnspan=4, pady=10)

        # Transfer Geçmişi Sekmesi
        tab2 = tk.Frame(notebook)
        notebook.add(tab2, text='Transfer Geçmişi')

        def refresh_transfer_gecmisi():
            for row in tree_gecmis.get_children():
                tree_gecmis.delete(row)
            for g in transfer_gecmisini_getir():
                tree_gecmis.insert('', 'end', values=g)

        list_frame = tk.LabelFrame(tab2, text='Transfer Geçmişi', padx=10, pady=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_gecmis = ttk.Treeview(list_frame, columns=('id', 'ogrenci', 'eski_sinif', 'yeni_sinif', 'eski_ders', 'yeni_ders', 'tarih', 'aciklama'), show='headings')
        tree_gecmis.heading('id', text='ID')
        tree_gecmis.heading('ogrenci', text='Öğrenci')
        tree_gecmis.heading('eski_sinif', text='Eski Sınıf')
        tree_gecmis.heading('yeni_sinif', text='Yeni Sınıf')
        tree_gecmis.heading('eski_ders', text='Eski Ders Saati')
        tree_gecmis.heading('yeni_ders', text='Yeni Ders Saati')
        tree_gecmis.heading('tarih', text='Tarih')
        tree_gecmis.heading('aciklama', text='Açıklama')
        
        for col in ['id', 'ogrenci', 'eski_sinif', 'yeni_sinif', 'eski_ders', 'yeni_ders', 'tarih', 'aciklama']:
            tree_gecmis.column(col, width=110)
        
        tree_gecmis.pack(fill='both', expand=True)

        refresh_transfer_gecmisi()

    def open_yonetici_raporu(self):
        win = tk.Toplevel(self)
        win.title('Yönetici Raporları')
        win.geometry('1100x700')

        notebook = ttk.Notebook(win)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Genel İstatistikler
        tab1 = tk.Frame(notebook)
        notebook.add(tab1, text='Genel İstatistikler')

        def refresh_istatistikler():
            stats = genel_istatistikler()
            label_toplam_ogrenci.config(text=f"Toplam Öğrenci: {stats['toplam_ogrenci']}")
            label_toplam_ogretmen.config(text=f"Toplam Öğretmen: {stats['toplam_ogretmen']}")
            label_toplam_sinif.config(text=f"Toplam Sınıf: {stats['toplam_sinif']}")
            
            for row in tree_ders_saati.get_children():
                tree_ders_saati.delete(row)
            for ders_saati, sayi in stats['ders_saati_dagilim']:
                tree_ders_saati.insert('', 'end', values=(f"{ders_saati} saat", sayi))

        # İstatistik kartları
        stats_frame = tk.Frame(tab1)
        stats_frame.pack(pady=20)
        
        label_toplam_ogrenci = tk.Label(stats_frame, text="Toplam Öğrenci: -", font=('Arial', 14, 'bold'), bg='lightblue', width=20)
        label_toplam_ogrenci.pack(side='left', padx=10, pady=5)
        
        label_toplam_ogretmen = tk.Label(stats_frame, text="Toplam Öğretmen: -", font=('Arial', 14, 'bold'), bg='lightgreen', width=20)
        label_toplam_ogretmen.pack(side='left', padx=10, pady=5)
        
        label_toplam_sinif = tk.Label(stats_frame, text="Toplam Sınıf: -", font=('Arial', 14, 'bold'), bg='lightyellow', width=20)
        label_toplam_sinif.pack(side='left', padx=10, pady=5)

        # Ders saati dağılımı
        dag_frame = tk.LabelFrame(tab1, text="Ders Saati Dağılımı", padx=10, pady=10)
        dag_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tree_ders_saati = ttk.Treeview(dag_frame, columns=('ders_saati', 'sayi'), show='headings', height=8)
        tree_ders_saati.heading('ders_saati', text='Ders Saati')
        tree_ders_saati.heading('sayi', text='Öğrenci Sayısı')
        
        tree_ders_saati.column('ders_saati', width=200)
        tree_ders_saati.column('sayi', width=200)
        
        tree_ders_saati.pack(expand=True, fill='both')

        # Sınıf Doluluk Raporu
        tab2 = tk.Frame(notebook)
        notebook.add(tab2, text='Sınıf Doluluk Raporu')

        def refresh_doluluk():
            for row in tree_doluluk.get_children():
                tree_doluluk.delete(row)
            for row in sinif_doluluk_raporu():
                tree_doluluk.insert('', 'end', values=row)

        def export_doluluk():
            data = []
            for item in tree_doluluk.get_children():
                data.append(tree_doluluk.item(item)['values'])
            
            if data:
                filename = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                    title="Doluluk Raporunu Kaydet"
                )
                if filename:
                    headers = ['Sınıf Adı', 'Kapasite', 'Mevcut Öğrenci', 'Doluluk Oranı (%)']
                    if csv_rapor_export(data, headers, filename):
                        messagebox.showinfo('Başarılı', f'Rapor başarıyla kaydedildi: {filename}')
                    else:
                        messagebox.showerror('Hata', 'Rapor kaydedilirken hata oluştu.')

        doluluk_frame = tk.LabelFrame(tab2, text='Sınıf Doluluk Oranları', padx=10, pady=10)
        doluluk_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_doluluk = ttk.Treeview(doluluk_frame, columns=('sinif', 'kapasite', 'mevcut', 'oran'), show='headings')
        tree_doluluk.heading('sinif', text='Sınıf Adı')
        tree_doluluk.heading('kapasite', text='Kapasite')
        tree_doluluk.heading('mevcut', text='Mevcut Öğrenci')
        tree_doluluk.heading('oran', text='Doluluk Oranı (%)')
        
        for col in ['sinif', 'kapasite', 'mevcut', 'oran']:
            tree_doluluk.column(col, width=200)
        
        tree_doluluk.pack(fill='both', expand=True)
        
        tk.Button(doluluk_frame, text='CSV Dışa Aktar', command=export_doluluk, bg='green', fg='white').pack(pady=10)

        # Öğretmen Atama Raporu
        tab3 = tk.Frame(notebook)
        notebook.add(tab3, text='Öğretmen Atama Raporu')

        def refresh_atamalar():
            for row in tree_atamalar.get_children():
                tree_atamalar.delete(row)
            for row in ogretmen_atama_raporu():
                tree_atamalar.insert('', 'end', values=row)

        def export_atamalar():
            data = []
            for item in tree_atamalar.get_children():
                data.append(tree_atamalar.item(item)['values'])
            
            if data:
                filename = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                    title="Atama Raporunu Kaydet"
                )
                if filename:
                    headers = ['Öğretmen', 'Branş', 'Atanan Sınıflar']
                    if csv_rapor_export(data, headers, filename):
                        messagebox.showinfo('Başarılı', f'Rapor başarıyla kaydedildi: {filename}')
                    else:
                        messagebox.showerror('Hata', 'Rapor kaydedilirken hata oluştu.')

        atama_frame = tk.LabelFrame(tab3, text='Öğretmen-Sınıf Atamaları', padx=10, pady=10)
        atama_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_atamalar = ttk.Treeview(atama_frame, columns=('ogretmen', 'brans', 'siniflar'), show='headings')
        tree_atamalar.heading('ogretmen', text='Öğretmen')
        tree_atamalar.heading('brans', text='Branş')
        tree_atamalar.heading('siniflar', text='Atanan Sınıflar')
        
        for col in ['ogretmen', 'brans', 'siniflar']:
            tree_atamalar.column(col, width=300)
        
        tree_atamalar.pack(fill='both', expand=True)
        
        tk.Button(atama_frame, text='CSV Dışa Aktar', command=export_atamalar, bg='green', fg='white').pack(pady=10)

        # Transfer Raporu
        tab4 = tk.Frame(notebook)
        notebook.add(tab4, text='Transfer Raporu')

        def refresh_transferler():
            for row in tree_transferler.get_children():
                tree_transferler.delete(row)
            for row in transfer_raporu():
                tree_transferler.insert('', 'end', values=row)

        def export_transferler():
            data = []
            for item in tree_transferler.get_children():
                data.append(tree_transferler.item(item)['values'])
            
            if data:
                filename = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                    title="Transfer Raporunu Kaydet"
                )
                if filename:
                    headers = ['Öğrenci', 'Eski Sınıf', 'Yeni Sınıf', 'Eski Ders Saati', 'Yeni Ders Saati', 'Tarih']
                    if csv_rapor_export(data, headers, filename):
                        messagebox.showinfo('Başarılı', f'Rapor başarıyla kaydedildi: {filename}')
                    else:
                        messagebox.showerror('Hata', 'Rapor kaydedilirken hata oluştu.')

        transfer_frame = tk.LabelFrame(tab4, text='Transfer İşlemleri Geçmişi', padx=10, pady=10)
        transfer_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tree_transferler = ttk.Treeview(transfer_frame, columns=('ogrenci', 'eski_sinif', 'yeni_sinif', 'eski_ders', 'yeni_ders', 'tarih'), show='headings')
        tree_transferler.heading('ogrenci', text='Öğrenci')
        tree_transferler.heading('eski_sinif', text='Eski Sınıf')
        tree_transferler.heading('yeni_sinif', text='Yeni Sınıf')
        tree_transferler.heading('eski_ders', text='Eski Ders Saati')
        tree_transferler.heading('yeni_ders', text='Yeni Ders Saati')
        tree_transferler.heading('tarih', text='Tarih')
        
        for col in ['ogrenci', 'eski_sinif', 'yeni_sinif', 'eski_ders', 'yeni_ders', 'tarih']:
            tree_transferler.column(col, width=150)
        
        tree_transferler.pack(fill='both', expand=True)
        
        tk.Button(transfer_frame, text='CSV Dışa Aktar', command=export_transferler, bg='green', fg='white').pack(pady=10)

        # Verileri yükle
        refresh_istatistikler()
        refresh_doluluk()
        refresh_atamalar()
        refresh_transferler()

if __name__ == '__main__':
    try:
        app = OkulYonetimApp()
        print("🚀 Özel Eğitim Okulu Yönetim Sistemi başlatıldı!")
        app.mainloop()
    except Exception as e:
        print(f"❌ Uygulama başlatma hatası: {e}")
        messagebox.showerror("Kritik Hata", f"Uygulama başlatılamadı: {e}")
