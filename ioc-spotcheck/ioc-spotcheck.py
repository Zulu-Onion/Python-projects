dict = {}

logs = r'logs.txt'      #Need to use full path
iocs = r'iocs.txt'      #Need to use full path
logs = open(logs).readlines()
iocs = open(iocs).readlines()

for ioc in iocs:
    dict[ioc] = []

for ioc in dict.keys():
    for line in logs:
        if ioc in line:
            dict[ioc].append(line)

print(dict)
