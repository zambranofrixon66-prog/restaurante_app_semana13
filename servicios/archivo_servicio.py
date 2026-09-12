import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta_relativa):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_absoluta = os.path.join(base_dir, ruta_relativa)
        
        if not os.path.exists(ruta_absoluta):
            return []
        
        try:
            with open(ruta_absoluta, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except Exception:
            return []