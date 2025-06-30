import configparser
from pathlib import Path
from typing import Any, Dict, Tuple, Type

from pydantic.fields import FieldInfo
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

from pydantic import BaseModel

class ADKAgents(BaseModel):
    gemini_api_key: str
    google_api_key: str
    app_name: str
    gemini_model: str

class RDS(BaseModel):
    db_url: str

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config/config.ini"
print(f"Config path: {CONFIG_PATH}")

class IniConfigSettingsSource(PydanticBaseSettingsSource): 
    """
    Settings source class for INI file
    """

    def get_section_values(self, section: str, encoding: str) -> Dict[str, Any]:
        config = configparser.ConfigParser()
        config.optionxform = str  # type: ignore

        config.read(Path(CONFIG_PATH), encoding=encoding)

        if config.has_section(section):
            return {key: config.get(section, key) for key in config.options(section)}
        return {}

    def get_field_value(self, field: FieldInfo, field_name: str) -> Tuple[Any, str, bool]:
        raise NotImplementedError("get_field_value is not implemented")

    def __call__(self) -> dict[str, Any]:
        d: Dict[str, Any] = {}
        encoding = self.config.get("env_file_encoding", "utf-8")

        for field_name, model_field in self.settings_cls.model_fields.items():
            section_values = self.get_section_values(field_name, encoding)  # type: ignore
            if section_values:
                d[field_name] = section_values
            else:
                d[field_name] = model_field.default
        return d


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    ADK_AGENTS: ADKAgents
    RDS: RDS
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            IniConfigSettingsSource(settings_cls),
            env_settings,
            file_secret_settings,
        )


settings = Settings()  # type: ignore