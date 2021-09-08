from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def drawing():
    return {"message": "This is the Drawing room"}
 
@app.get("/bedroom/{id}")
def bedroom(id: int):
    return {"message": f"This is the Bedroom{id}"}

@app.get("/bedroom")
def master_bedroom():
    return {"message": "This is the Master Bedroom"}

@app.get("/personal_info/{name}_{age}_{birth_place}")
def info(name, age, birth_place):
    return {"name":{name}, 
    "age": {age}, 
    "Birth_place": birth_place}
