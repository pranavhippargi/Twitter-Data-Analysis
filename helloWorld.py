import tweepy
import pandas as pd  

consumer_key = "yLjjxhLqUrp4181CRpF87XsrA"
consumer_secret = "uO9jXZcCJ1eRPHnVLA1eWf9U5hqC3NLH5PPwQvuWDrC2kvGcnE"
access_token = "2840569633-ve68zs1gAnS2qrwS3PVHYcPxgYCLV8oRdfoovDj"
access_token_secret = "nGK44QaP89jSLAC7TEvgPEXQXNgRSTpWZvZDG7dhsdFV3"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

class HelloWorld():
    def __init__(self):
       pass

    
    def getTweets(self):
        api = tweepy.API(auth)

        # The search term you want to find
        query = "Donald Trump"
        # Language code (follows ISO 639-1 standards)
        language = "en"

        # Calling the user_timeline function with our parameters
        results = api.search(q=query, lang=language)

        # Create arrays to store 1) Tweet,  2) Location, 3) Screen Name\

        tweetsArray = []
        locationArray = []
        screenNameArray = []

        # foreach through all tweets pulled
        for tweet in results:
        # printing the text stored inside the tweet object
            #print(tweet.user.screen_name,"Tweeted:",tweet.text, "Location:", tweet.user.location)
            tweetsArray.append(tweet.text)
            locationArray.append(tweet.user.location)
            screenNameArray.append(tweet.user.screen_name)
       # print(tweetsArray)
        #print(locationArray)
        s1 = pd.Series(tweetsArray)
        s2 = pd.Series(locationArray)
        s3 = pd.Series(screenNameArray)
        df = pd.join(s1, s2)
        #print(df.head)   
        df.to_csv('tweetsCSV2.csv', sep='\t', encoding='utf-8', index=False)    
test = HelloWorld()
test.getTweets()
    