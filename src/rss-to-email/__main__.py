import config
import email_api
import rss


feeds = config.load_feeds()
new_entries = rss.get_new_entries(feeds)
print(new_entries)
for entry in new_entries:
    email_api.send_entry(entry)
