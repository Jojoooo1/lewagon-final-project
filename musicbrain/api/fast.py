import io
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

from musicbrain.ml_logic.model import int_to_music_label
from musicbrain.ml_logic.registry import load_model

app = FastAPI()
app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict/json")
async def predict(data: dict = None):
    if data:
        try:
            X_pred = pd.DataFrame(data)
            y_pred = app.state.model.predict_proba(X_pred)
            # result = int_to_music_label(y_pred)
            print("Feature prediction: " + str(int_to_music_label(app.state.model.predict(X_pred))))
            
            return {"music_labels": y_pred.tolist()}
        except Exception as e:
            return {"error": f"Invalid JSON, exception '{e}'"}

    else:
        return {"error": "No valid input provided"}

@app.post("/predict/csv")
async def predict(file: UploadFile = File(None)):

    # if file and file.filename.endswith((".csv")):
    contents = await file.read()

    try:
        X_pred = pd.read_csv(io.BytesIO(contents), header=None)
        y_pred = app.state.model.predict_proba(X_pred)
        # result = int_to_music_label(y_pred)
        print("Feature prediction: " + str(int_to_music_label(app.state.model.predict(X_pred))))
        
        return {"music_labels": y_pred.tolist()}
    except Exception as e:
        return {"error": f"Invalid CSV file, exception '{e}'"}

    # else:
    #     return {"error": "No valid input provided"}