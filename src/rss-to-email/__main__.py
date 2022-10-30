import time

import config
import email_api
import rss


while True:
    # Get the list of new entries and send each of them as an email.
    new_entries = rss.get_new_entries(config.load_feeds())
    for entry in new_entries:
        email_api.send_entry(entry)

    # Wait 10m between polls
    time.sleep(600)
