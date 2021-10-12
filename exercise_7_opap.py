import datetime
import urllib.request
import json

#Χρησιμοποιώ την βιβλιοθήκη datetime για να βρω την σημερινή ημερομηνία
date = datetime.datetime.now()
currentYear = date.strftime('%Y')
currentMonth = date.strftime('%m')
currentDay = date.strftime('%d')

# Η λίστα Days περιέχει όλες τις μέρες του μήνα.
Days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

day = currentDay

#Αφαιρώ το μηδενικό που προιγείται στην ημέρα, την κάνω στην αρχή λίστα και στην συνέχεια το κάνω string
if (day[0] == '0'):
    day = list(day)
    day.pop(0)
    day = str(day)
    day = day.replace('[', '')
    day = day.replace(']', '')
    day = day.replace("'", '')


  # Η λίστα changeday θα περιέχει τις μέρες του τρέχοντος μήνα.
changeDay = []

# Με αυτή τη δομή επανάληψης θα βάλω στη λίστα changeDay τις μέρες του τρέχοντος μήνα.
for n in Days:
    if(n > day):
        break
    else:
        changeDay.append(n)

# Μετατρέπω τη μεταβλητή day σε integer, όπου αντιπροσοπεύει το πλήθος των μερών που διανύσαμε μέχρι τώρα.
day = int(day)

print('Ο αριθμός που εμφανίζεται συχνότερα στο ΚΙΝΟ κάθε μέρα του τρέχοντος μήνα είναι:')
# Με αυτή τη δομή επανάληψης θα ξεκινώ από την πρώτη μέρα του μήνα και θα φτάνω μέχρι την τρέχουσα μέρα.
for i in range(day):

    temp = changeDay[i]
    changeDate = currentYear + '-' + currentMonth + '-' + temp
    url = 'https://api.opap.gr/draws/v3.0/1100/draw-date/' + changeDate + '/' + changeDate + '/draw-id' # Προσθέτω στο url την ημερομηνία.
    r = urllib.request.urlopen(url)
    draw_id = r.read()
    draw_id = draw_id.decode()
    draw_id = list(draw_id)
    draw_id.pop(0)
    draw_id.pop()

    Ids = []
    value = ''

    for g in range (len(draw_id)):
        if(draw_id[g] != ','):
          value += draw_id[g]
        else:
          Ids.append(value)
          value = ''

    t=[]
    # Με αυτή τη δομή επανάληψης θα ελέγξω όλες τις κληρώσεις που έγιναν την i μέρα.
    for j in range (len(Ids)):
        id = Ids[j]
        url_2 = 'https://api.opap.gr/draws/v3.0/1100/' + id
        r2 = urllib.request.urlopen(url_2)
        page_content = r2.read()
        page_content = page_content.decode()
        dict = json.loads(page_content)         # Μετατρέπω το page_content σε λεξικό.
        t.extend(dict['winningNumbers']['list'])

    #Δημιουργώ μια λίστα με 80 στοιχεία που αντιπροσωπεύουν τους 80 αριθμούς του ΚΙΝΟ και βρίσκω το πλήθος του αριθμού που υπάρχει τις περισσότερες φορές
    new_list = []
    for a in range(80):
        new_list.insert(a-1,0)
        for b in range(len(t)):
            if a==t[b]:
                new_list[a-1] +=1
    #Ορίζω ως max το πλήθος του πρώτου στοιχείου
    max = new_list[0]
    #Αναζητό το πραγματικό max και εισάγω στην μεταβλητή number τον αριθμό ο οποιός εμφανίζεται τις περισσότερες φορές
    for a in range(80):
        if new_list[a] > max:
            max = new_list[a]
            number = a-1
    print('\nΤην', i + 1, 'η μέρα είναι ο αριθμός:', number)
