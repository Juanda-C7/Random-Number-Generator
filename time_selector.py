# time_selector.py
from datetime import datetime

# Lista extensa de palabras y frases clave
keywords = [
    "acción", "aventura", "música", "deportes", "noticias", "gaming",
    "tecnología", "ciencia", "cocina", "arte", "películas", "series",
    "educación", "viajes", "naturaleza", "animales", "fitness", "yoga",
    "humor", "memes", "programación", "python", "javascript", "IA",
    "robótica", "historia", "astronomía", "física", "química", "matemáticas",
    "economía", "finanzas", "negocios", "marketing", "emprendimiento",
    "salud", "meditación", "relax", "música clásica", "rock", "pop",
    "rap", "jazz", "instrumental", "cultura", "política", "documentales",
    "tutoriales", "gaming tips", "estrategias", "animación 3D", "fotografía",
    "cine independiente", "viajes exóticos", "aventuras extremas",
    "DIY", "manualidades", "cómics", "anime", "manga", "series coreanas",
    "kpop", "ciencia ficción", "terror", "historia antigua", "historia moderna",
    "biología", "ecología", "medio ambiente", "startup", "tecnología verde",
    "innovación", "inteligencia artificial", "machine learning", "blockchain",
    "criptomonedas", "realidad virtual", "realidad aumentada", "drone",
    "fotografía nocturna", "viajes espaciales", "recetas saludables", "postres",
    "panadería", "fitness en casa", "yoga para principiantes", "meditación guiada"
]

def get_keyword_from_time():
    now = datetime.now()
    millis = now.microsecond // 1000
    index = (now.hour + now.minute + now.second + millis) % len(keywords)
    return keywords[index]
