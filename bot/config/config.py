from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    CLAIM_RETRY: int = 1
    SLEEP_BETWEEN_CLAIM: int = 240

    AUTO_UPGRADE_FARM: bool = True
    MAX_UPGRADE_LEVEL: int = 3

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
