import os

import dotenv
import yaml


# Load environment variable from ./.env and ./local.env
dotenv.load_dotenv()
dotenv.load_dotenv("dev.env")
CONFIG_DIR = os.path.abspath(os.getenv("CONFIG_DIR"))


def load_config():
    with open(os.path.join(CONFIG_DIR, "config.py"), "r") as config_file:
        config = yaml.safe_load(config_file)
    return config
