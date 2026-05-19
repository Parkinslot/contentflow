import os
from groq import Groq
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Conecta con Groq usando tu API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generar_posts(tema, red_social, tono):
    """
    Genera 3 posts para redes sociales.
    
    tema        → de qué trata el post (ej: "beneficios del trabajo remoto")
    red_social  → LinkedIn, Twitter o Instagram
    tono        → profesional, casual o divertido
    """

    prompt = f"""
    Eres un experto en marketing de contenidos y redes sociales.
    
    Genera exactamente 3 posts para {red_social} sobre el siguiente tema: "{tema}"
    
    Tono: {tono}
    
    Reglas:
    - Cada post debe estar separado por una línea con "---"
    - Cada post debe empezar con "POST 1:", "POST 2:", "POST 3:"
    - Adaptá el largo al formato de {red_social}
    - Incluí emojis si corresponde al tono
    - Escribí en español
    - Solo devolvé los 3 posts, sin explicaciones extra
    """

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return respuesta.choices[0].message.content