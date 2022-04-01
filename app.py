import praw
import re 

#! Login credentials are in the "praw.ini" file
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("AedorBotTest") #! Subreddit was made to test bot

#! Prints the name of the account that is logged in
print(reddit.user.me())



#! FILTER COMMENTS AND SEE IF BOT IS CALLED
def check_comment(comment):
    stringComment = str.lower(comment.body) #CONVERT TO STRING AND LOWERCASE
    commentRegex = re.compile(r"test_bot") # <== REGEX FILTER LOOKS FOR 'test_bot' (lowercase sensitive)
    match = commentRegex.search(stringComment) # RUN THE SEARCH FILTER ON COMMENT.BODY
    
    if bool(match): #IF REGEX IS GREATER THAN 0 ==> OUR FILTER FOUND SOMEONE CALLING THE BOT
        comment.reply('Your Bot Works!')
        print("Replied to comment")


for comment in subreddit.stream.comments(skip_existing=False):
    check_comment(comment)

        
