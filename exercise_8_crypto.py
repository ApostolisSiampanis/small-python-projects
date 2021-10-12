import urllib.request
import json

#Ζητάω από τον χρήστη αν δώσει την διεύθυνση του αρχείου
file = input('Give file path: ')
#Ανοίγω το αρχείο
f = open(file, 'r')
#Εισάγω με την χρήση του json τα στοιχεία του αρχείου
mydict = json.loads(f.read())
#Κλείνω το αρχείο
f.close()
#Μετράω το μήκος του λεξικού μου
k = len(mydict)
#Προσθέτω τα κλειδιά του λεξικού μου στην μεταβλητή cryptocurrency
cryptocurrency = list(mydict.keys())
#Προσθέτω τις τιμές του λεξικού μου στην μεταβλητή values
values = list(mydict.values())
#Επαναλαμβάνω την διαδικασία της αναζήτησης όσες φο΄ρες χρείαζεται σύμφωνα με το μέγεθος του λεξικού
for i in range (k):
    string = cryptocurrency[i]
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms="+string+"&tsyms=EUR"
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    d = json.loads(html)
    output = string + ' in euro:'
    amount = int(d[string]['EUR']) * values[i]
    print(output, amount)
