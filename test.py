import praw
import re

#! Login credentials are in the "praw.ini" file
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("AedorBotTest") #! Will change the subreddit later once bot is complete
##subreddit = reddit.subreddit("AedorBotTest")

#! Prints the name of the account that is logged in
print(reddit.user.me())


#! FILTER COMMENTS AND SEE IF BOT IS CALLED
def check_comment(comment):
    stringComment = str.lower(comment) #CONVERT TO STRING AND LOWERCASE
    commentRegex = re.compile(r"test_bot(POS, Name, Year)") # <== REGEX FILTER LOOKS FOR 'test_bot' (lowercase sensitive)
    match = commentRegex.search(stringComment) # RUN THE SEARCH FILTER ON COMMENT.BODY

    if bool(match): #IF 'match' IS EMPTY = FALSE, ELSE IT = TRUE
        """NEED TO FIGURE OUT HOW TO TAKE THE PARAMETERS (POS, NAME, YEAR) AND FILTER THEM. THEN THEY NEED TO BE RE
        RETURNED OR STORED IN A VARIABLE SO THAT THE FUNCTION 'search_database()' can use it to query our db. IF THERE IS NO YEAR VALUE THEN IT 
        STILL NEEDS TO RUN  """
        
        
        
        

        return True
    else:
        return False


#! HOW THE INFO SHOULD BE ACCESSED IN THE DATABASE    
def search_database():
    #1.RECEIVE COMMENT, STRIP IT, ACCESS DATABASE, RETURN JSON DICT
    pass




for comment in subreddit.stream.comments(skip_existing=False):
    if check_comment(comment.body):
        newFilterRegex = "create a filter that can format the string down to (POS, Name, Year)"
        
        search_database() 
       # print("PASSED THE TEST: " + str(comment.body))
    else:
        #print("FAILED THE TEST")
    


















#! HOW THE INFO SHOULD BE ACCESSED IN THE DATABASE    
def search_database():
    #1.RECEIVE COMMENT, STRIP IT, ACCESS DATABASE, RETURN JSON DICT
    pass

#! HOW THE INFO FROM THE DATABASE SHOULD BE FORMATTED AND RESPONDED TO ON THE REDDIT SITE
def respond_to_commentor_with():
    pass


#for comment in praw.helpers.comment_stream(reddit, 'AedorBotTest'): #(LOGIN CRED, SUBREDDIT)
   # if check_comment(comment): # CHECK IF BOT IS CALLED
    #    search_database(reformatted_comment) #IF TRUE THEN SEARCH DATABASE FOR THE PARAMETERS ENTERED

    #else:
     #   continue # DO I USE RETURN, CONTINUE, OR BREAK?  **NEED TO LOOK UP**






''' 
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