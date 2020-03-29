from gensim.models import Word2Vec
import random
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Bidirectional
from keras.layers.embeddings import Embedding
from keras.preprocessing.sequence import pad_sequences







modelvec = Word2Vec.load("../word2vec/models/word2vec_old.model")

def get_embedding_index(stringlist):
    source_word_indices = []
    array_of_word_lists = stringlist.split(' ') # split data into individual words
    for word in array_of_word_lists:
        if word in modelvec.wv.vocab:
            source_word_indices.append(int(modelvec.wv.vocab[word].index))  ## convert known words to embedding indexes
        else:
            source_word_indices.append(0) # using as padding index
    return source_word_indices


dataset=[]
datasettest=[]

linesPOS = open('data/positive_3900.txt','r').readlines()
linesNEG = open('data/negative_4000.txt','r').readlines()
for i in linesPOS:
    i=i.strip('\n')
    dataset.append([get_embedding_index(i),1])   ## add possitive data to dataset
for i in linesNEG:
    i=i.strip('\n')
    dataset.append([get_embedding_index(i),0])  ## add negative data to dataset

random.shuffle(dataset) ##shuffle dataset to increase entropy


linesPOSTEST = open('data/outputTESTPOS.txt','r').readlines()
linesNEGTEST = open('data/outputTESTNEG.txt','r').readlines()
for i in linesPOSTEST:
    i=i.strip('\n')
    datasettest.append([get_embedding_index(i),1])  # preparing test data similar to train data
for i in linesNEGTEST:
    i=i.strip('\n')
    datasettest.append([get_embedding_index(i),0])
random.shuffle(datasettest)



X_train = pad_sequences([i[0] for i in dataset])
y_train = [i[1] for i in dataset]

X_test = pad_sequences([i[0] for i in datasettest])
y_test = [i[1] for i in datasettest]




model = Sequential()
model.add(modelvec.wv.get_keras_embedding(train_embeddings=False))
model.add(Bidirectional(LSTM(128, recurrent_dropout=0.1))) # BiLSTM for understanding the place of the word in sentence
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))  # two Dense 64 node layers to avoid underfitting
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu')) # dropout layers to avoid overfitting
model.add(Dropout(0.1))
model.add(Dense(1,activation='sigmoid'))  # activation='sigmoid' for binary classifiction
model.summary()

model.compile(
    loss="binary_crossentropy",
    optimizer='adam',
    metrics=['accuracy'])

model.fit(X_train,y_train, epochs=20)

pred=model.predict(X_test)


for i in pred:
    if i[0] > 0.5:
        i[0]=1
    else:
        i[0]=0


print(classification_report(y_test,pred))
sns.heatmap(confusion_matrix(y_test,pred),annot=True) # obtain all classification metrics
plt.show()


model.save('models/test.h5') 