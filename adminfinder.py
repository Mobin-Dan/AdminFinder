import urllib
from colorama import Fore
print'''
            #################################################
            #################################################
            ##########  Ashiyane ADMINPAGE FindeR  ##########
            ############ CreaTed BY Mobin_dan‌‌ ‌ ‌‌    ##########
            ############  WE LOVE IRAN           ############
            #################################################
            #################################################

'''

url=raw_input("Enter Target's WebSite Url (ex:https/http://www.website.com): ")
try:
    OF=open("admin.txt","r")
    for line in OF:
        url2=url +"/"+ line
        site=urllib.urlopen(url2)
        if site.code==200:
           print(Fore.GREEN+"[+]FOUND "+url2)
        else:
           print(Fore.RED+"[-]NOT FOUND "+url2)
    OF.close()
except KeyboardInterrupt:
   print(Fore.GREEN)
   print "Bye Bye !!!"
   print "t.me/@World_warning"

