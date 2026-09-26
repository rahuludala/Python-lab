import re

p = r"^[A-Za-z_]\w*$"

for x in ["_count2", "2fast", "total_sum"]:
    print(x, bool(re.fullmatch(p, x)))
