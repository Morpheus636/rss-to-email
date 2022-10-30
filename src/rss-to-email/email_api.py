import os

import yagmail


email_client = yagmail.SMTP(os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASSWORD"))


def send_entry(feed_and_entry: tuple) -> None:
    """Send an entry via gmail."""
    feed_name = feed_and_entry[0]
    entry = feed_and_entry[1]

    contents_formatted = f"{entry.description} \n\n View full source: {entry.link} \nPublished in {feed_name} at {entry.published}\n Sent by Morpheus636's rss-to-email."

    email_client.send(
        to=os.getenv("RECIPIENT_ADDRESS"),
        subject=f"{feed_name}: {entry.title}",
        contents=contents_formatted,
    )
