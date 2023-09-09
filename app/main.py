from fastapi import FastAPI


app = FastAPI()

def get_application():
    _app = FastAPI()

    return _app

app = get_application()

@app.get("/")
def get_articles():
    return {'message': "hello world"}