import numpy as np
import string
import gensim
import nltk
import gensim.models.ldamodel as glda
import gensim.models.coherencemodel as cm
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora

def create_model(K):
	pre_collection = preprocess()
	
	dictionary = corpora.Dictionary(pre_collection)
	dictionary.filter_extremes(no_below=2, no_above=0.8, keep_n=500)
	docs_ids=[dictionary.doc2bow(doc) for doc in pre_collection]
	lda = glda.LdaModel(docs_ids, num_topics=K, id2word=dictionary)
	return lda, dictionary, docs_ids, pre_collection

def clean_doc(doc):
	pont = set(string.punctuation)
	stop = set(stopwords.words('english'))
	stpo = nltk.stem.PorterStemmer()
	lemma = WordNetLemmatizer()
	
	output = doc.lower()
	output = ' '.join([w for w in output.split() if w not in stop])
	output = ''.join(ch for ch in output if ch not in pont)
	output = ' '.join(lemma.lemmatize(w) for w in output.split())
	output = ' '.join(stpo.stem(w) for w in output.split())
	return output

def preprocess():
	collection_name = "tagmynews20K.short"
	fdoc = open(collection_name)
	docs = fdoc.readlines()
	final_list = []
	for doc in docs:
		final_list.append(clean_doc(doc).split())
	return final_list
					
					

					   
K = 20
topic_id = 0
num_words = 30
word_id = 0

lda, dictionary, docs_ids, pre_collection = create_model(K)

w_top = lda.get_topic_terms(topic_id, topn=num_words)

topics = []
for t in range(K):
	words = lda.get_topic_terms(t, topn=10)
	topics.append([dictionary.get(w[0]) for w in words])
print(topics)
print(lda.get_document_topics(docs_ids[0], minimum_probability=0))

mycm = cm.CoherenceModel(model=lda, texts=pre_collection,
			 corpus=dictionary, coherence='u_mass')
mycm.get_coherence()

mycm = cm.CoherenceModel(topics=[topics[0]], dictionary=dictionary,
			 texts=pre_collection, coherence='u_mass')
