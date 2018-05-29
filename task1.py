"""
Counts the most common words
in a given text.
"""

from __future__ import print_function
import re
from collections import Counter

string_to_check = 'Otaniemi is the home of the Aalto University engineering schools campus, thus "Otaniemi" is often used as a synonym for Aalto.'

# find all words in the string
#TODO: type following code "words = re.findall('[a-zA-Z_]+', string_to_check)" below, as you type you get support from PyCharm

# counts the number each time a word appears
#TODO: type following code "word_counts = Counter(words)" below


print('words in given text are {}'.format(dict(word_counts)))
