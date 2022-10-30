import config
import rss


feeds = config.load_feeds()
new_entries = rss.get_new_entries(feeds)
print(new_entries)
