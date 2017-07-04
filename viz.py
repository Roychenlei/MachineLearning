#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree 

iris=load_iris()

test_idx=[0,1,2,100]

#training data
train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx,axis=0)


#testing data
test_target=iris.target[test_idx]
test_data=iris.data[test_idx ]


print test_target
print test_data


clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print test_target
print clf.predict(test_data)

#