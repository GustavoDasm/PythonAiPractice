from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd

app = FastAPI()

class Datos(BaseModel):
    input: str
    
@app.get("/api/data/csv")
async def get_data_csv():
    num_rows = 10
    data = {
        "A": np.random.rand(num_rows),
        "B": np.random.randint(0, 100, num_rows),
        "C": np.random.choice(['X', 'Y', 'Z'], num_rows)
    }   
    
    df = pd.DataFrame(data)
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)    