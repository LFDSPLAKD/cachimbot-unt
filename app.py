from flask import Flask, request, jsonify
import google.generativeai as ai
import os

app = Flask(__name__)

# Configuración de la API de Google Gemini
API_KEY = 'AIzaSyCip740g0Wl2SEshz-8SkkO_9YfISoo5cI'  # Asegúrate de tener tu API Key aquí
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Mensaje inicial para definir el rol del chatbot
initial_system_message = """
Eres un chatbot universitario para la Universidad Nacional de Trujillo (UNT).
Ayudas a estudiantes de primer ciclo ("cachimbos") con preguntas sobre:
- Dónde queda su facultad
- Cómo matricularse
- Cómo obtener o renovar el carnet universitario
Responde siempre con claridad y cordialidad.
"""
chat.send_message(initial_system_message)

@app.route('/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "No recibí ningún mensaje."})
    response = chat.send_message(user_message)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto asignado por Render o 5000 local
    app.run(host='0.0.0.0', port=port)       # Escucha en todas las interfaces
