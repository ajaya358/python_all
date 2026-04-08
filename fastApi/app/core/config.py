from pydantic_settings import BaseSettings, SettingsConfigDict # thisis a pydantic settings class used to load environment variables

class Settings(BaseSettings):
    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8") # this is a pydantic settings class
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore") # extra="ignore" పెడితే తెలియనివి వస్తే వదిలేస్తుంది
   
    POSTGRES_URL: str
    MONGO_URL: str
    MONGO_DB: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()