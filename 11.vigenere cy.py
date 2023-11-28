import string
main=string.ascii_lowercase
pt=input("Enter the message: ")
key=input("Enter the key: ")
index=0
ct=""
pt=pt.lower()
key=key.lower()
for c in pt:
    if c in main:
        off=ord(key[index])-ord('a')
        en=(ord(c)-ord('a')+off)%26
        e=chr(en+ord('a'))
        ct+=e
        index=(index+1)%len(key)
    else:
        ct+=c
print("plain text: ",pt)
print("cipher text: ",ct)

