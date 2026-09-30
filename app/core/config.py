from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Code Intelligence Engine"
    environment: str = "development"
    llm_mode: str = "demo"
    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_model: str = ""
    database_url: str = "sqlite:///./local.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
