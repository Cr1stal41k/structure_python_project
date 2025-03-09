from pydantic_settings import BaseSettings


class MixinSettings(BaseSettings):
    """Base settings class for all settings classes."""


    class Config:
        """Pydantic config class."""
        env_file = '.env'
        env_file_encoding = 'utf-8'