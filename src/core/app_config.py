from pydantic import Field, PositiveInt

# Project Stuff
from core.base_config import MixinSettings


class AppConfig(MixinSettings):
    host: str = Field('localhost', env='HOST')
    port: PositiveInt = Field(8080, env='PORT')


app_config: AppConfig = AppConfig()