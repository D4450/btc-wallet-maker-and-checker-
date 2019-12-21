import blockchain
import requests
from bitcoin import *
from subprocess import call
from sys import platform

for i in range(10000):
    my_private_key = random_key()
    #print(my_private_key)
    my_private_key = random_key()
    my_public_key = privtopub(my_private_key)
    #print(my_public_key)
    my_bitcoin_address = pubtoaddr(my_public_key)
    x=my_bitcoin_address
    
  

    x=requests.get('https://blockchain.info/q/addressbalance/'+x)
    r=x.text


 
    
    #print(r)
    if r =="Invalid Bitcoin Address":
        print("invalid ")

    else:   
        if r=="0":

            print("number of checking : ",i ," balance is :",r)
            
        else:
            print(my_bitcoin_address)
            print("balance is-->  ", r , " satooshi")
            
    f = open('aa.txt', 'a')
    f.writelines(" +++ " + my_private_key + "\n +++ " + my_public_key+ "\n +++ " + my_bitcoin_address+"\n ### "+" BALANCE is : "+r+"\n --- \n")  # python will convert \n to os.linesep
    f.close()     
