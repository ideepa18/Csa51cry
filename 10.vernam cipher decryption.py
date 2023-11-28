def ver(ct,key):
    ct=ct.lower()
    key=key.lower()
    ct=ct.replace(" ","")
    key=key.replace(" ","")
    pt=""
    for i in range(len(ct)):
        n1=ord(ct[i])-97
        n2=ord(key[i])-97
        s=chr((((n1-n2)+26)%26)+97)
        pt+=s
    print("Decrypted message is: ",pt)
pt=input("Enter the message to be decrypted: ")
key=input("Enter the one time pad: ")
ver(pt,key)
