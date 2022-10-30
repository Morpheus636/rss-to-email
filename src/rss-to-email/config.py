import os

import dotenv
import yaml


# Load environment variable from ./.env and ./local.env
dotenv.load_dotenv()
dotenv.load_dotenv("dev.env")
CONFIG_DIR = os.path.abspath(os.environ["CONFIG_DIR"])
FEEDS_PATH = os.path.join(CONFIG_DIR, "feeds.yml")


def load_feeds() -> dict:
    """Loads the dict of RSS feeds to monitor from `feeds.yml`

    :return: None
    """
    with open(FEEDS_PATH, "r") as feeds_file:
        feeds = yaml.safe_load(feeds_file)
    return feeds


def update_feeds(feeds: dict) -> None:
    """Writes the dict of RSS feeds to `feeds.yml`.
    Most often used when updating the `last_entry` of each feed.

    :param feeds: The dict of feeds to dump to the file.
    :type feeds: dict
    :return: None
    """
    with open(FEEDS_PATH, "w") as feeds_file:
        yaml.safe_dump(feeds, feeds_file)
