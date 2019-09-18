#!/usr/bin/python3
MAX_KEY_SIZE = 26

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

def getKey():
 key = 0
 while True:
  print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
  key=int(input())
  if(key>=1 and key <= MAX_KEY_SIZE):
   return key

def shift(symbol, key):
 shifted = 0
 if ord(symbol)>=ord('a') and ord(symbol)<=ord('z'):
  shifted = ord(symbol)+key
  if shifted > ord('z'):
   shifted = shifted-(ord('z')-ord('a')+1)
  elif shifted < ord('a'):
   shifted = shifted+(ord('z')-ord('a')+1)
 elif ord(symbol)>=ord('A') and ord(symbol)<=ord('Z'):
  shifted = ord(symbol)+key
  if shifted > ord('Z'):
   shifted = shifted-(ord('z')-ord('a')+1)
  elif shifted < ord('A'):
   shifted = shifted+(ord('z')-ord('a')+1)
 return chr(shifted)

def encrypt(mode, fileName, key):
 outputFileName = 'encrypt.txt'
 if mode[0] is 'd':
  key = -key
  outputFileName = 'decrypt.txt'
 translated = ''
 outputFile = open(outputFileName, 'w')
 inputFile = open(fileName, 'r')
 message = inputFile.read()
 
 for symbol in message:
  translated += shift(symbol, key)
 
 outputFile.write(translated)
 outputFile.close()
 inputFile.close()
 print('En(De)cryption complete')
 
mode = getMode()
key = getKey()
fileName = getFileName()
encrypt(mode, fileName, key)
