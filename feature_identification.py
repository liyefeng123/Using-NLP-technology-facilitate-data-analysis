import nltk,re, pprint
import os
reason_term_list = []
status_term_list = []
All_sentences = []
f = open("./Msc-twitter-data/data/accident_term.txt")
line = f.readline()
while line:
    if line[-1:] == '\n':
        line = line[:-1]
    reason_term_list.append(line)  # 后面跟 ',' 将忽略换行符
    line = f.readline()
f.close()

f = open("./Msc-twitter-data/data/status_term.txt")
line = f.readline()
while line:
    if line[-1:] == '\n':
        line = line[:-1]
    status_term_list.append(line)  # 后面跟 ',' 将忽略换行符
    line = f.readline()
f.close()

print('term',reason_term_list)
def identifiy_feature(sentences,sentences_row):
    senthasLocation = []
    senthasReason = []
    senthasStatus = []
    senthasDescribe = 1
    num_sent = len(sentences)
    #detect location term
    for i in range(num_sent):
        tree = nltk.ne_chunk(sentences[i])
        All_sentences.append(i)
        for subtree in tree.subtrees():
            if subtree.label() == 'GPE' or subtree.label() == 'PERSON':
                if i not in senthasLocation:
                    senthasLocation.append(i)
    print('sen',senthasLocation)
    #detect accident term
    for i in range(num_sent):
        tree_node = nltk.ne_chunk(sentences[i]).flatten()
        for j in tree_node:
            if j[0] in status_term_list:
                if i not in senthasStatus:
                    senthasStatus.append(i)
            if j[0] in reason_term_list:
                if i not in senthasReason:
                    senthasReason.append(i)
    TRS_1 = list(set(senthasLocation).intersection(set(senthasStatus)))
    TRS_2 = list(set(senthasLocation).intersection(set(senthasReason)))
    TRS = list(set(TRS_1).union(set(TRS_2)))
    NO_TRS = list(set(All_sentences).difference(TRS))
    TRS_Sentences = []
    NO_TRS_Sentences = []
    file = open('./Msc-twitter-data/data/training_data.txt', 'w')
    for i in TRS:
        temp_sentences = ''
        TRS_Sentences.append(sentences_row[i])
        for j in range(len(sentences_row[i])):
            temp_sentences = temp_sentences + ' ' + sentences_row[i][j][0]
        print('temp',temp_sentences)
        file.write('TRS:'+temp_sentences+ '\n');
    for i in NO_TRS:
        temp_sentences = ''
        NO_TRS_Sentences.append(sentences_row[i])
        for j in range(len(sentences_row[i])):
            temp_sentences = temp_sentences + ' ' + sentences_row[i][j][0]
        file.write('NO_TRS:'+temp_sentences + '\n');
    file.close()
    return
