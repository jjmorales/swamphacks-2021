import twitter_credentials   
import json                 
import tweepy
from tweepy import OAuthHandler                    


recent_tweets = []

def get_tweets(username, number_of_tweets): 

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET) #authentication
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    tweets = api.user_timeline(user_id=username,count=number_of_tweets, include_rts = False) 

    for tweet in tweets:
        if tweet.in_reply_to_status_id == None:
            recent_tweets.append({'name' : tweet.user.screen_name, 'text' : tweet.text, 'img' : tweet.user.profile_image_url})
  
# https://codeofaninja.com/tools/find-twitter-id/
# @WSBgod @WSBmod @chamath @elonmusk
target_user_id = ['1225646869730054146','1282418324228337665', '3291691', '44196397']      
target_user_screen = ['wsbgod','wsbmod','chamath','elonmusk'] 
number_of_tweets = 10    

for user in target_user_id:
    get_tweets(user, number_of_tweets)  

with open('tweets.json', 'w') as outfile:
    json.dump(recent_tweets, outfile)

