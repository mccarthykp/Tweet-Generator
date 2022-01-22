import random, sys

def sentence_from_file():
  myfile = open('/usr/share/dict/words')
  content_of_file = myfile.read()

  # push inputted number of random words into words_list

  myfile.close()

words_list = []

sentence_from_file()

