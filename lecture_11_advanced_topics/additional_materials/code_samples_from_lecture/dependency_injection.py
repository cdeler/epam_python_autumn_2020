import datetime
from typing import Callable


class ConstructorInjection:
    def __init__(self, config_provider: Callable) -> None:
        self.config_provider = config_provider

    def get_db_connection_string(self) -> str:
        current_config = self.config_provider()
        return current_config.db_connection


class ParameterInjection:
    def __init__(self) -> None:
        pass

    def get_db_connection_string(self, config_provider: Callable) -> str:
        current_config = config_provider()
        return current_config.db_connection


class SetterInjection:
    """Setter Injection"""

    def __init__(self):
        pass

    def set_config_provider(self, config_provider: Callable):
        self.config_provider = config_provider

    def get_db_connection_string(self):
        current_config = self.config_provider()
        return current_config.db_connection


def production_conf() -> str:
    config = type("Config", (), {"db_connection": "postgres:///prod.db:5432/db"})
    return config

def dev_conf() -> str:
    config = type("Config", (), {"db_connection": "postgres:///localhost:5432/db"})
    return config


if __name__ == "__main__":
    prod_conf_constructor_inj = ConstructorInjection(production_conf)
    print(prod_conf_constructor_inj.get_db_connection_string())
    
    dev_conf_constructor_inj = ConstructorInjection(dev_conf)
    print(dev_conf_constructor_inj.get_db_connection_string())
    
    prod_conf_param_inj = ParameterInjection()
    print(prod_conf_param_inj.get_db_connection_string(production_conf))
    
    dev_conf_param_inj = ParameterInjection()
    print(dev_conf_param_inj.get_db_connection_string(dev_conf))
    
    prod_conf_setter_inj = SetterInjection()
    prod_conf_setter_inj.set_config_provider(production_conf)
    print(prod_conf_setter_inj.get_db_connection_string())
    
    dev_conf_setter_inj = SetterInjection()
    dev_conf_setter_inj.set_config_provider(dev_conf)
    print(dev_conf_setter_inj.get_db_connection_string())
    
