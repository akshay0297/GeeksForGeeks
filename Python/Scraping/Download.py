import requests as rq

print("Downloading.....")
res = rq.get('http://textfiles.com/computers/CYBERSPACE/cybcraft.txt')

print (type(res))

if res.status_code == rq.codes.ok:
    print("Status OK !")

print(len(res.text))

try :
    res.raise_for_status()
    dummy = open('Downloaded.txt' , 'wb')
    for i in res.iter_content(13000):
        dummy.write(i)
    dummy.close()
except Exception as exe:
    print("Exception Thrown :: \n %s " %(exe))

print(res.text[:])

