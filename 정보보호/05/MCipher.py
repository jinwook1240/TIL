#!/usr/bin/python3
from Crypto.Cipher import AES

BS = 16
pad = lambda s : s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def setAES(key, iv):
 cipher = AES.new(key, AES.MODE_CBC, iv)#counter = lambda : 
 return cipher

def AES_Encrypt(cipher, data):
 message = pad(data)
 return cipher.encrypt(message)

def AES_Decrypt(cipher, data):
 return unpad(cipher.decrypt(data))