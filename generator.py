import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generar_posts(tema, red_social, tono):

    instrucciones = {
        "LinkedIn": "Posts de 150-300 palabras. Empezá con un gancho fuerte en la primera línea (algo que genere curiosidad o impacto). Usá saltos de línea para que sea fácil de leer. Incluí una pregunta al final para generar comentarios. Sin hashtags en exceso, máximo 3 al final.",
        "Twitter": "Tweets de máximo 280 caracteres cada uno. Directos, con impacto inmediato. Podés usar hilos si el tema lo requiere. Máximo 2 hashtags.",
        "Instagram": "Captions de 100-200 palabras. Empezá con una frase que detenga el scroll. Tono más personal y cercano. Usá emojis estratégicamente. Incluí un call to action claro al final. Hashtags relevantes al final (5-8)."
    }

    tonos = {
        "Profesional": "Autoridad y credibilidad. Datos concretos cuando sea posible. Sin frases vacías ni clichés. Directo al punto.",
        "Casual": "Como si le hablaras a un amigo. Natural, cercano, sin tecnicismos. Que se sienta humano.",
        "Divertido": "Con humor inteligente, ironía sutil o una perspectiva inesperada. Que sorprenda."
    }

    prompt = f"""
Sos un experto en copywriting y marketing de contenidos con 10 años de experiencia creando contenido viral.

Tu tarea: generá 3 posts DISTINTOS entre sí para {red_social} sobre este tema: "{tema}"

Tono: {tonos[tono]}
Formato: {instrucciones[red_social]}

Reglas críticas:
- Cada post debe tener un ángulo DIFERENTE del tema (no repitas la misma idea con otras palabras)
- Evitá frases genéricas como "En el mundo actual", "Es importante destacar", "Sin lugar a dudas"
- Cada post debe aportar valor real: un dato, una perspectiva nueva, un consejo accionable, o una historia
- Escribí en español neutro, natural, que suene humano
- Separá cada post con exactamente "---"
- Empezá cada post con "POST 1:", "POST 2:", "POST 3:"
- No agregues explicaciones ni comentarios fuera de los posts
"""

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Sos un experto en copywriting y creación de contenido para redes sociales. Generás contenido de alto valor, original y adaptado a cada plataforma."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.85,
        max_tokens=2000
    )

    return respuesta.choices[0].message.content