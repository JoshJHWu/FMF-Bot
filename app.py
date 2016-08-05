import smtplib
import praw
from submission import Submission

#add key word
keyword = "cotton"

# reddit parser
user_agent = ("FMFA 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("frugalmalefashion")

key_submissions = []

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
            server.login("fmfbot@gmail.com", "NachoMontreal")

            msg = "Howdy, Your keyword: %s found a match! \n\n Title: %s \n Url: %s" % (keyword, submission.title, submission.url)
            server.sendmail("fmfbot@gmail.com", "joshua.jh.wu@gmail.com", msg)
            server.quit()
