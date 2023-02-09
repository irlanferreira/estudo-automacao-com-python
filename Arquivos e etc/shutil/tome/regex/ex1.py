import re

#text = input(str(":"))

telereg = re.compile(r'''(

(\d{2,3})?
(-)?
(\d{5})

)''', re.VERBOSE)

emailreg = re.compile(r'''(

[a-zA-z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})

)''', re.VERBOSE)

telefones = []
for t in telereg.findall("My  phone is 81984192135 and 81988247639"):
  telefones.append(t[0])

emails = []
for e in emailreg.findall("My email is irlanferreiradasilva2@gmail.com, and also cristianafdsana@gmail.com"):
  emails.append(e[0])



res = "Phones founded:\n"
for i in telefones:
  res+=f"{i}\n"
res+="\nEmails founded:\n"
for i in emails:
  res+=f"{i}\n"
print(res)