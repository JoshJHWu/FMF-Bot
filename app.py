import smtplib
import praw
import time
from submission import Submission

#add key word
keyword = "common"

# reddit parser
user_agent = ("UNIQUE ID")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("frugalmalefashion")

key_submissions = []

def search_reddit():
    for submission in subreddit.get_new(limit = 5):
        for word in submission.title.lower().split():
            if word == keyword:
                key_submissions.append(submission)
                print "SENDING:"
                print "Title: ", submission.title
                print "Url: ", submission.url
                print "---------------------------------\n"

                # mailer
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("BOT EMAIL", "PASS")

                msg = "Howdy, Your keyword: %s found a match! \n\n Title: %s \n Url: %s" % (keyword, submission.title, submission.url)
                server.sendmail("BOT EMAIL", "RECIPIENT EMAIL", msg)
                server.quit()

while True:
    search_reddit()
    print "working"
    time.sleep(60)
