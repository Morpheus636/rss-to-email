import config
import rss


feeds = config.load_feeds()
new_entires = rss.get_new_entries(feeds)
