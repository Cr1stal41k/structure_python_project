from pydantic import Field

# Project Stuff
from core.base_config import MixinSettings


class SettingsPostgres(MixinSettings):
    """
    Настройки подключений к БД

    """

    db_name: str = Field(default='postgres', env='DB_NAME')
    db_user: str = Field(default='postgres', env='DB_USER')
    db_password: str = Field(default='postgres', env='DB_PASSWORD')
    db_host: str = Field(default='localhost', env='DB_HOST')
    db_port: str = Field(default='5432', env='DB_PORT')


db_config: SettingsPostgres = SettingsPostgres()
