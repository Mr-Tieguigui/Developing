from pattern.web import Twitter, plaintext

twitter = Twitter(language='en') 
for tweet in twitter.search('"more important than"', cached=False):
    print(plaintext(tweet.text))