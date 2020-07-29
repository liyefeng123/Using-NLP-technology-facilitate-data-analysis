import tweepy
import nltk, re, pprint

consumer_key = "JkeYDc16IeikToySQVJvvtP6s"
consumer_secret = "PWmCpVmBJifPVHx4mq96EBD5fR9o91XVuqPGtGJYOhbwTPrK4i"
access_token = "1197607983406100480-QMbGvirnYOOynKEBLOWInLf6sbnWLe"
access_token_secret = "nFeMwaf3uUaIJoNSVMa7LwkCjWKvIA0hgEbB1baKmNUbO"

# 创建认证对象
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 设置你的access token和access secret
auth.set_access_token(access_token, access_token_secret)
# 传入auth参数，创建API对象
api = tweepy.API(auth)
#api = tweepy.API(auth_handler=auth, parser=JSONParser(), proxy = '127.0.0.1:1080', wait_on_rate_limit=True)


query = "car accident"
language = "en"
results = api.search(q=query,)
for tweet in results:
    print (tweet.user.screen_name,"Tweeted:",tweet.text)


#def ie_preprocess(document):
#    sentences = nltk.sent_tokenize(document)                      #句子分割s
#    sentences = [nltk.word_tokenize(sent) for sent in sentences]  #分词
#    sentences = [nltk.pos_tag(sent) for sent in sentences]        #词性标注器
