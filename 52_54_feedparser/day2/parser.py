import feedparser


feed_file = "reddit_tech.xml"

feed = feedparser.parse(feed_file)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(entry.title)
