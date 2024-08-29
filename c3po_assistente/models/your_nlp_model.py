import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Baixar recursos necessários do NLTK (apenas na primeira vez)
nltk.download('punkt')

# Treinamento de exemplo
def train_model():
    # Exemplos de comandos e respostas correspondentes
    training_data = {
        "olá, oi, saudações": "Olá! Como posso ajudar você hoje?",
        "tchau, adeus": "Até mais! Tenha um ótimo dia!",
        "qual é o seu nome, quem é você": "Eu sou seu assistente virtual!"
    }
    
    # Preparar dados para treinamento
    sentences = []
    labels = []
    
    for keys, response in training_data.items():
        for key in keys.split(","):
            sentences.append(key.strip())
            labels.append(response)
    
    # Vetorização TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    # Treinamento do modelo de regressão logística
    model = LogisticRegression()
    model.fit(X, labels)
    
    # Salvar o modelo treinado e o vetor TF-IDF
    with open('models/nlp_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    
    with open('models/vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)

# Função para prever a resposta
def predict_response(user_input):
    # Carregar o modelo e o vetor
    model_path = 'models/nlp_model.pkl'
    vectorizer_path = 'models/vectorizer.pkl'
    
    if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
        train_model()  # Treina o modelo se ele não existir
        
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
        
    with open(vectorizer_path, 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    
    # Vetorizar a entrada do usuário
    user_input_vect = vectorizer.transform([user_input])
    
    # Predizer a resposta
    response = model.predict(user_input_vect)
    
    return response[0]

if __name__ == "__main__":
    # Treinamento do modelo na primeira execução
    train_model()
    # Teste rápido
    print(predict_response("Olá"))
    print(predict_response("qual é o seu nome"))
    print(predict_response("tchau"))
