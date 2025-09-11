from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  mongo_uri: str