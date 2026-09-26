import re

s = "2024-06-01 08:15:32 ERROR Disk full"

p = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<msg>.*)"

m = re.match(p, s)

print(m.group("date"))
print(m.group("time"))
print(m.group("level"))
print(m.group("msg"))
