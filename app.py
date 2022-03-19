import praw

reddit = praw.Reddit(
    client_id="xxxxx",
    client_secret="xxxxx",
    user_agent="xxxxx",
    username="xxxxx",
    password="xxxxxx"

)

subreddit = reddit.subreddit("AedorBotTest")

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
