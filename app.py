import praw
user_agent = ("FMFABOT 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("frugalmalefashion")

for submission in subreddit.get_new(limit = 5):
    print "Title: ", submission.title
    print "Url: ", submission.url
    print "---------------------------------\n"
