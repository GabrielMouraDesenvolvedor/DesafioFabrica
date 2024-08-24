Instalação:

Clonar o Repositório:

git clone https://github.com/GabrielMouraDesenvolvedor/DesafioFabrica.git

cd DesafioFabrica

Criar e Ativas a VENV (Ambiente Virtual):

python -m venv venv

venv\Scripts\activate  # No Windows

source venv/bin/activate  # No macOS/Linux


Instale as Dependências:

pip install -r requirements.txt


Configure as Migrações do BD ( Banco de Dados):

python manage.py migrate


Crie um SuperUsuário (Opcional):

python manage.py createsuperuser

Inicie o Servidor de Desenvolvimento:

python manage.py runserver


ENDPOINTS

CRUD para Endtidades:

Author:
GET /api/authors/ - Lista todos os autores.
POST /api/authors/ - Cria um novo autor.
GET /api/authors/{id}/ - Recupera um autor específico.
PUT /api/authors/{id}/ - Atualiza um autor específico.
DELETE /api/authors/{id}/ - Deleta um autor específico.

Book:
GET /api/books/ - Lista todos os livros.
POST /api/books/ - Cria um novo livro.
GET /api/books/{id}/ - Recupera um livro específico.
PUT /api/books/{id}/ - Atualiza um livro específico.
DELETE /api/books/{id}/ - Deleta um livro específico.

Piada do Chuck Norris:
GET /api/chucknorris/joke/ - Retorna uma piada aleatória do Chuck Norris.
