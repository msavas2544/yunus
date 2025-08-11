from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    # 32x32 icon oluştur
    icon_size = 32
    img = Image.new('RGBA', (icon_size, icon_size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Mavi renkte "E" harfi çiz (Eğitim için)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    # "E" harfini merkeze yerleştir
    text = "E"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (icon_size - text_width) // 2
    y = (icon_size - text_height) // 2
    
    draw.text((x, y), text, fill=(0, 0, 255, 255), font=font)
    
    # ICO dosyası olarak kaydet
    img.save('app_icon.ico', 'ICO')
    print("Uygulama ikonu oluşturuldu: app_icon.ico")

if __name__ == "__main__":
    create_app_icon()
