import praw
from submission import Submission
from container import Container

user_agent = ("FMFA 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("frugalmalefashion")
c = Container()

for submission in subreddit.get_new(limit = 5):
    s = Submission({'title':submission.title,'url':submission.url})
    c.contents.append(s)
    # print "Title: ", s.title
    # print "Url: ", s.url
    # print "---------------------------------\n"

print c.contents[0].title
