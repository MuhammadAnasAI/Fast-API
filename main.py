from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, I am a Data Scientist working on the Artificial Intelligence."}
@app.post("/")
async def post_root():
    return {"message": "Hello, I am an expert in Artficial Intelligence."}
#@app.put("/{item_id}")
#async def put_item(item_id: int):
 #   return{"message": f"item ID is {item_id}"}
#Add a path parameter:
@app.get("/items")
async def get_items():
    return {"message": "This is an item_id"}
#Check the path Parameters for the Items:
@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id": item_id}
#Check tht path parameters for the Users:
@app.get("/users/{user_id}")
async def get_item(user_id):
    return {"item_id": user_id}