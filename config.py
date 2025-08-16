from pydantic import BaseSettings
class Settings(BaseSettings):
    BASE_DOMAIN: str = "braylockglobalai.com"
    WHISPERLINK_SALT: str = "supersecret"
    DEFAULT_FROM: str = "Dave <sales@braylockglobalai.com>"
settings = Settings()
