import config
import feedparser


def get_new_entries(feeds: dict, count: int = 0) -> list:
    """Gets a list of entries added to each feed since the last time it was parsed.

    :param feeds: Dict of feed as loaded py `config.load_feeds()`
    :type feeds: dict
    :param count: Optional - tells the parser how many entries to return from
    the top of the list. If specified, the parser will ignore the last_entry field.
    :type count: int
    :return: List of tuples for each new entry in the format (feed_name, entry)
    :rtype: list
    """
    new_entries = []
    for feed in feeds:
        parsed_feed = feedparser.parse(feeds[feed]["url"])
        # If the count was specified, add the first x-number of entries to the list to return as tuples.
        if count:
            for i in range(0, count):
                new_entries.append((feed, parsed_feed.entries[i]))

        # If the count was not specified, return each new entry until the feed was last parsed.
        else:
            for entry in parsed_feed.entries:
                # If the entry is new, add it to the list to return.
                if entry.link != feeds[feed]["last_entry"]:
                    new_entries.append((feed, entry))
                # Break if the entry is not new.
                else:
                    break

        # Update the last entry to be the most recent item.
        feeds[feed]["last_entry"] = parsed_feed.entries[0].link

    # Write the updated last entries to the file and return the list of newly parsed entries.
    config.update_feeds(feeds)
    return new_entries
