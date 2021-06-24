
print("""  _     ___ ____ _____ ____ _____ _   _ 
 | |   |_ _/ ___|_   _/ ___| ____| \ | |
 | |    | |\___ \ | || |  _|  _| |  \| |
 | |___ | | ___) || || |_| | |___| |\  |
 |_____|___|____/ |_| \____|_____|_| \_|
                                        """)
print("instagram : 7snhacker")
import string
import random
letters = string.ascii_lowercase
user = int(input("letter count : "))
r = open("username.txt", "w")
done = 0
li = 0
while li == 0:
    done += 1
    print(done)
    r.write(''.join(random.choice(letters) for i in range(user)) + '\n')

r.close()
