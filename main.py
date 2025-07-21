from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, I am a Data Scientist working on the Artificial Intelligence."}
@app.post("/")
async def post_root():
    return {"message": "Hello, I am an expert in Artficial Intelligence."}
@app.put("/{item_id}")
async def put_item(item_id: int):
    return{"message": f"item ID is {item_id}"}
