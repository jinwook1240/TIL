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
  key=input().lower()
  valid = True
  for character in key:
   if not (ord(character) >= ord('a') and ord(character) <= ord('z')):
     return
  return key

def shift(symbol, key):
 shifted = ''
 if ord(symbol)>=ord('a') and ord(symbol)<=ord('z'):
  shifted = chr(ord(symbol)+key)
  if shifted >ord('z'):
   shifted -= (ord('a')-1)
  elif shifted < ord('a'):
   shifted += (ord('a')-1)
 elif ord(symbol)>=ord('A') and ord(symbol)<=ord('Z'):
  shifted = chr(ord(symbol)+key)
  if shifted >ord('Z'):
   shifted -= (ord('A')-1)
  elif shifted < ord('A'):
   shifted += (ord('A')-1)
 return shifted

def encrypt(mode, fileName, key):
 key_int = []
 for idx, keysymbol in enumerate(key):
  tmp = ord(keysymbol)-ord('a')
  if mode[0] is 'd':
   tmp = -tmp
  key_int.append(tmp)
  print(tmp)
 outputFileName = 'encrypt.txt'
 if mode[0] is 'd':
  outputFileName = 'decrypt.txt'
 translated = ''
 outputFile = open(outputFileName, 'w')
 inputFile = open(fileName, 'r')
 message = inputFile.read()
 
 for idx, symbol in enumerate(message):
  translated += shift(symbol, key_int[idx%len(key_int)])
  print(symbol, translated, key_int[idx%len(key_int)])
 
 outputFile.write(translated)
 outputFile.close()
 inputFile.close()
 print('En(De)cryption complete')
 
mode = getMode()
key = getKey()
fileName = getFileName()
encrypt(mode, fileName, key)
