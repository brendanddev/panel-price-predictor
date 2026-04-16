from fastapi import FastAPI

app = FastAPI(title="Panel Price Predictor API")


@app.get("/")
def root():
    return {"message": "Panel Price Predictor API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}