import requests as req
from colorama import Fore
print('''
            #################################################
            #################################################
            ##########  Ashiyane ADMINPAGE FindeR  ##########
            ############ CreaTed BY Mobin_dan‌‌ ‌ ‌‌    ##########
            ############  WE LOVE IRAN           ############
            ############ t.me/termux_learning    ############
            #################################################
            #################################################

''')

url=input("Enter Target's WebSite Url:")
try:
    OF=open("admin.txt","r")
    for line in OF:
        url2=url +"/"+ line
        site=req.get(url2)
        if site.status_code==200:
           print(Fore.GREEN+"[+]FOUND "+url2)
        else:
           print(Fore.RED+"[-]NOT FOUND "+url2)
    OF.close()
except KeyboardInterrupt:
   print(Fore.GREEN)
   print("Bye Bye !!!")

