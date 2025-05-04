from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env

# Inicializamos el cliente con la API key desde la variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Plantilla de prompt optimizada
PROMPT_TEMPLATE = """\
Eres un mentor empático y experto en psicología y desarrollo personal.  
Tu misión es ayudarme, a conocerme mejor a través de mi historial emocional, para conortarme a mí mismo e incontrar mi proposito.

A continuación encontrarás una serie de mis registros con fecha, emoción y descripción del día:

{entries}

Por favor, genera **solo** un objeto JSON con estas claves, en este orden:

1. "analysis": Análisis psicológico detallado de los patrones emocionales y su posible origen.  
2. "positive_patterns": Lista de patrones positivos (explica por qué son valiosos).  
3. "negative_patterns": Lista de patrones negativos (sugiere cómo reducir su impacto).  
4. "strengths": Fortalezas y **cómo potenciarlas**.  
5. "weaknesses": Debilidades y **tips de mejora**.  
6. "opportunities": Oportunidades a aprovechar.  
7. "threats": Amenazas y **estrategias de mitigación**.  
8. "recommendations": Recomendaciones finales: pasos prácticos para potenciar habilidades, aportar valor y mantener el bienestar emocional.

El formato **debe ser exactamente**:

{{  
  "analysis": "...",  
  "positive_patterns": ["...", "..."],  
  "negative_patterns": ["...", "..."],  
  "strengths": "...",  
  "weaknesses": "...",  
  "opportunities": "...",  
  "threats": "...",  
  "recommendations": "..."  
}}  
"""

def generate_swot_from_records(text, debug=False):
    """
    Llama a la API de OpenAI para generar un análisis DOFA enriquecido.
    Si debug=True, devuelve la respuesta sin parsear para inspección.
    """
    prompt = PROMPT_TEMPLATE.format(entries=text)
    response = client.chat.completions.create(
        model="gpt-4",   # o "gpt-4o-mini" si lo tienes disponible
        messages=[
            {"role": "system", "content": "Devuelve únicamente un JSON con las claves indicadas, sin texto adicional."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    content = response.choices[0].message.content.strip()

    if debug:
        return content  # Para depuración

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"No pude parsear JSON de OpenAI:\n{content}")
