# DiagnosisAPI

### A RESTful API that allows you utilize an internationally recognized set of diagnosis codes.

#### A User can 
- Create a new diagnosis code record
- Edit existing diagnosis code record
- Retrieve diagnosis codes 
- Delete diagnosis codes 
- Retrieve a single diagnosis code
- Upload ICD CSV files containing diagnosis codes 

##  Technologies 

* Python3
* Django
* Django Rest Framework
* PostgreSQL
* Docker



##  Setting Up

#### 1 - Clone repository
```
git clone https://github.com/ibrahimshittu/mPharmaBackendTest/
cd DiagnosisAPI
```

#### 2 - Building docker image
```
docker-compose build
```

#### 3 - Making Initial Migrations
```
docker-compose run web python manage.py migrate
```

#### 4 - Testing the Application
```
docker-compose run web python manage.py test
```

#### 5 - Load initial data fixtures
```
docker-compose run web python manage.py loaddata category.json
docker-compose run web python manage.py loaddata codes.json
```

#### 6 - Running the Application
```
docker-compose up 
```

##  Documentation 

The documentation can be accessed via Swagger, ReDoc or importing the api in json format to Postman

* Swagger Documentation
```http://127.0.0.1/docs/```
* ReDoc Documentation
```http://127.0.0.1/redoc/```
* JSON API 
```http://127.0.0.1/api_json/```

