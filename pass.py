#! /usr/bin/python3
import random
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
f = open("/home/jonathan/Dropbox/abcdefg", "a")
key='' //enter key
cipher = AES.new(key,AES.MODE_CFB, '1234567890123456')
decryptor = AES.new(key, AES.MODE_CFB, '9348493023950485')
def checkargumentistoolong(argument):
    if len (argument) != 3 and argument[1] != 'get':
        return True
    
PAD = "X"

def key_hash(key):
    return SHA256.new(key.encode()).digest()

def encrypt(text, key):
    while len(text) % 16 != 0:
        text += PAD
    cipher = AES.new(key_hash(key))
    encrypted = cipher.encrypt(text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt(text, key):
    cipher = AES.new(key_hash(key))
    plain = cipher.decrypt(base64.b64decode(text))
    return plain.decode().rstrip(PAD)

if(checkargumentistoolong(sys.argv)):
    print('incorrect usage')
   

if(sys.argv[1] == 'get'):
  with open('/home/jonathan/Dropbox/abcdefg','r') as openfileobject:
      for line in openfileobject:
       print(decrypt(line,'6535770394059654'))
   

    
    

else:  
 string = "1234567890!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

 thelist = list(string)

 pw = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]


 for x in range(1,20):
    
     pw[x] = (thelist[random.randint(1, 69)])
 password= ''.join(pw)
 toencode = "HOST: " + sys.argv[1] + " USERNAME: " + sys.argv[2] + " PASSWORD: " + password
 f.write(encrypt(toencode,'6535770394059654'))
 f.write('\n')
 f.close()

 print("Successfully written. Type the command python pass.py get to retrieve your password.")

      
 
 

