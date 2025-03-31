import os
from PIL import Image

def limpiar_carpeta(carpeta):
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        try:
            if os.path.isfile(ruta):
                # Elimina si el archivo es muy pequeño
                if os.path.getsize(ruta) < 10 * 1024:
                    os.remove(ruta)
                    continue

                # Abre imagen y verifica dimensiones
                with Image.open(ruta) as img:
                    if img.size[0] < 100 or img.size[1] < 100:
                        os.remove(ruta)
        except:
            os.remove(ruta)

# Aplica limpieza a cada clase
for clase in ['ps4_controller', 'glasses', 'servo', 'doctor_strange']:
    limpiar_carpeta(f'dataset/{clase}')

print("🧹 Imágenes limpias.")
