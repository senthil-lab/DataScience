# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:44:08 2021

@author: snara016
"""

import pandas as pd
import numpy as np


bank_df = pd.read_csv('BankNote_Authentication.csv')

bank_df.head()

# independent feature
X = bank_df.iloc[:,:-1]
X.head()

# dependent feature
y = bank_df.iloc[:,-1]

y.head()

# Train - Test spilt
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=0)

X_train.shape
X_test.shape

# Implement Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
classifer = RandomForestClassifier()
classifer.fit(X_train, y_train)


# Prediction

y_pred = classifer.predict(X_test)

# Check Accuracy

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, y_pred)

score

# Create a Pickle file using serialization
import pickle
# open file name called classifier.pkl in write byte mode 
pickle_out = open("classifier.pkl","wb")
# dumping the classifier inside pickle_out file
pickle.dump(classifer, pickle_out)
pickle_out.close()

classifer.predict([[2,3,4,1]])



