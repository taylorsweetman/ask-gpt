import json

from lib import Config


def get_config(temperature: float = 0) -> Config:
    with open("config.json") as config_file:
        config = json.load(config_file)
    return Config(
        temperature=temperature,
        max_tokens=config["max_tokens"],
        completions_model=config["completions_model"],
    )
