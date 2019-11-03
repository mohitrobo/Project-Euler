#Cyclical figurate numbers

import time
from collections import defaultdict

start = time.time()

#store numbers with length of four
tri = []
squ = []
pen = []
hexa = []
hep = []
octo = []
for i in xrange(1,10000):
    #triangular numbers
    t = (i*(i+1))/2
    if len(str(t)) == 4:
        tri.append(t)
    #square numbers
    s = i*i
    if len(str(s)) == 4:
        squ.append(s)
    #Pentagonal numbers
    p = (i*(3*i-1))/2
    if len(str(p)) == 4:
        pen.append(p)
    #Hexagonal numbers
    hx = i*(2*i-1)
    if len(str(hx)) == 4:
        hexa.append(hx)
    #Heptagonal numbers
    hp = (i*(5*i-3))/2
    if len(str(hp)) == 4:
        hep.append(hp)
    #Octagonal numbers
    oc = i*(3*i-2)
    if len(str(oc)) == 4:
        octo.append(oc)
    

#print("tri:{}".format(len(tri)))
#print("squ:{}".format(len(squ)))
#print("pen:{}".format(len(pen)))
#print("hexa:{}".format(len(hexa)))
#print("hep:{}".format(len(hep)))
#print("octo:{}".format(len(octo)))


#1.) make a dictionary of key:value pair where, keys last 2 digit == first 2 digit of values
#2.) keeping one list as key and other lists as value


#dictionary for cyclical numbers
cyclical = defaultdict(list)

#triangular list as key
for i in xrange(0,len(tri)):
    for j in xrange(0,len(squ)):
        if str(tri[i])[2:] == str(squ[j])[:2]:
            if int(str(squ[j])[2:])>=10:
                cyclical[3,tri[i]].append((4,squ[j]))
    for j in xrange(0,len(pen)):
        if str(tri[i])[2:] == str(pen[j])[:2]:
            if int(str(pen[j])[2:])>=10:
                cyclical[3,tri[i]].append((5,pen[j]))
    for j in xrange(0,len(hexa)):
        if str(tri[i])[2:] == str(hexa[j])[:2]:
            if int(str(hexa[j])[2:])>=10:
                cyclical[3,tri[i]].append((6,hexa[j]))
    for j in xrange(0,len(hep)):
        if str(tri[i])[2:] == str(hep[j])[:2]:
            if int(str(hep[j])[2:])>=10:
                cyclical[3,tri[i]].append((7,hep[j]))
    for j in xrange(0,len(octo)):
        if str(tri[i])[2:] == str(octo[j])[:2]:
            if int(str(octo[j])[2:])>=10:
                cyclical[3,tri[i]].append((8,octo[j]))

#print(cyclical)
                                      
#square list as key
for i in xrange(0,len(squ)):
    for j in xrange(0,len(tri)):
        if str(squ[i])[2:] == str(tri[j])[:2]:
            if int(str(tri[j])[2:])>=10:
                cyclical[4,squ[i]].append((3,tri[j]))
    for j in xrange(0,len(pen)):
        if str(squ[i])[2:] == str(pen[j])[:2]:
            if int(str(pen[j])[2:])>=10:
                cyclical[4,squ[i]].append((5,pen[j]))
    for j in xrange(0,len(hexa)):
        if str(squ[i])[2:] == str(hexa[j])[:2]:
            if int(str(hexa[j])[2:])>=10:
                cyclical[4,squ[i]].append((6,hexa[j]))
    for j in xrange(0,len(hep)):
        if str(squ[i])[2:] == str(hep[j])[:2]:
            if int(str(hep[j])[2:])>=10:
                cyclical[4,squ[i]].append((7,hep[j]))
    for j in xrange(0,len(octo)):
        if str(squ[i])[2:] == str(octo[j])[:2]:
            if int(str(octo[j])[2:])>=10:
                cyclical[4,squ[i]].append((8,octo[j]))
    

#pentagonal list as key
for i in xrange(0,len(pen)):
    for j in xrange(0,len(tri)):
        if str(pen[i])[2:] == str(tri[j])[:2]:
            if int(str(tri[j])[2:])>=10:
                cyclical[5,pen[i]].append((3,tri[j]))
    for j in xrange(0,len(squ)):
        if str(pen[i])[2:] == str(squ[j])[:2]:
            if int(str(squ[j])[2:])>=10:
                cyclical[5,pen[i]].append((4,squ[j]))
    for j in xrange(0,len(hexa)):
        if str(pen[i])[2:] == str(hexa[j])[:2]:
            if int(str(hexa[j])[2:])>=10:
                cyclical[5,pen[i]].append((6,hexa[j]))
    for j in xrange(0,len(hep)):
        if str(pen[i])[2:] == str(hep[j])[:2]:
            if int(str(hep[j])[2:])>=10:
                cyclical[5,pen[i]].append((7,hep[j]))
    for j in xrange(0,len(octo)):
        if str(pen[i])[2:] == str(octo[j])[:2]:
            if int(str(octo[j])[2:])>=10:
                cyclical[5,pen[i]].append((8,octo[j]))


#hexagonal list as key
for i in xrange(0,len(hexa)):
    for j in xrange(0,len(tri)):
        if str(hexa[i])[2:] == str(tri[j])[:2]:
            if int(str(tri[j])[2:])>=10:
                cyclical[6,hexa[i]].append((3,tri[j]))
    for j in xrange(0,len(squ)):
        if str(hexa[i])[2:] == str(squ[j])[:2]:
            if int(str(squ[j])[2:])>=10:
                cyclical[6,hexa[i]].append((4,squ[j]))
    for j in xrange(0,len(pen)):
        if str(hexa[i])[2:] == str(pen[j])[:2]:
            if int(str(pen[j])[2:])>=10:
                cyclical[6,hexa[i]].append((5,pen[j]))
    for j in xrange(0,len(hep)):
        if str(hexa[i])[2:] == str(hep[j])[:2]:
            if int(str(hep[j])[2:])>=10:
                cyclical[6,hexa[i]].append((7,hep[j]))
    for j in xrange(0,len(octo)):
        if str(hexa[i])[2:] == str(octo[j])[:2]:
            if int(str(octo[j])[2:])>=10:
                cyclical[6,hexa[i]].append((8,octo[j]))



#heptagonal list as key
for i in xrange(0,len(hep)):
    for j in xrange(0,len(tri)):
        if str(hep[i])[2:] == str(tri[j])[:2]:
            if int(str(tri[j])[2:])>=10:
                cyclical[7,hep[i]].append((3,tri[j]))
    for j in xrange(0,len(squ)):
        if str(hep[i])[2:] == str(squ[j])[:2]:
            if int(str(squ[j])[2:])>=10:
                cyclical[7,hep[i]].append((4,squ[j]))
    for j in xrange(0,len(pen)):
        if str(hep[i])[2:] == str(pen[j])[:2]:
            if int(str(pen[j])[2:])>=10:
                cyclical[7,hep[i]].append((5,pen[j]))
    for j in xrange(0,len(hexa)):
        if str(hep[i])[2:] == str(hexa[j])[:2]:
            if int(str(hexa[j])[2:])>=10:
                cyclical[7,hep[i]].append((6,hexa[j]))
    for j in xrange(0,len(octo)):
        if str(hep[i])[2:] == str(octo[j])[:2]:
            if int(str(octo[j])[2:])>=10:
                cyclical[7,hep[i]].append((8,octo[j]))



#octagonal list as key
for i in xrange(0,len(octo)):
    for j in xrange(0,len(tri)):
        if str(octo[i])[2:] == str(tri[j])[:2]:
            if int(str(tri[j])[2:])>=10:
                cyclical[8,octo[i]].append((3,tri[j]))
    for j in xrange(0,len(squ)):
        if str(octo[i])[2:] == str(squ[j])[:2]:
            if int(str(squ[j])[2:])>=10:
                cyclical[8,octo[i]].append((4,squ[j]))
    for j in xrange(0,len(pen)):
        if str(octo[i])[2:] == str(pen[j])[:2]:
            if int(str(pen[j])[2:])>=10:
                cyclical[8,octo[i]].append((5,pen[j]))
    for j in xrange(0,len(hexa)):
        if str(octo[i])[2:] == str(hexa[j])[:2]:
            if int(str(hexa[j])[2:])>=10:
                cyclical[8,octo[i]].append((6,hexa[j]))
    for j in xrange(0,len(hep)):
        if str(octo[i])[2:] == str(hep[j])[:2]:
            if int(str(hep[j])[2:])>=10:
                cyclical[8,octo[i]].append((7,hep[j]))












