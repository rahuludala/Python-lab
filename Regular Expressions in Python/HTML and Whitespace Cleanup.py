import re

def clean_text(html):
    html = re.sub(r"<.*?>", "", html)
    return re.sub(r"\s+", " ", html).strip()

s = "<p>Hello   <b>World</b></p>\n Welcome"
print(clean_text(s))
