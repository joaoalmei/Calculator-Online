from pydantic import BaseModel

class EquationRequest(BaseModel):
    expression: str  # expressão matemática recebida do frontend

class EquationResponse(BaseModel):
    result: str  # resultado da expressão (ex: "4" ou "2.5")
