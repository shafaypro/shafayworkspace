import tweepy  # the main file used ofr the twitter access
from tweepy import Stream  # Stream is taken by this
from tweepy import OAuthHandler  # outh handler is a secuirity gate which checks the security number of employes
from tweepy.streaming import StreamListener  # cause we need to import the file so that we can inherit in the class
import time
ckey = 'Ru74Ybfzyws3q2JSNZTOUv4gv'
csecret = 'auVpDi7tbPR6K9hARUDPx58GwdmB24VyAOenXg6jfJ2uiK03nZ'
atoken = '558084273-QWy1ZFg5ZO6G0BvuJbVAyZNxinUfKERLmWfPPMBc'
asecret = 'PjA8TYtCNUyc1dhDv7BqWeCQstDx2fbGn8ZrqXitxkPet'

class listener(StreamListener):  # This is extending the Stream Listener class
	def on_data(self, raw_data):
		try:
			#print (raw_data)
			# if you want a limited data abstracted from the twitter then we need the following lone
			tweet = raw_data.split(',"text":"')[1].split('","source')[0]
			print (tweet)
			savetweet = str(time.time()) + '::' + tweet
			saveFile = open('TwitterDB.csv', 'a') # CSV file is created and ready to Written
			saveFile.write(savetweet) # adds the data to the file (replace by raw_data)
			saveFile.write('\n')  # for each line ending the next line is implemented
			return True
		except BaseException, e:
			print ('Failed on data : ,'+str(e))
			time.sleep(5)
	def on_error(self, status_code):
		print (status_code)

auth = OAuthHandler(ckey, csecret)  # the oath handler checks the consumers key and secret
auth.set_access_token(atoken, asecret)  # the access token are matched by the oath handler
twitterStream = Stream(auth, listener())  # twitter stream streams the access access set,ask for the listener n give data
twitterStream.filter(track=['car']) # Filters the tweets by track