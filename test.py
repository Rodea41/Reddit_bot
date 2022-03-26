import praw

#! Login credentials are in the "praw.ini" file
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("AedorBotTest") #! Will change the subreddit later once bot is complete
##subreddit = reddit.subreddit("AedorBotTest")

#! Prints the name of the account that is logged in
print(reddit.user.me())


for comment in subreddit.stream.comments(skip_existing=False):
    print("This is a comment ")
    print(comment.body)
    print("  ")



