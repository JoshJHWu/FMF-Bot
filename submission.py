class Submission():

    def __init__(self, args = {}):
        self.title = args['title']
        self.url = args['url']

# print Submission({'title':"title", 'url':1}).url
