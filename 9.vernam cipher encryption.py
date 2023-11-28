pt=input("Enter the message: ")
key=input("Enter the one time pad: ")
pt=pt.replace(" ","")
key=key.replace(" ","")
pt=pt.lower()
key=key.lower()
if(len(pt)!=len(key)):
    print("Lengths are different")
else:
    ct=""
    for i in range(len(pt)):
        k1=ord(pt[i])-97
        k2=ord(key[i])-97
        s=chr((k1+k2)%26+97)
        ct+=s
    print("Enrypted message is: ",ct)
