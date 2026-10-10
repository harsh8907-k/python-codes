word = ["donkey","he"]

with open("file.txt","r")as f:
    content = f.read()

contentnew = content.replace(word,"######")    

with open("donkey.txt","w")as f:
    content = f.write(contentnew)