import requests

msg = "hello"
bytelist = bytearray(msg,encoding="utf-8")
print(bin)
bits = []
for i in bytelist:
    bits.append(bin(i))
print(bits)

for element in bits:
    for i in range(2,9):
        if int(element[i]) == 1:
            requests.get("http://localhost:8080",cookies= {"name1" : "1", "name2" : "2"})
        else:
            requests.get("http://localhost:8080",cookies= {"name1" : "1"})
#requests.get("http://localhost:8080",cookies= {"name1" : "1"})
#requests.get("http://localhost:8080",cookies= {"name1" : "1", "name2" : "2"})