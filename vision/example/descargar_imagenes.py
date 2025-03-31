import os
from icrawler.builtin import GoogleImageCrawler

objetos = {
    'ps4_controller': 'PlayStation 4 controller',
    'glasses': 'eyeglasses',
    'servo': 'servo motor',
    'doctor_strange': 'Doctor Strange action figure'
}

base_dir = 'dataset'

max_images = 100

# Crear carpeta base si no existe
os.makedirs(base_dir, exist_ok=True)

# Descargar imágenes por cada clase
for clase, keyword in objetos.items():
    save_dir = os.path.join(base_dir, clase)
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"\n🔍 Buscando imágenes de: {keyword}")
    crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    crawler.crawl(keyword=keyword, max_num=max_images)

print("\n✅ Descarga finalizada. Revisa la carpeta 'dataset'.")
