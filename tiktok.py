import requests
import time

rr = requests.session()
from user_agent import generate_user_agent

print("""
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗          
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝          
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝           
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗           
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗          
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝          

 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

instagram : 7snhacker""")
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": f"{generate_user_agent()}",
    "Connection": "close",
    "Host": "www.tiktok.com",
    "Accept-Encoding": "gzip, deflate",
    "Cache-Control": "max-age=0"

}
times = float(input('sleep : '))
us = open('username.txt', 'r')
while True:
    time.sleep(times)
    user = us.readline().split("\n")[0]
    url = f"https://www.tiktok.com/@{user}"
    req = rr.get(url, headers=headers)
    if req.status_code == 404:
        print(f'{user} : Available')
        with open('Available.txt',"a") as Available:
            Available.write(user+'\n')
    elif req.status_code == 200:
        print(f'{user} : Not Available')
