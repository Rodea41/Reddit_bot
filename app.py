import praw

#! Login credentials are in the "praw.ini" file
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("Eldenring")
##subreddit = reddit.subreddit("AedorBotTest")

#! Prints the name of the account that is logged in
print(reddit.user.me())

for comment in subreddit.stream.comments(skip_existing=True):
    print("This is a comment ")
    print(comment.body)
    print("  ")



"""    


for submission in subreddit.top(limit=1):
    print("************")
    print('SUBMISSION TITLE : ' + submission.title)
    print("************")
    ''' for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " Cooper Kupp " in comment_lower:
                print("-----------------")
                print(comment.body)
 '''
   
    #! &#x200B; == Blank space (in comment post)
    #! Gets the comment but not the nested comments
    # **TO DO ** Figure out how to get nested comments
    for comment in submission.comments:
        counter = comment
        print(' ')
        print('START OF NEW COMMENT')
        print('-----------------')
        print(' ')
        print('comment # ' + str(comment))
        print(comment.body)
        if comment.replies:
            for reply in comment.replies:
                print('+++++++++++')
                print(' ')
                print('REPLY:', reply.body)





"""