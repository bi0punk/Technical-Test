

## Manual Build 

```bash
> 👉 Install **Django** modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
<br>
> 👉 Migrate DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

```bash
$ python manage.py runserver       # start the project
```
<br>
>  👉 Documentation

```bash
http://127.0.0.1:8000/api/schema/swagger-ui/
http://127.0.0.1:8000/api/schema/redoc/
```
<br>
> 👉Endpoints

```bash
Aquí están los endpoints de la API y los comandos para probarla utilizando curl y httpie:

### Endpoints de la API

Categorías (CRUD)
-   Listar todas las categorías: GET /api/categories/
-   Crear una nueva categoría: POST /api/categories/
-   Obtener una categoría específica: GET /api/categories/{id}/
-   Actualizar una categoría: PUT /api/categories/{id}/
-   Borrar una categoría: DELETE /api/categories/{id}/

Comercios (CRUD)
-   Listar todos los comercios: GET /api/merchants/
-   Crear un nuevo comercio: POST /api/merchants/
-   Obtener un comercio específico: GET /api/merchants/{id}/
-   Actualizar un comercio: PUT /api/merchants/{id}/
-   Borrar un comercio: DELETE /api/merchants/{id}/
    

Keywords (CRUD)
-   Listar todas las keywords: GET /api/keywords/
-   Crear una nueva keyword: POST /api/keywords/
-   Obtener una keyword específica: GET /api/keywords/{id}/
-   Actualizar una keyword: PUT /api/keywords/{id}/
-   Borrar una keyword: DELETE /api/keywords/{id}/


Transacciones (CRUD y enriquecimiento)
-   Listar todas las transacciones: GET /api/transactions/
-   Crear una nueva transacción: POST /api/transactions/
-   Obtener una transacción específica: GET /api/transactions/{id}/
-   Actualizar una transacción: PUT /api/transactions/{id}/
-   Borrar una transacción: DELETE /api/transactions/{id}/
-   Enriquecer transacciones: POST /api/transactions/enrich/
```
<br>

### Comandos para probar la API utilizando curl

#### **Categorías**

**Listar todas las categorías**
curl -X GET http://localhost:8000/api/categories/

**Crear una nueva categoría**
curl -X POST http://localhost:8000/api/categories/ -H "Content-Type: application/json" -d '{"name": "Restaurantes", "type": "expense"}'

**Obtener una categoría específica**
curl -X GET http://localhost:8000/api/categories/{id}/

**Actualizar una categoría**
curl -X PUT http://localhost:8000/api/categories/{id}/ -H "Content-Type: application/json" -d '{"name": "Comida", "type": "expense"}'

**Borrar una categoría**
curl -X DELETE http://localhost:8000/api/categories/{id}/

#### **Comercios**

**Listar todos los comercios**
curl -X GET http://localhost:8000/api/merchants/

**Crear un nuevo comercio**
curl -X POST http://localhost:8000/api/merchants/ -H "Content-Type: application/json" -d '{"merchant_name": "Uber Eats", "merchant_logo": "http://logo.url", "category": "{category_id}"}'

**Obtener un comercio específico**
curl -X GET http://localhost:8000/api/merchants/{id}/

**Actualizar un comercio**
curl -X PUT http://localhost:8000/api/merchants/{id}/ -H "Content-Type: application/json" -d '{"merchant_name": "Uber", "merchant_logo": "http://newlogo.url", "category": "{category_id}"}'

**Borrar un comercio**
curl -X DELETE http://localhost:8000/api/merchants/{id}/

#### **Keywords**

**Listar todas las keywords**
curl -X GET http://localhost:8000/api/keywords/

**Crear una nueva keyword**
curl -X POST http://localhost:8000/api/keywords/ -H "Content-Type: application/json" -d '{"keyword": "uber eats", "merchant": "{merchant_id}"}'

**Obtener una keyword específica**
curl -X GET http://localhost:8000/api/keywords/{id}/

**Actualizar una keyword**
curl -X PUT http://localhost:8000/api/keywords/{id}/ -H "Content-Type: application/json" -d '{"keyword": "uber", "merchant": "{merchant_id}"}'

**Borrar una keyword**
curl -X DELETE http://localhost:8000/api/keywords/{id}/

#### **Transacciones**

**Listar todas las transacciones**
curl -X GET http://localhost:8000/api/transactions/

**Crear una nueva transacción**
curl -X POST http://localhost:8000/api/transactions/ -H "Content-Type: application/json" -d '{"description": "PYU *UberEats", "amount": -300.00, "date": "2023-12-01"}'

**Obtener una transacción específica**
curl -X GET http://localhost:8000/api/transactions/{id}/

**Actualizar una transacción**
curl -X PUT http://localhost:8000/api/transactions/{id}/ -H "Content-Type: application/json" -d '{"description": "PYU *Uber", "amount": -250.00, "date": "2023-12-01"}'

**Borrar una transacción**
curl -X DELETE http://localhost:8000/api/transactions/{id}/

**Enriquecer transacciones**
curl -X POST http://localhost:8000/api/transactions/enrich/ -H "Content-Type: application/json" -d '{"transactions": [{"id": "d1c0bd75-1aee-4901-9ef9-2a7897518e16", "description": "PETROBRAS 11 ORTE/7 SU", "amount": -100.00, "date": "2023-12-01"}]}'


## Codebase 

```bash
< PROJECT ROOT >
.
├── api_enrichment
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── templates
│   │   └── transaction_list.html
│   ├── tests.py
│   └── views.py
├── api_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── test_script
│   ├── data.csv
│   └── loaddata.py
└── tree.txt 
```   

<br />

