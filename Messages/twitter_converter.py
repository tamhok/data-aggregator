from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from . import models
from . import twitter_secrets
import json
import logging

class TwitterHandler( StreamListener ):


    def __init__( self ):
        self.logger = logging.getLogger(__name__)

        try:
            self.auth = OAuthHandler(twitter_secrets.APP_KEY, twitter_secrets.APP_SECRET)
            self.auth.secure = True
            self.auth.set_access_token(twitter_secrets.OAUTH_TOKEN, twitter_secrets.OAUTH_TOKEN_SECRET)

            self.api = API(self.auth)

            # If the authentication was successful, you should
            # see the name of the account self.logger.info out
            self.logger.info(self.api.me().name)

            self.stream = Stream(self.auth, self)
            self.stream.userstream(async = True)

        except BaseException as e:
            self.logger.info("Error in __init__", e)

    def on_connect( self ):
        self.logger.info("Connection established!!")

    def on_disconnect( self, notice ):
        self.logger.info("Connection lost!! : ", notice)

    def on_data( self, status ):
        self.logger.info("Entered on_data()")
        data = json.loads(status)
        if 'direct_message' in data:
            name = data['direct_message']['sender_screen_name']
            text = data['direct_message']['text']
            m = models.Message(source = "twitter", name = name, message = text, rec_by = "", response = "")
            m.save()
            self.logger.info("Name: " + name + " Text: " + text)
        return True

    def on_error( self, status ):
        self.logger.info(status)

    def sendMessage( self, name, message):
        if(self.api.me().screen_name != name):
            self.api.send_direct_message(screen_name = name, text = message)
            self.logger.info("successfully sent " + message + " to " + name)
        else:
            self.logger.info("Cannot send message to yourself")


#tweeter = TwitterHandler()
