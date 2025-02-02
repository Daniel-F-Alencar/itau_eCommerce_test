# 🛒 E-commerce Inventory API
RESTful API para gerenciar o inventário de produtos de um e-commerce.  
Desenvolvida com **Flask**, **SQLAlchemy**, **JWT Authentication** e **MySQL**.  

## 📌 Tecnologias Utilizadas
- **Flask** (Backend)
- **Flask-SQLAlchemy** (ORM)
- **Flask-Migrate** (Migrações do Banco)
- **Flask-JWT-Extended** (Autenticação JWT)
- **MySQL** (Banco de Dados)
- **Faker-Commerce** (Dados Mock)
- **Postman/cURL** (Testes de API)

---

## 📦 Instalação e Configuração

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/ecommerce-inventory.git
cd ecommerce-inventory
```

### 2️⃣ Criar um Ambiente Virtual
```sh
python -m venv venv
```
Ativar no **Windows**:
```sh
venv\Scripts\activate
```
Ativar no **Mac/Linux**:
```sh
source venv/bin/activate
```

### 3️⃣ Instalar Dependências
```sh
pip install -r requirements.txt
```

---

## 🛢 Configuração do Banco de Dados
1. **Instale o MySQL Community Server** (se ainda não tiver).
2. **Crie o banco de dados manualmente** no MySQL:
```sql
CREATE DATABASE ecommerce_db;
```
3. **Edite `config.py` e atualize com suas credenciais do MySQL:**
```python
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:SUA_SENHA@localhost/ecommerce_db'
```
4. Caso o servidor não esteja rodando, utilize o comando "net start MySQL80" para iniciar o servidor.
---

## 🔄 Criar Estrutura do Banco
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## 🛠 Populando o Banco com Dados Mock
Para gerar **30 produtos fictícios** no banco:
```sh
python seed.py
```

---

## 🚀 Rodando a API
```sh
python run.py
```
A API estará disponível em **http://127.0.0.1:5000/**.

---

## 📝 Endpoints da API

### 1️⃣ Autenticação
#### 🔹 Registrar um Usuário
```http
POST /api/auth/register
```
📌 **Body (JSON):**
```json
{
    "name": "John Doe",
    "username": "johndoe",
    "password": "password123"
}
```

#### 🔹 Login (Gerar Token JWT)
```http
POST /api/auth/login
```
📌 **Body (JSON):**
```json
{
    "username": "johndoe",
    "password": "password123"
}
```
📌 **Resposta (200 OK):**
```json
{
    "access_token": "eyJ0eXA...<TOKEN>"
}
```
**⚠ Copie esse `access_token` para usar nas próximas requisições protegidas!**  

---

### 2️⃣ Produtos
#### 🔹 Listar Todos os Produtos
```http
GET /api/products/
```

#### 🔹 Buscar Produto por ID
```http
GET /api/products/{id}
```

#### 🔹 Criar um Produto (JWT Required)
```http
POST /api/products/
```
📌 **Body (JSON):**
```json
{
    "name": "Smartphone",
    "description": "High-end smartphone",
    "price": 999.99,
    "stock": 20
}
```
📌 **Header:**
```
Authorization: Bearer <TOKEN>
```

#### 🔹 Atualizar Produto (JWT Required)
```http
PUT /api/products/{id}
```
📌 **Body (JSON):**
```json
{
    "price": 899.99,
    "stock": 10
}
```

#### 🔹 Deletar Produto (JWT Required)
```http
DELETE /api/products/{id}
```

---

## 📌 Testando no Postman
1. **Abra o Postman**  
2. **Importe as Requisições** via `cURL` ou crie-as manualmente  
3. **Autentique-se e use o Token** nos endpoints protegidos  

---

## 🛠 Possíveis Erros e Soluções
🔴 **Erro `ECONNREFUSED 127.0.0.1:5000`?**  
✅ **Certifique-se de que o Flask está rodando** (`python run.py`)  

🔴 **Erro `Access Denied` no MySQL?**  
✅ **Verifique o usuário e senha do MySQL no `config.py`**  

