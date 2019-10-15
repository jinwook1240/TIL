#!/usr/bin/python3
from Crypto.Cipher import AES
import base64
import os

BS = 16
pad = lambda s : s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

def getMode():
 while True:
  print('Enter either "encrypt" or "e" or "decrypt" or "d".')
  mode = input().lower()
  if mode in 'encrypt e decrypt d'.split():
   return mode
  else:
   print('the value you entered is invalid')

def getFileName():
 print('Enter your file name:')
 return input()

def crypto(mode, fileName):
 keyValue = ''
 iv = b'fdasafdsfdasfdas'
 key = 'thisisbadkeyokey'
 outputFileName = 'encrypt.txt'
 if mode[0] is 'd':
  outputFileName = 'decrypt.txt'
 
 translated = ''
 outputFile = open(outputFileName, 'wb')
 
 inputFile = open(fileName, 'rb')
 message = inputFile.read()
 ######
 obj = AES.new(key, AES.MODE_CTR, counter = lambda : iv)
 translated = b''
 if mode[0] is 'e':
  translated = obj.encrypt(message)
 elif mode[0] is 'd':
  translated = obj.decrypt(message)
 ######
 outputFile.write(translated)
 outputFile.close()
 inputFile.close()
 print('En(De)cryption complete')

mode = getMode()
fileName = getFileName()
crypto(mode, fileName)
