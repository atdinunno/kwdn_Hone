import requests
from bs4 import BeautifulSoup
from collections import Counter
import string
#import re
#from nltk import word_tokenize

#TAG_RE = re.compile(^)

#get url request and text content from html
r = requests.get('https://en.wikipedia.org/wiki/Pickles')
html = r.text
soup = BeautifulSoup(html, 'html5lib')
#texts = soup.findAll(text=True)

for item in soup(['style', 'script', '[document]', 'head', 'title']):
    item.extract()

split_text_list = soup.getText().lower().split()

split_text_list = [''.join(c for c in s if c not in string.punctuation) for s in split_text_list]

#create counter object and use most_common() method
cnt = Counter()
for x in split_text_list:
    cnt[x] += 1

#sort by most common
freq_word_tuple = cnt.most_common()
print(freq_word_tuple)
list_each_count = [x[1] for x in freq_word_tuple]
total_word_count = sum(list_each_count)
list_each_density = [x[1]/total_word_count for x in freq_word_tuple]

temp_list = []
for x in freq_word_tuple:
    temp_list.append(x)

main_list = [list(x) for x in temp_list]

test = list(list_each_density)

i=0
while i < len(main_list):
    for x in main_list:
        x.append(test[i])
        i +=1

def numUniqueWords():
    #get number of unique words in list_of_lists
    num_unique_words = len(main_list)
    return num_unique_words

print(main_list, '\n\nUnique Words: ' + str(numUniqueWords()) + ' Total Words: ' + str(total_word_count))
