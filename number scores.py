#Names Scores
import urllib2
import time
start = time.time()

#dictionary to store alphabet values
alphabet_value = {'"':0, 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
                  'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
                  'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,
                  'z':26}

data = urllib2.urlopen("https://projecteuler.net/project/resources/p022_names.txt").read()
data = data.strip().split(",")
sort_data = sorted(data)
total = 0
for index in xrange(0,len(sort_data)):
    add = 0
    for j in sort_data[index].lower():
        add += alphabet_value[j]
    total += (add*(index+1))

end = time.time()
print(total)
print(end-start)
