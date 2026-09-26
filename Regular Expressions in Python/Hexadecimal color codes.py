import re

s = "#FFAA00 #000 #12FG45"
print(re.findall(r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?", s))
