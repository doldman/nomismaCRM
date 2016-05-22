import re

f = open('nomisma.rdf','r',encoding="utf8")
mylinelist = f.readlines()

myDescription = ''
myrdf = ''
myskos = ''
mydcterms = ''
mydate = ''
mynmo = ''
myObverse = ''
myReverse = ''
mylegendObverse = ''
mylegendReverse = ''
mydescriptionObverse = ''
mydescriptionReverse = ''
myportraitObverse = ''
myportraitReverse = ''
viewnumber = 0
obversecount = 0
reversecount = 0
out = open('nomismaout.xml','a',encoding="utf8")
print('<?xml version="1.0" encoding="UTF-8"?>',file=out)
print('<nomisma>',file=out)

for line in mylinelist:

    m = re.search(r'<(.*):(.*) (.*):(.*)=\"(.*)\"',line)
    m1 = re.search(r'<(.*):(.*) (.*):(.*)=\"(.*)\">(.*)(<)',line)
    m2 =  re.search(r'<(.*):(.*)>(.*)</(.*):(.*)>',line)
    m3 =  re.search(r'</record>',line)
    m4 = re.search(r'<(.*):(.*) (.*):(.*)=\"(.*)\">(\d*)(<.*)', line)

    if m:
        if m.group(1) == 'nmo' and m.group(2) == 'hasObverse':
            myObverse = '\t<' + m.group(2) + 'details' + '>\n'
            obversecount += 1
        if m.group(1) == 'nmo' and m.group(2) == 'hasReverse':
            myReverse = '\t<' + m.group(2) + 'details' + '>\n'
            reversecount += 1
        if m.group(1) == 'rdf' and m.group(2) == 'Description':
            viewnumber += 1
        if m.group(1) == 'nmo' and m.group(2) != 'hasPortrait' and m.group(2) != 'hasStartDate' and m.group(2) != 'hasEndDate':
            mynmo += '\t<' + m.group(2) + '>' + m.group(5) + '</' + m.group(2) + '>\n'
        if viewnumber == 1:
            if m.group(1) == 'nmo' and m.group(2) == 'hasPortrait':
                myportraitObverse += '\t\t<' + m.group(2) + '>' + m.group(5) + '</' + m.group(2) + '>\n'
        if viewnumber == 2:
            if m.group(1) == 'nmo' and m.group(2) == 'hasPortrait':
                myportraitReverse += '\t\t<' + m.group(2) + '>' + m.group(5) + '</' + m.group(2) + '>\n'
        if m.group(1) == 'rdf' and m.group(2) != 'Description':
            myrdf += '\t<' + m.group(2) + '>' + m.group(5) + '</' + m.group(2) + '>\n'
        if m.group(1) == 'dcterms' and m.group(3) != 'xml':
            mydcterms += '\t<' + m.group(2) + '>' + m.group(5) + '</' + m.group(2) + '>\n'

    if m4:
         if m.group(2) == 'hasStartDate' or m.group(2) == 'hasEndDate':
            mydate += '\t<' + m4.group(2) + '>' + m4.group(6) + '</' + m4.group(2) + '>\n'


    if m1:
        if m1.group(1) == 'skos':
            myskos += '\t<' + m1.group(2) + '>' + m1.group(6) + '</' + m1.group(2) + '>\n'

    if m2:
        if m2.group(5) == 'hasLegend':
            if viewnumber == 1:
                mylegendObverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'
            if viewnumber == 2:
                mylegendReverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'
        if m2.group(5) == 'description':
            if viewnumber == 1:
                mydescriptionObverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'
            if viewnumber == 2:
                mydescriptionReverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'
        if m2.group(5) == 'hasPortrait':
            if viewnumber == 1:
                myportraitObverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'
            if viewnumber == 2:
                myportraitReverse = '\t\t<' + m2.group(5) + '>' + m2.group(3) + '</' + m2.group(5) + '>\n'

    if m3:

        #print('<record>\n' + mynmo + mydate + myskos + myrdf + myObverse + mylegendObverse + mydescriptionObverse + myportraitObverse + '\t</hasObversedetails>\n' + myReverse + mylegendReverse + mydescriptionReverse + myportraitReverse + '\t</hasReversedetails>\n' + '</record>')
        if obversecount == 1 and reversecount == 1:
            print('<record>\n' + mynmo + mydate + myskos + myrdf + myObverse + mylegendObverse + mydescriptionObverse + myportraitObverse + '\t</hasObversedetails>\n' + myReverse + mylegendReverse + mydescriptionReverse + myportraitReverse + '\t</hasReversedetails>\n' + '</record>',file=out)
        if obversecount == 1 and reversecount == 0:
            print('<record>\n' + mynmo + mydate + myskos + myrdf + myObverse + mylegendObverse + mydescriptionObverse + myportraitObverse + '\t</hasObversedetails>\n' + myReverse + mylegendReverse + mydescriptionReverse + myportraitReverse + '</record>',file=out)
        if obversecount == 0 and reversecount == 1:
            print('<record>\n' + mynmo + mydate + myskos + myrdf + myObverse + mylegendObverse + mydescriptionObverse + myportraitObverse + myReverse + mylegendReverse + mydescriptionReverse + myportraitReverse + '\t</hasReversedetails>\n' + '</record>',file=out)
        if obversecount == 0 and reversecount == 0:
            print('<record>\n' + mynmo + mydate + myskos + myrdf + myObverse + mylegendObverse + mydescriptionObverse + myportraitObverse + myReverse + mylegendReverse + mydescriptionReverse + myportraitReverse + '</record>',file=out)
        myDescription = ''
        myrdf = ''
        myskos = ''
        mydcterms = ''
        mynmo = ''
        myObverse = ''
        myReverse = ''
        mydate = ''
        mylegendObverse = ''
        mylegendReverse = ''
        mydescriptionObverse = ''
        mydescriptionReverse = ''
        myportraitObverse = ''
        myportraitReverse = ''
        viewnumber = 0
        obversecount = 0
        reversecount = 0

print('</nomisma>',file=out)
#print('</nomisma>')
f.close()

out.close
















