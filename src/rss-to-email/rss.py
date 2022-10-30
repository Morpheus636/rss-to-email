import config
import feedparser


def get_new_entries(feeds) -> list:
    new_entries = []

    for feed in feeds:
        parsed_feed = feedparser.parse(feeds[feed]["url"])
        # Go through entries and process any that were published since the feed was last parsed.
        for entry in parsed_feed.entries:
            # If the entry is new, add it to the list to return.
            if entry.link != feeds[feed]["last_entry"]:
                new_entries.append(entry)
                print(entry)  # FIXME
            # Break if the entry is not new.
            else:
                break

        # Update the last entry to be the most recent item.
        feeds[feed]["last_entry"] = parsed_feed.entries[0].link

    # Write the updated last entries to the file and return the list of newly parsed entries.
    config.update_feeds(feeds)
    return new_entries
