from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# 1. Configuração do MongoDB (substitua pela sua string)
MONGO_URI = "mongodb+srv://<<user>>:<<credencial>>@esp32.9igsjch.mongodb.net/?appName=Esp32"


client = MongoClient(MONGO_URI)
db = client.Esp32
colecao = db.leituras_umidade

app = Flask(__name__)

@app.route('/api/leitura', methods=['POST'])
def receber_leitura():
    # Recebe os dados JSON do ESP32
    dados = request.get_json()

    if not dados or 'umidade' not in dados or 'temperatura' not in dados:
        return jsonify({"status": "erro", "mensagem": "Dados incompletos"}), 400


    try:
        # Prepara o documento para o MongoDB
        documento = {            
            "Setor": dados['Setor'],           
            "umidade": float(dados['umidade']),
            "temperatura": float(dados['temperatura']),
            "timestamp": datetime.utcnow()
        }

        # Insere no MongoDB
        colecao.insert_one(documento)

        return jsonify({"status": "sucesso", "mensagem": "Dados salvos"}), 201

    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return jsonify({"status": "erro", "mensagem": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    # Execute em um servidor acessível pelo ESP32
    # Use host='0.0.0.0' para que seja acessível externamente
    app.run(host='0.0.0.0', port=5000)