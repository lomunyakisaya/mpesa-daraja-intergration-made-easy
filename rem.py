import re
phone = "0712-243 978"
cleaned = re.sub(r"(\D)", "", phone)
print(cleaned)

#Find a word
message= "I love python and java"
