import praw

#! Login credentials are in the "praw.ini" file
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("Eldenring") #! Will change the subreddit later once bot is complete
##subreddit = reddit.subreddit("AedorBotTest")

#! Prints the name of the account that is logged in
print(reddit.user.me())


for comment in subreddit.stream.comments(skip_existing=True):
    print("This is a comment ")
    print(comment.body)
    print("  ")
''' 
for comment in subreddit.stream.comments(skip_existing=True):
    print("This is a comment ")
    print(comment.body)
    print("  ")

    #! TODO
    #! 1. Find comment that has 'football_stats_bot (POS, Name, year(optional))'
    #! 2. Filter out everything in the comment using regex. All we want is want is ( POS, Name, year(optional) )
    #! 3. Determine if the year parameter was entered, if not then use the current year(2021) by default
    #! 4. Format the result into JSON so we can query the SQLite3 database with it 
    if comment.body == "football_stats_bot": 
        """ Need to respond to 'football_stats_bot (WR, C. Kupp, year(optional))'    """
        
        if comment.body has 'WR':
            pass
            if comment.body
        
        elif comment.body has 'QB':
            pass

        elif comment.body has 'RB':
            pass

        elif comment.body has 'K':
            pass

        elif comment.body has 'TE':
            pass

        else:
            print("That is not a position I recognize") '''











"""
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " Cooper Kupp " in comment_lower:
                print("-----------------")
                print(comment.body)
"""