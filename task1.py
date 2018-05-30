"""
Counts the most common words
in a given text.
"""

from __future__ import print_function
import re
from collections import Counter

string_to_check = 'Otaniemi is the home of the Aalto ...' \
                  'University engineering schools campus, thus "Otaniemi" is often used as a synonym for Aalto.'

# find all words in the string
words = re.findall('[a-zA-Z_]+', string_to_check)

# counts the number each time a word appears
word_counts = Counter(words)

print('words in given text are {}'.format(dict(word_counts)))
