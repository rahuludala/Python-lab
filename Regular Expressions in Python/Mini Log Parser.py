import re

log = """[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
"""

p = r'\[(?P<timestamp>.*?)\] (?P<level>\w+) user=(?P<user>\w+) msg="(?P<msg>.*?)"'

entries = []

for m in re.finditer(p, log):
    entries.append(m.groupdict())

print(entries)

for level in ["ERROR", "WARN", "INFO"]:
    print(level, len(re.findall(level, log)))

hidden = re.sub(r"user=\w+", "user=<hidden>", log)
print(hidden)
