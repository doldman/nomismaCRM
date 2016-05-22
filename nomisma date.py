
import re

f = open('nomismaObjectout.nt','r',encoding='utf8')
out = open('nomismaObjectoutdate.nt','a',encoding='utf8')

mylines = f.readlines()

for line in mylines:
    m1 = re.search(r'(<http://www.cidoc-crm.org/cidoc-crm/P82a_begin_of_the_begin>)(.*")(\d*)(")', line)
    m2 = re.search(r'(<http://www.cidoc-crm.org/cidoc-crm/P82b_end_of_the_end>)(.*")(\d*)(")', line)


    if m1:
        line = re.sub(r'(<http://www.cidoc-crm.org/cidoc-crm/P82a_begin_of_the_begin>)(.*")(\d*)(")',m1.group(1) + ' "'  + m1.group(3) + '-01-01"^^xsd:date',line.rstrip())
        print(line,file=out)
    elif m2:
        line = re.sub(r'(<http://www.cidoc-crm.org/cidoc-crm/P82b_end_of_the_end>)(.*")(\d*)(")',m2.group(1) + ' "' + m2.group(3) + '-12-31"^^xsd:date',line.rstrip())
        print(line,file=out)
    else:
        print(line.rstrip(),file=out)

f.close()
out.close()





