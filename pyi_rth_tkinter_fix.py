import os
import sys

# PyInstaller için Tkinter runtime düzeltmesi
if hasattr(sys, '_MEIPASS'):
    # PyInstaller paketlenmiş uygulama
    base_path = sys._MEIPASS
    
    # Tcl/Tk kütüphanelerinin konumlarını belirle
    tcl_lib = os.path.join(base_path, 'tcl', 'tcl8.6')
    tk_lib = os.path.join(base_path, 'tcl', 'tk8.6')
    
    # Alternatif konumlar
    if not os.path.exists(tcl_lib):
        tcl_lib = os.path.join(base_path, 'tcl8.6')
    if not os.path.exists(tk_lib):
        tk_lib = os.path.join(base_path, 'tk8.6')
        
    # Ortam değişkenlerini ayarla
    if os.path.exists(tcl_lib):
        os.environ['TCL_LIBRARY'] = tcl_lib
        print(f"TCL_LIBRARY set to: {tcl_lib}")
    else:
        print(f"TCL_LIBRARY path not found: {tcl_lib}")
        
    if os.path.exists(tk_lib):
        os.environ['TK_LIBRARY'] = tk_lib
        print(f"TK_LIBRARY set to: {tk_lib}")
    else:
        print(f"TK_LIBRARY path not found: {tk_lib}")
        
    # PATH'e tcl klasörünü ekle
    tcl_bin = os.path.join(base_path, 'tcl', 'bin')
    if os.path.exists(tcl_bin):
        os.environ['PATH'] = tcl_bin + os.pathsep + os.environ.get('PATH', '')
