import random, sys

words = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]

def rearrange():
  random.shuffle(words)
  print(words[0] + ' ' + words[1] + ' ' + words[2] + ' ' + words[3])

rearrange()

  