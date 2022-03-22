import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")
##subreddit = reddit.subreddit("AedorBotTest")


print(reddit.user.me())


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
