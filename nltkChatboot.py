import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Baixe recursos necessários do NLTK (faça isso uma vez)
nltk.download('punkt')
nltk.download('stopwords')

# Defina intenções e respostas
intents = {
    "oi": "Olá! Como posso ajudar você?",
    "como_esta": "Estou bem, obrigado por perguntar.",
    "adeus": "Até logo! Qualquer outra dúvida, estou aqui.",
}

# Pré-processamento de Dados
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(tokens)

# Entrada do usuário
user_input = input("Usuário: ")

# Processamento de Intenções
preprocessed_input = preprocess(user_input)
intent = None
for key in intents.keys():
    if key in preprocessed_input:
        intent = key
        break

# Gerar resposta
if intent:
    print("Assistente:", intents[intent])
else:
    print("Assistente: Desculpe, não entendi sua pergunta.")
