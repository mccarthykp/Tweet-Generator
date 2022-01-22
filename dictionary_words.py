import random, sys

def sentence_from_file():
  myfile = open('/usr/share/dict/words')
  content_of_file = myfile.readlines()

  num_words = int(sys.argv[1])
  words_list = []

  for index in range(num_words):
    # push inputted number of random words into words_list
    rand_num = random.randint(0, len(content_of_file))
    words_list.append(content_of_file[rand_num].strip('\n'))
    
  sentence = ' '
  print(sentence.join(words_list))
  myfile.close()

if __name__ == '__main__':
  sentence_from_file()

# augment function to take in two arguments = the file and the inputted number
