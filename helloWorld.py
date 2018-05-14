#Twitter API
import tweepy
#Pandas for DataFrame Objects
import pandas as pd  
import matplotlib.pyplot as plt
import textblob as tb 


# API KEYS 
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
       self.tweet =[]
       self.tweetText =[]

    
    def getTweets(self):
        api = tweepy.API(auth)

        # The search term you want to find
        query = "Microsoft"
        # Language code (follows ISO 639-1 standards)
        language = "en"

        # Calling the user_timeline function with our parameters
        results = api.search(q=query, lang=language)

        # Create arrays to store 1) Tweet,  2) Location, 3) Screen Name
        # All other things like Date + Time, Media, ect, will be added later 

        self.tweetsArray = []
        self.locationArray = []
        self.screenNameArray = []
        self.sentimentArray = []
        
        # foreach through all tweets pulled
        for tweet in results:
        # printing the text stored inside the tweet object
        #print(tweet.user.screen_name,"Tweeted:",tweet.text, "Location:", tweet.user.location)
           self.tweetsArray.append(tweet.text)
           self.locationArray.append(tweet.user.location)
           self.screenNameArray.append(tweet.user.screen_name)
           self.sentimentArray.append()
        #    self.sentimentArray.append()
      
    def getSentiment(self):
       
        positive = 0
        negative = 0
        neutral = 0
        polarity = 0

        for tweets in results:
            analysis = textblob(tweets.text)
            polarity += analysis.sentiment.polarity

            if(analysis.sentiment.polarity == 0):
                neutral += 1
            elif(analysis.sentiment.polarity < 0.00):
                negative += 1
            elif(analysis.sentiment.polarity > 0.00):
                positive += 1

    def percentage(self, part, whole):
        
        return 100 * (float(part) / float(whole))
    
    


       

#_-----------------------------------------------------------------------------------------x-----------------------------------------------------------------------_#

#Let's GO! 
test = HelloWorld()
test.getTweets()
test.addToArray()
    
