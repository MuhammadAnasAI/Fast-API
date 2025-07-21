from fastapi import FastAPI, HTTPException
import seaborn as sns
import pandas as pd
from fastapi.responses import HTMLResponse
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.io import to_html



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
@app.get("/survival_rate_plotly", response_class=HTMLResponse)
async def get_survival_rate_plotly():
    #plot the dataset:
    fig = px.bar(df, x="class", y="survived", color="sex")
    #Convert the plot into the html:
    html = to_html(fig, full_html=False)
    #Create the full html document:
    full_html = f"""
    <html>
    <head>
    <title>Survival Rate Plot</title>
    </head>
    <body>
    <h1>Survival Rate Plot</h1>
    {html}
    </body>
    </html>
    """
    return HTMLResponse(content=full_html)
#Specify the ports to run the app at 5000:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
                