from pydantic import BaseModel

class EquationRequest(BaseModel):
    expression: str  

class EquationResponse(BaseModel):
    result: str  
