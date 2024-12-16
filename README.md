
## Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

## Django Rest Framework API Client Test
```bash
python manage.py test
```

## Test It Using Curl
```
curl -X POST http://127.0.0.1:8000/user_api/users/ \
     -H "Content-Type: application/json" \
     -d '{"username":"OFBGAB1001","user_id":"XWSSGID-1253605895203984534550"}'
```