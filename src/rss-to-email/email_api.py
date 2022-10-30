import os

import yagmail


RECIPIENT = os.environ["RECIPIENT_ADDRESS"]

email_client = yagmail.SMTP(os.environ["GMAIL_USER"], os.environ["GMAIL_PASSWORD"])


def send_entry(feed_and_entry: tuple) -> None:
    """Send an entry via gmail.

    :param feed_and_entry: Tuple containing the feed name and entry
    :return: None
    """
    feed_name = feed_and_entry[0]
    entry = feed_and_entry[1]

    contents_formatted = f"{entry.description} \n\n View full source: {entry.link} \nPublished in {feed_name} at {entry.published}\n Sent by Morpheus636's rss-to-email."

    email_client.send(
        to=RECIPIENT,
        subject=f"{feed_name}: {entry.title}",
        contents=contents_formatted,
    )
