from tkinter import *


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    


    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit", COMMAND=getTweets())

        # placing the button on my window
        quitButton.place(x=0, y=0)

import tweepy
import pandas as pd  

   

   
class HelloWorld():
    def __init__(self):
        pass

    def getNewTweets(self):
        pass
    
    
    def getTweets(self):
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
        


            
test = HelloWorld()
test1 = HelloWorld()
test1.getTweets()
    
















root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  
