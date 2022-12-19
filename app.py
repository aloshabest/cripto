import fastapi


api = fastapi.FastAPI()

response = {"Ответ": "Который возвращает сервер"}

@api.get('/')
def index():
    return response

@api.get('/hello')
def hello():
    return "hello"

@api.get('/about/us')
def about():
    return {"we are": "legion"}