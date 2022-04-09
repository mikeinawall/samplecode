### This code used 3 files 
#a) a csv of fake tweets  
#b) txt file consisting of a list of positive words  
#c) a txt file of negative words
#Using those files it created a csv which created a score for a tweet based on the positive and negative words in the tweet

def strip_punctuation(x):
    for y in punctuation_chars:
        if y in x:
            x = x.replace(y, '')
    return x

def get_neg(x):
    x = strip_punctuation(x)
    x = x.lower()
    x = x.split() 
    y = 0 
    for word in negative_words:
        if word in x:
            y += 1
    return y

def get_pos(x):
    x = strip_punctuation(x)
    x = x.lower()
    x = x.split() 
    y = 0 
    for word in positive_words:
        if word in x:
            y += 1
    return y

tweets = open("project_twitter_data.csv", "r")
data = open("resulting_data.csv" , "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
data.write('\n')
tweet_lines = tweets.readlines()[1:]

for line in tweet_lines:
    line_split = line.split(',')
    nort = line_split[1]
    norp = line_split[2].strip()
    pos = get_pos(line)
    neg = get_neg(line)
    net = pos - neg
    rowstring = '{}, {}, {}, {}, {} '.format(nort,norp,pos,neg,net)
    data.write(rowstring)
    data.write('\n')
    
tweets.close()
data.close()
