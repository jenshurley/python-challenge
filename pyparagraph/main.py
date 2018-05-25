import re
import sys

file = sys.argv[1]

with open(file) as f: 
    data = f.read()
    sents = re.split("\.|\?|!", data )
    sents = [x.strip() for x in sents if len(x) > 2] 

sentlist = []
for s in sents:
    st = list(s)
    sentlist.append("".join(st))

sentence_length = [len(sents.replace(' ','')) for sents in sentlist]  
#TODO - in characters still incl spaces and commmas, see above which is redundant. write list compr
#TODO rename variables for clarity
#TODO i don't think the replace is in the right place
words_in_sents = [sents.split(' ') for sents in sentlist]

l_sent = [len(words) for words in words_in_sents]

ave_sent_length = sum(l_sent)/len(l_sent)

flattenend_words = [x for w in words_in_sents for x in w]

word_lengths = [len(w) for w in flattenend_words]

ave_word_length = int(sum(word_lengths)/len(word_lengths))

#TODO string formatting here
print("AveWordLength=", ave_word_length,"letters | AveSentLength=", ave_sent_length, "words | LenWords=", sum(l_sent), "| Sentences=", len(sents))
print(sentence_length)