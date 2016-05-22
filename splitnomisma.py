

def opennewfile(count):
    fw = open('nomisma' + str(count), 'w', encoding="utf8")
    return fw


count = 1
f = open('','r',encoding="utf8")
fw = opennewfile(count)

lines = f.readlines()

for line in lines:
    if not line.find("</record>"):
        print(line,file=fw)
    if line.find("</record>"):
        print(line,file=fw)
        fw.close()
        count += 1
        fw = opennewfile(count)

