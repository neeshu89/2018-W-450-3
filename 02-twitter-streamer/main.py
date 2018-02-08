from lib.twitter_streamer import Twitterator
from lib.utility import get_credentials
#importing classes from libraries in lib folder

if __name__ == "__main__":
    # checking that this module is the main module, otherwise, abort and go back

    try:
        credentials = get_credentials()

        vineland_bbox = "-75.2565792933,39.3133877994,-74.8130062952,39.5808909262"

        this_twitterator = Twitterator(credentials, vineland_bbox)
        # setting the location and logging in
        # define westwood_bbox as the coordinates
        # inputs the attributes/parameters for the local Twitterator function
        
        this_twitterator.collect_tweets()
        # calls on the collect_tweets function using the local twitterator (which has the local attributes)

    except FileNotFoundError:
        print("Did you forget to create you credentials.yml file in the data directory?")
        # except function only gets called in the case of an error/exception
 
        # if error with file for get_credentials - serve up error