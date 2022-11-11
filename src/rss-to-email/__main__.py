import random
import time

import config
import email_api
import rss


def main():
    # Check if it's the first run of the config file.
    feeds = config.load_feeds()
    # Get the last entry field from a random feed.
    last_entry = random.choice(list(feeds.values()))["last_entry"]
    if not last_entry:
        rss.get_new_entries(feeds, count=1)

    # Start the poll loop.
    while True:
        # Get the list of new entries and send each of them as an email.
        new_entries = rss.get_new_entries(config.load_feeds())
        for entry in new_entries:
            email_api.send_entry(entry)

        # Wait 10m between polls
        time.sleep(600)


if __name__ == "__main__":
    main()
