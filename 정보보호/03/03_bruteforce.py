#!/usr/bin/python3

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
  print('Enter the key')
  key=input()
  return key

def str_xor(keyValue, message):
 translated = b''
 for idx, var in enumerate(keyValue):
  #print(ord(var), '^', message[idx], '=', ord(var)^message[idx])
  translated+=bytes([ord(var)^message[idx]])
 return translated

def encrypt(mode, fileName, key):
 keyValue = ''
 outputFileName = 'encrypt.txt'
 if mode[0] is 'd':
  outputFileName = 'decrypt.txt'
 outputFile = open(outputFileName, 'wb')
 inputFile = open(fileName, 'rb')
 message = inputFile.read()
 for i in range(len(message)//3):# 3: 키 길이
  keyValue += key
 translated = str_xor(keyValue, message)
 outputFile.write(translated)
 outputFile.close()
 inputFile.close()
 print('En(De)cryption complete')

def bruteforce():
 mode = getMode()
 #key = getKey()
 key = [ord('a'),ord('a'),ord('a')]
 fileName = getFileName()
 outputFileName = 'encrypt.txt'
 if mode[0] is 'd':
  outputFileName = 'decrypt.txt'
 bruteForceFile = open(outputFileName+'.bruteforce', 'a')
 while key[0]<=ord('z'):
  while key[1] <= ord('z'):
   while key[2] <= ord('z'):
    encrypt(mode, fileName, bytes(key).decode())
    outputFile = open(outputFileName, 'rb')
    result = outputFile.read()
    outputFile.close()
    bruteForceFile.write(bytes(key).decode()+'\t'+result.decode()+'\n')
    key[2] += 1
   key[2] = ord('a')
   key[1] += 1
  key[1] = ord('a')
  key[0] += 1
 bruteForceFile.close()
bruteforce()
