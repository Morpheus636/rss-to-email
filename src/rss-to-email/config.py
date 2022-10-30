import os

import dotenv
import yaml


# Load environment variable from ./.env and ./local.env
dotenv.load_dotenv()
dotenv.load_dotenv("dev.env")
CONFIG_DIR = os.path.abspath(os.getenv("CONFIG_DIR"))
FEEDS_PATH = os.path.join(CONFIG_DIR, "feeds.yml")


def load_feeds() -> None:
    with open(FEEDS_PATH, "r") as feeds_file:
        feeds = yaml.safe_load(feeds_file)
    return feeds


def update_feeds(feeds) -> None:
    with open(FEEDS_PATH, "w") as feeds_file:
        yaml.safe_dump(feeds, feeds_file)
