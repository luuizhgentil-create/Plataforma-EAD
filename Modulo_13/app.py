from flask import Flask, request, jsonify # pyright: ignore[reportMissingImports]
import sqlite3

app = Flask(__name__)

# Configura o banco de dados e cria a tabela ao iniciar
def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
    conn.commit()
    conn.close()

init_db()

# Atividade 1: Rota GET /saudacao
@app.route("/saudacao", methods=["GET"])
def saudacao():
    return jsonify({"mensagem": "Olá! Seja bem-vindo à API Flask."})

# Atividade 2 e 3: Rota POST /cadastrar com SQLite
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome_usuario = dados.get("nome")
    
    if not nome_usuario:
        return jsonify({"erro": "Nome é obrigatório"}), 400

    # Salva no banco SQLite
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome_usuario,))
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": f"Usuário {nome_usuario} cadastrado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
