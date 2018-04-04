import re

infile = open('C:\Windows\System32\drivers\etc\services').read().splitlines()
ports = set()

for line in infile:
    if re.match(r"^(#|$)", line) or line.isspace():
        continue
    m = re.search("(?P<port>\d+)/(udp|tcp)", line)
    port = int(m.group('port'))
    if port > 200:
        break
    ports.add(port)

for i in range(201):
    if i not in ports:
        print(i)
