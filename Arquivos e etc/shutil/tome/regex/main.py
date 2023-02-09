import re

frase = "Meu número é 81988247639, e também 81988247639"
reg = re.compile(r"(\d\d)?(\d){5}(-)?(\d){4}")
res = reg.findall(reg)
print(res)