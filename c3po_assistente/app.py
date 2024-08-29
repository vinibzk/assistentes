from flask import Flask, render_template, request, jsonify
from models.your_nlp_model import predict_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    resposta = predict_response(user_input)  # Usa o modelo para prever a resposta
    return jsonify({"response": resposta})

if __name__ == '__main__':
    app.run(debug=True)
