from fastapi import FastAPI
import seaborn as sns
import pandas as pd
from fastapi.responses import HTMLResponse
import matplotlib.pyplot as plt
import base64
from io import BytesIO


app = FastAPI()
df = sns.load_dataset("titanic")
#Perform a simple data transformation:
survival_rate = df.groupby("class")['survived'].mean().reset_index()
#Define the route:
@app.get("/")
async def root():
    return {"message": "This is a titanic web app route!"}
@app.get("/survival_rate")
async def get_survival_rate():
    return survival_rate.to_dict(orient="records")
#Create a rotue for survival rate plot:
@app.get("/survival_rate_plot", response_class=HTMLResponse)
async def get_survival_rate_plot():
    #fig, ax = plt.subplots()
    sns.barplot(x="class", y="survived", hue="sex",  data=df)
    #labels of plot:
    plt.title('Survival Rate by Class')
    plt.xlabel('Class')
    plt.ylabel('Survival Rate')
    #Save the plot to a bytes buffer:
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    # Encode the plot as a base64-encoded string:
    image_str = base64.b64encode(buf.getbuffer()).decode("utf-8")
    #Generate the HTML content:
    html_content = f'<img src="data:image/png;base64, {image_str}" alt="Survived Image">'
    return HTMLResponse(content=html_content)

