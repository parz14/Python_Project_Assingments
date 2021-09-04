import re
FILE = open("mail.txt", "r+")
next(FILE)
for mail_ids in FILE:
    if re.match("[a-z A-Z 0-9]+@gmail.com$", mail_ids):
        print("Valid")
    else:
        print("Not valid")
FILE.close()
