import secrets

pw = ""
Zeichen ="QWERTZUIOPASDFGHJKLYXCVBNMweqrtzuiopasdfghjklyxcvbnm-.,12345666667890ß!"
laenge = int(input("Bitte Passwortlänge eingeben: "))

for _ in range(laenge):
    pw = pw+secrets.choice(zeichen)
    
print(pw)