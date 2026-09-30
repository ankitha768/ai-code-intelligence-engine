from pydantic import BaseModel, Field

class CodeRequest(BaseModel):
    language: str = Field(min_length=1, max_length=40)
    code: str = Field(min_length=1)

class SQLRequest(BaseModel):
    request: str = Field(min_length=3)
    schema_context: str = ""

class DocumentRequest(BaseModel):
    language: str = Field(min_length=1, max_length=40)
    code: str = Field(min_length=1)

class IntelligenceResponse(BaseModel):
    result: str
    mode: str
