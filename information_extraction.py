import nltk,re, pprint
import datetime
import pandas as pd
import feature_identification
import question_classifier.question_classifier as qc
from nltk.corpus import conll2000
content = ''
for line2 in open("./Msc-twitter-data/data/row_news.txt"):
    content = content + line2
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences_row = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences_row]
    #feature_identification.identifiy_feature(sentences,sentences)
    return sentences
def ie_named_entity_finding(pos_sent):
    named_entities_GPE = []
    named_entities_ORGANIZATION = []
    named_entities_PERSON = []
    named_entities_LOCATION = []
    named_entities_DATE = []
    named_entities_TIME = []
    named_entities_MONEY = []
    named_entities_PERCENT = []
    named_entities_FACILITY = []
    for i in pos_sent:
        tree = nltk.ne_chunk(i)
        print('tree',tree)
        for subtree in tree.subtrees():
            if subtree.label() == 'GPE':
                entity_GPE = ""
                for leaf in subtree.leaves():
                    entity_GPE = entity_GPE + leaf[0] + " "
                named_entities_GPE.append(entity_GPE.strip())
            if subtree.label() == 'ORGANIZATION':
                entity_ORG = ""
                for leaf in subtree.leaves():
                    entity_ORG = entity_ORG + leaf[0] + " "
                named_entities_ORGANIZATION.append(entity_ORG.strip())
            if subtree.label() == 'PERSON':
                entity_PER = ""
                for leaf in subtree.leaves():
                    entity_PER = entity_PER + leaf[0] + " "
                named_entities_PERSON.append(entity_PER.strip())
            if subtree.label() == 'LOCATION':
                entity_LOC = ""
                for leaf in subtree.leaves():
                    entity_LOC = entity_LOC + leaf[0] + " "
                named_entities_LOCATION.append(entity_LOC.strip())
            if subtree.label() == 'DATE':
                entity_DATE = ""
                for leaf in subtree.leaves():
                    entity_DATE = entity_DATE + leaf[0] + " "
                named_entities_DATE.append(entity_DATE.strip())
            if subtree.label() == 'TIME':
                entity_TIME = ""
                for leaf in subtree.leaves():
                    entity_TIME = entity_TIME + leaf[0] + " "
                named_entities_TIME.append(entity_TIME.strip())
            if subtree.label() == 'MONEY':
                entity_MONEY = ""
                for leaf in subtree.leaves():
                    entity_MONEY = entity_MONEY + leaf[0] + " "
                named_entities_MONEY.append(entity_MONEY.strip())
            if subtree.label() == 'FACILITY':
                entity_FACILITY = ""
                for leaf in subtree.leaves():
                    entity_FACILITY = entity_FACILITY + leaf[0] + " "
                named_entities_FACILITY.append(entity_FACILITY.strip())
    return named_entities_GPE,named_entities_ORGANIZATION,named_entities_PERSON,named_entities_LOCATION,named_entities_DATE

def ie_chunking_reason(pos_sent):
    grammar = r""" reason: {<NNS>*<IN>*<IN><JJ>?<NN>}   # chunk determiner/possessive, adjectives and noun {<DT|PP\$>?<JJ>*<NN>}  {<NNP>+}
     status:{<VBD>}
     """
    cp = nltk.RegexpParser(grammar)
    List_rea = []
    List_status = []
    for sentence in pos_sent:
        result = cp.parse(sentence)
        #print(result)
        for subtree in result.subtrees():
            if subtree.label() == 'reason':
                entity_reason = ""
                for leaf in subtree.leaves():
                    entity_reason = entity_reason + leaf[0] + " "
                List_rea.append(entity_reason.strip())
            if subtree.label() == 'status':
                entity_status = ""
                for leaf in subtree.leaves():
                    entity_status = entity_status + leaf[0] + " "
                List_status.append(entity_status.strip())
    return List_rea,List_status
sentences = ie_preprocess(content)
List_reason,status = ie_chunking_reason(sentences)
List_GPE,List_ORGANIZATION,List_PERSON,List_LOCATION,List_DATE = ie_named_entity_finding(sentences)
location = [List_GPE[0]]
#qc.train()
#write data into csv
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
test=pd.DataFrame({'location': location,'reason2':location,'status':status[0],'time':theTime})
test.to_csv('./Msc-twitter-data/data/output.csv',encoding='gbk')

