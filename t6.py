import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from numpy import array
from sklearn.model_selection import train_test_split
from pandas import ExcelWriter
from pandas import ExcelFile
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nf = pd.ExcelFile('reviews_tagged.xlsx')
df = pd.read_excel(nf, names = ['Review','Type'], sheet_name='Sheet1')
#nf1 = pd.ExcelFile('negativetestdata.xlsx')
#dfs1 = pd.read_excel(nf1, sheet_name='Sheet1')
#df = pd.DataFrame({'Review': [], 'Type': []})
#df = df.append(dfs)
df.loc[df["Type"]=='Positive', "Type"]=1
df.loc[df["Type"]=='Negative', "Type"]=0



df_x_1 = df["Review"]
df_y = df["Type"]

#b = df['Review'].values
df_x =df_x_1.astype('U')
cv = TfidfVectorizer()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.20, random_state = 4)
x_traincv = cv.fit_transform(x_train)

a = x_traincv.toarray()
classifier = MultinomialNB()
y_train = y_train.astype('int')
classifier.fit(x_traincv, y_train)
x_testcv = cv.transform(x_test)
predictions = classifier.predict(x_testcv)
print(predictions)
realdata = np.array(y_test)
print(realdata)
c = 0
for i in range (len(predictions)):
    if(predictions[i]==realdata[i]):
        c = c+1
print(c)
x = len(predictions)
print(x)
accuracy = c/x
print(accuracy)


