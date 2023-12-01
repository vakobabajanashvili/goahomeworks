janezas_razmi = ["alex rajavi", "anastasia feridze", "nika qatamadze", "nikoloz takidze", "nugzar turmanishvili", "roba amonashvili", "vako"]
supersia = []

for i in janezas_razmi:
    if i.lower().count("i")>=2:
        supersia.append(i.title())
for i in supersia:
    print(i)


for i in janezas_razmi:
    if len(i) <= 16:
        print(i.upper())