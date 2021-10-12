import tweepy
import re

#Συνάρτηση για την αφαίρεση των emoji
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                               "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

#Επαλήθευση κλειδιών
api_key = '' #my api key
api_secret_key = '' #my api secret key
access_token = '' #my access token
access_token_secret = '' #my access token secret

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
screenname = input("Screen name")
stuff = api.user_timeline(screenname, count = 10, include_rts = True)

#Παίρνω τα tweets και τα βάζω σε μια λ΄ίστα
tweets = str(stuff)
list = []
x = ""
for info in stuff[:]:
    for i in str(info.text):
        if i==" ":
            list.append(x)
            x=""
        else:
            x = x + i

#Χρησιμοποιώ την επανάληψη φυσαλίδας με φθίνουσα σειρά ώστε να σχηματίσω ανάλογα την λίστα μου
u=len(list)
for i in range(1,u,1):
    for z in range(u-1,i-1,-1):
        if len(list[z])<len(list[z-1]):
            list[z],list[z-1]=list[z-1],list[z]

#Αφαίρεση των emoji
list2 = []
for q in range(len(list)):
    text = list[q]
    list2.append(deEmojify(text))
list = list2

#Πάω και διαβάζω την λ΄σιτα ανάποδα και βλέπω αν κάποιο στοιχείο της λίστας περιέχει κάποιο ειδικό χαρακτήρα
Numbers=["1","2","3","4","5","6","7","8","9","0"]
for y in range(u-1,-1,-1):
    text = list[y]
    if ("."in text) or (","in text) or ("!"in text) or ("@"in text) or ("#"in text) or ("$"in text) or ("%"in text) or ("^"in text) or ("&"in text) or ("*"in text) or ("("in text) or (")"in text) or ("["in text) or ("]"in text) or ("{"in text) or ("}"in text) or (";"in text) or (":"in text) or ("/"in text) or ("<"in text) or (">"in text) or ("?"in text) or ("|"in text) or ("-"in text) or ("="in text) or ("_"in text)or("+"in text) or ("http"in text) or ("\\"in text):
        list.pop(y)
    elif True:
        for w in range(10):
            if Numbers[w] in list[y]:
                list.pop(y)

#Εκτυπώνω τις μεγαλύτερες σε μήκος λέξεις
print ("The longest words are:",list[-5],list[-4],list[-3],list[-2],list[-1])
#Εκτυπώνω τις μικρότερες σε μήκος λέξεις
print ("The shortest words are:",list[0],list[1],list[2],list[3],list[4])
