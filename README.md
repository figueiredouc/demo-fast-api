# FastAPI Demo - Sistema de Sensores com Autenticação JWT e Admin

Uma aplicação FastAPI completa com autenticação JWT, gerenciamento de sensores e interface administrativa (SQLAdmin).

## 🚀 Funcionalidades

- ✅ **Autenticação JWT** via `fastapi-users`
- ✅ **Endpoints de Sensores**: listagem e detalhes
- ✅ **Backoffice (SQLAdmin)**: interface administrativa com CRUD de sensores
- ✅ **Arquitetura Rails-like**: controllers, presenters, repositories, services
- ✅ **Testes**: specs para o controller de sensores
- ✅ **Docker**: containerização completa com PostgreSQL
- ✅ **Migrações**: Alembic para gerenciamento de schema

## 📋 Tecnologias


- **Python 3.12**
- **FastAPI 0.128.0**
- **SQLAlchemy 2.0.45** (sync)
- **PostgreSQL 16**
- **fastapi-users 15.0.3** (autenticação JWT)
- **SQLAdmin 0.22.0** (interface administrativa)
- **Alembic 1.17.2** (migrações)
- **pytest 8.3.3** (testes)

## 📁 Estrutura do Projeto

```
fast-api-demo/
├── app/
│   ├── admin/              # SQLAdmin views
│   │   └── admin.py
│   ├── api/
│   │   ├── controllers/    # Controllers da API
│   │   │   ├── sensors_controller.py
│   │   │   └── users_controller.py
│   │   ├── dependencies.py
│   │   └── routes.py       # Rotas principais
│   ├── core/               # Configuração core
│   │   ├── config.py       # Settings
│   │   ├── db.py           # Database connection
│   │   └── security.py     # JWT authentication
│   ├── migrations/         # Alembic migrations
│   ├── models/             # SQLAlchemy models
│   │   ├── base.py
│   │   ├── sensor.py
│   │   └── user.py
│   ├── presenters/         # Presenters para serialização
│   │   └── sensor_presenter.py
│   ├── repositories/       # Data access layer
│   │   └── sensor_repository.py
│   ├── schemas/            # Pydantic schemas
│   │   ├── sensor.py
│   │   └── user.py
│   └── services/           # Business logic
│       └── sensor_service.py
├── tests/                  # Testes
│   └── test_sensors_controller.py
├── .env                    # Variáveis de ambiente (não versionado)
├── .env.example            # Exemplo de variáveis de ambiente
├── alembic.ini             # Configuração Alembic
├── docker-compose.yml      # Orquestração Docker
├── Dockerfile              # Imagem da aplicação
├── main.py                 # Entry point
├── requirements.txt        # Dependências Python
└── README.md
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Docker e Docker Compose
- Python 3.12+ (para desenvolvimento local)

### 1. Clone o repositório

```bash
git clone <repository-url>
cd fast-api-demo
```

### 2. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o `.env` com suas configurações:

```env
ENV=development
DATABASE_URL=postgresql+psycopg://app:app@db:5432/app
SECRET_KEY=change-me-to-a-secure-secret-key
JWT_LIFETIME_MINUTES=60
SUPERUSER_EMAIL=admin@example.com
SUPERUSER_PASSWORD=admin123
```

**⚠️ Importante**: Altere o `SECRET_KEY` para um valor seguro em produção!

### 3. Execute as migrações

```bash
# Inicie apenas o banco de dados
docker compose up -d db

# Execute as migrações
docker compose run --rm api alembic upgrade head
```

### 4. Inicie a aplicação

```bash
docker compose up --build
```

A aplicação estará disponível em:
- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Admin**: http://localhost:8000/admin

## 📚 Endpoints da API

### Autenticação

#### Login (JWT)
```http
POST /v1/auth/jwt/login
Content-Type: application/x-www-form-urlencoded

username=admin@example.com&password=admin123
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Registro
```http
POST /v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

### Sensores

#### Listar todos os sensores
```http
GET /v1/sensors/
```

**Resposta:**
```json
[
  {
    "id": 1,
    "name": "Temp-01",
    "kind": "temperature",
    "is_active": true
  }
]
```

#### Detalhes de um sensor
```http
GET /v1/sensors/{id}
```

**Resposta:**
```json
{
  "id": 1,
  "name": "Temp-01",
  "kind": "temperature",
  "is_active": true,
  "location": "Lab"
}
```

## 🔐 Autenticação

Para usar endpoints protegidos, inclua o token JWT no header:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Exemplo no Postman

1. **Login**:
   - Método: `POST`
   - URL: `http://localhost:8000/v1/auth/jwt/login`
   - Body (x-www-form-urlencoded):
     - `username`: `admin@example.com`
     - `password`: `admin123`

2. **Copie o `access_token`** da resposta

3. **Use em requisições autenticadas**:
   - Aba Authorization → Type: Bearer Token
   - Cole o token

## 🎛️ Interface Administrativa (SQLAdmin)

Acesse: http://localhost:8000/admin

- **Login**: Use as credenciais do superusuário configuradas no `.env`
- **Funcionalidades**:
  - CRUD completo de Sensores
  - Visualização de Usuários
  - Interface web intuitiva

## 🧪 Testes

Execute os testes:

```bash
# Com Docker
docker compose run --rm api pytest

# Localmente (com venv ativado)
pytest
```

### Estrutura de Testes

Os testes estão em `tests/test_sensors_controller.py` e cobrem:
- Listagem vazia de sensores
- Listagem com múltiplos sensores
- Detalhes de um sensor específico
- Tratamento de erro 404

## 🔄 Migrações (Alembic)

### Criar uma nova migração

```bash
docker compose run --rm api alembic revision --autogenerate -m "descrição da migração"
```

### Aplicar migrações

```bash
docker compose run --rm api alembic upgrade head
```

### Reverter migração

```bash
docker compose run --rm api alembic downgrade -1
```

## 🏗️ Arquitetura

O projeto segue uma arquitetura inspirada em Rails, com separação clara de responsabilidades:

- **Models**: Definição dos modelos SQLAlchemy
- **Repositories**: Camada de acesso a dados
- **Services**: Lógica de negócio
- **Controllers**: Endpoints da API
- **Presenters**: Serialização de dados para resposta
- **Schemas**: Validação e serialização Pydantic

## 🔧 Desenvolvimento Local

### Setup do ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Executar localmente (sem Docker)

1. Configure o `.env` com `DATABASE_URL` apontando para um PostgreSQL local:
   ```env
   DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/dbname
   ```

2. Execute as migrações:
   ```bash
   alembic upgrade head
   ```

3. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

## 📝 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|-------|
| `ENV` | Ambiente (development/production) | `development` |
| `DATABASE_URL` | URL de conexão PostgreSQL | - |
| `SECRET_KEY` | Chave secreta para JWT | - |
| `JWT_LIFETIME_MINUTES` | Tempo de vida do token JWT (minutos) | `60` |
| `SUPERUSER_EMAIL` | Email do superusuário inicial | `admin@example.com` |
| `SUPERUSER_PASSWORD` | Senha do superusuário inicial | `admin123` |

## 🐳 Docker

### Comandos úteis

```bash
# Construir e iniciar
docker compose up --build

# Executar em background
docker compose up -d

# Ver logs
docker compose logs -f api

# Parar containers
docker compose down

# Parar e remover volumes
docker compose down -v

# Executar comando no container
docker compose exec api <comando>
```

## 📦 Dependências Principais

- **fastapi**: Framework web moderno e rápido
- **sqlalchemy**: ORM para Python
- **fastapi-users**: Sistema de autenticação completo
- **sqladmin**: Interface administrativa
- **alembic**: Ferramenta de migração de banco de dados
- **pydantic**: Validação de dados
- **pytest**: Framework de testes

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

Desenvolvido como demo de FastAPI com arquitetura Rails-like.

---

**Nota**: Este é um projeto de demonstração. Para uso em produção, considere:
- Configurar HTTPS
- Usar variáveis de ambiente seguras
- Implementar rate limiting
- Adicionar logging adequado
- Configurar CORS apropriadamente
- Implementar backup do banco de dados
