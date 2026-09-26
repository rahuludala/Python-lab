import re

text = "Today is 13/09/2026 and tomorrow is 14/09/2026"

dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print(dates)

result = re.sub(
    r"(\d{2})/(\d{2})/(\d{4})",
    r"\3-\2-\1",
    text
)

print(result)
