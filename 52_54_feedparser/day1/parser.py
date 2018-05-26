import feedparser


feed_file = "newreleases.xml"

feed = feedparser.parse(feed_file)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(entry.published + " - " + entry.title + ': ' + entry.link)
