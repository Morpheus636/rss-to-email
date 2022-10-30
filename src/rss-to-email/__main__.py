import time

import config
import email_api
import rss


while True:
    # Wait 10 mins in between polls
    time.sleep(600)
    # Get the list of new entries and send each of them as an email.
    new_entries = rss.get_new_entries(config.load_feeds())
    for entry in new_entries:
        email_api.send_entry(entry)
