from pydantic import Field, PositiveInt

# Project Stuff
from core.base_config import MixinSettings


class AppConfig(MixinSettings):
    host: str = Field(default='localhost', env='HOST')
    port: PositiveInt = Field(default=8080, env='PORT')


app_config: AppConfig = AppConfig()
