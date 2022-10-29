import os

import dotenv
import yaml


# Load environment variable from ./.env and ./local.env
dotenv.load_dotenv()
dotenv.load_dotenv("dev.env")
CONFIG_DIR = os.path.abspath(os.getenv("CONFIG_DIR"))


def load_feeds():
    with open(os.path.join(CONFIG_DIR, "feeds.yml"), "r") as feeds_file:
        feeds = yaml.safe_load(feeds_file)
    return feeds
