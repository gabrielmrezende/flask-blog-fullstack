# 📝 Flask Blog Full Stack

Aplicação web Full Stack desenvolvida com **Python**, **Flask**, **HTML**, **Bootstrap** e **banco de dados**, com o objetivo de praticar a construção de aplicações web completas integrando frontend e backend.

Projeto desenvolvido durante um curso de Desenvolvimento Web com Python para fins educacionais e de portfólio.

---

# 🚀 Funcionalidades

* Cadastro de usuários
* Login e logout com sessão persistente
* Criação de posts
* Edição de posts pelo próprio autor
* Exclusão de posts
* Edição de perfil (nome, e-mail e foto)
* Upload e redimensionamento de foto de perfil
* Seleção de cursos no perfil do usuário
* Listagem de todos os usuários cadastrados
* Banco de dados integrado (SQLite local / PostgreSQL em produção)
* Interface responsiva com Bootstrap

---

# 🛠️ Tecnologias Utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Bcrypt
* Flask-WTF / WTForms
* Pillow (manipulação de imagens)
* SQLAlchemy
* SQLite (desenvolvimento) / PostgreSQL (produção)
* Gunicorn
* HTML
* CSS
* Bootstrap
* JavaScript

---

# 📚 O que Aprendi

* Estrutura de aplicações web com Flask usando Application Factory e Blueprint-style
* Integração entre frontend e backend
* Autenticação de usuários com hash de senha (Bcrypt)
* Gerenciamento de sessão com Flask-Login
* Manipulação de banco de dados com SQLAlchemy (CRUD completo)
* Upload e processamento de imagens com Pillow
* Validação de formulários com WTForms
* Suporte a ambiente de produção com PostgreSQL e Gunicorn
* Organização de projetos em pacotes Python
* Uso do Git e GitHub para versionamento

---

# 📂 Estrutura do Projeto

```
/Projeto Flask Hashtag
│
├── main.py                         # Ponto de entrada da aplicação
├── criar_banco.py                  # Script auxiliar para criação do banco
├── requirements.txt                # Dependências do projeto
├── Procfile                        # Configuração para deploy (Gunicorn)
├── README.md
│
└── comunidadeimpressionadora/      # Pacote principal da aplicação
    ├── __init__.py                 # Configuração do app, banco e extensões
    ├── models.py                   # Modelos do banco (Usuario, Post)
    ├── forms.py                    # Formulários WTForms
    ├── routes.py                   # Rotas e lógica de negócio
    │
    ├── templates/                  # Templates HTML (Jinja2)
    │   ├── base.html
    │   ├── navbar.html
    │   ├── home.html
    │   ├── login.html
    │   ├── perfil.html
    │   ├── editarperfil.html
    │   ├── criarpost.html
    │   ├── post.html
    │   ├── usuarios.html
    │   └── contato.html
    │
    └── static/                     # Arquivos estáticos
        ├── main.css
        └── fotos_perfil/           # Fotos de perfil dos usuários
```

---

# ▶️ Como Rodar o Projeto

1. Clone o repositório

```
git clone https://github.com/seu-usuario/flask-blog.git
```

2. Entre na pasta

```
cd flask-blog
```

3. Crie um ambiente virtual

```
python -m venv venv
```

4. Ative o ambiente virtual

```
venv\\Scripts\\activate
```

5. Instale as dependências

```
pip install -r requirements.txt
```

6. Rode o projeto

```
python main.py
```

---

# 👨‍💻 Autor

Gabriel Rezende
Estudante de Ciência da Computação
Apaixonado por desenvolvimento web, IA e projetos full stack 🚀

---

# ⭐ Contribuições

Sugestões e melhorias são bem-vindas! Abra uma issue ou pull request.
