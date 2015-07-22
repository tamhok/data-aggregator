from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from . import models
from . import twitter_secrets
import json

class TwitterHandler( StreamListener ):

    def __init__( self ):
        try:
            self.auth = OAuthHandler(twitter_secrets.APP_KEY, twitter_secrets.APP_SECRET)
            self.auth.secure = True
            self.auth.set_access_token(twitter_secrets.OAUTH_TOKEN, twitter_secrets.OAUTH_TOKEN_SECRET)

            self.api = API(self.auth)

            # If the authentication was successful, you should
            # see the name of the account print out
            print(self.api.me().name)

            self.stream = Stream(self.auth, self)

            self.stream.userstream(async = True)

        except BaseException as e:
            print("Error in __init__", e)


    def on_connect( self ):
        print("Connection established!!")

    def on_disconnect( self, notice ):
        print("Connection lost!! : ", notice)

    def on_data( self, status ):
        print("Entered on_data()")
        data = json.loads(status)
        if 'direct_message' in data:
            name = data['direct_message']['sender_screen_name']
            text = data['direct_message']['text']
            models.Message("twitter", name, text)
            print("Name: " + name + " Text: " + text)
        return True

    def on_error( self, status ):
        print(status)

    def sendMessage( self, name, message):
        if(self.api.me().screen_name != name):
            self.api.send_direct_message(screen_name = name, text = message)
            print("successfully sent " + message + " to " + name)
        else:
            print("Cannot send message to yourself")

#def main():
#    listener = StdOutListener()
#    print("I'm async")

#if __name__ == '__main__':
#    main()
