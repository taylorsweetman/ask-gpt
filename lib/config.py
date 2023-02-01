import json

from lib import Config


def get_config() -> Config:
    with open("config.json") as config_file:
        config = json.load(config_file)
    return Config(**config)
