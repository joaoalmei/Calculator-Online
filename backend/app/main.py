from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import EquationRequest, EquationResponse
from .calculator import calcular_expressao

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate", response_model=EquationResponse)
async def calcular(req: EquationRequest):
    resultado = calcular_expressao(req.expression)
    return EquationResponse(result=resultado)
