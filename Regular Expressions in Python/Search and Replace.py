import re

text = "Mail john@gmail.com or ram@yahoo.com"
result = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "[EMAIL HIDDEN]", text)
print(result)
