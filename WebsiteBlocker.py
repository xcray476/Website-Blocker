from datetime import datetime


sites_to_block = [
    'www.foxnews.com','74.120.97.0'
]

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def block_websites(start_hour , end_hour):
    while True:
       if datetime(datetime.now().year, datetime.now().month, datetime.now().day,start_hour) < datetime.now() < datetime (datetime.now().year, datetime.now().month, datetime.now().day,end_hour):
           print("Do the work ....")
           with open("C:\Windows\System32\drivers\etc\hosts", 'r+') as hostfile:
               host = hostfile.read()
               for site in sites_to_block:
                   if site not in host:
                       hostfile.write(redirect+''+site+'\n') 
    else: 
                    with open ("C:\Windows\System32\drivers\etc\hosts", '+r') as hostfile: hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any (site in host for site in sites_to_block):hostfile.write(host)
                        hostfile.truncate()
print('Good time')              
datetime


if __name__=='__main__':
    block_websites(17, 18)

