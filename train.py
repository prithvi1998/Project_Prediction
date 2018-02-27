import nltk
import csv

def count1(tag):
    """ This function counts the number of occurance of a given tag in  corpus"""
    count = 0
    for i in m:
        if i[1] == tag:
            count = count + 1
    return count

def count2(tag1,tag2):
    """This function counts the number of occurance of a given bigram in  corpus"""
    count = 0
    isfirst = 1
    for i in m:
        if isfirst != 1 :
            if prev[1] == tag1 and i[1] == tag2 :
                count = count+1
        else:
            isfirst = 0
        prev = i
    return count

def count3(word,tag):
    """This function counts the number of occurance of a word with particular tag"""
    count = 0
    for i in m:
        if isfirst != 1 :
            if i[1] == tag1 and i[0] == word :
                count = count+1
    return count

def transition_prob():
    """This function calculates and fills transition table"""
    for i in range(12):
        for j in range(12):
            print j
            tag1 = tags[i]
            tag2 = tags[j]
            x = count1(tag2)
            y = count2(tag2,tag1)
            transition_table[i].append(float(y)/float(x))
        writer.writerow(transition_table[i])
    return

def emission_prob():
    """This function calculates and fills emission table"""
    for i in range(vocab_count):
        for j in range(12):
            print j
            tag = tags[j]
            x = count1(tag)
            y = count3(vocab[i],tag)
            emission_table[i].append(float(y)/float(x))
            writer1.writerow(emission_table[i])
        return

m = nltk.corpus.brown.tagged_words(tagset = 'universal')

# tags = ["NOUN","VERB","DET","ADJ","PRON","PRT","NUM","CONJ","ADV","ADP","X","."]

#transition_table[][]
transition_table = []
for i in range(12):
    transition_table.append([])

#emission_table[][]
vocab = []
vocab_count = 0
for i in m :
    if i[0] not in vocab:
        vocab.append(i[0])
        vocab_count = vocab_count + 1

print "asdasd"

emission_table = []
for i in range(vocab_count):
    emission_table.append([])

bigrams = nltk.bigrams(m)

file_out = open("transition_table.csv","wb")
writer = csv.writer(file_out, delimiter=" ", quotechar='"', quoting=csv.QUOTE_ALL)

file_out1 = open("emission_table.csv","wb")
writer1 = csv.writer(file_out, delimiter=" ", quotechar='"', quoting=csv.QUOTE_ALL)

# transition_prob()
emission_prob()

# print transition_table
print emission_table

print vocab_count
