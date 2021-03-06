#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/9/11 14:42
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  LogisticRegression
# @File      :  LogisticRegression_test2.py
# @Software  :  PyCharm Community Edition

# ********************************************************* 
import numpy as np
import random

def sigmoid(inX):
	return 1.0/(1+np.exp(-inX))

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
	m,n = np.shape(dataMatrix)
	weights = np.ones(n)
	for j in range(numIter):
		dataIndex = list(range(m))
		for i in range(m):
			alpha = 4/(1.0+j+i)+0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			h = sigmoid(sum(dataMatrix[randIndex]*weights))
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weights

def classifyVector(inX, weights):
	prob = sigmoid(sum(inX*weights))
	if prob > 0.5:
		return 1.0
	else:
		return 0.0

def colicTest():
	frTrain = open('horseColicTraining.txt')
	frTest = open('horseColicTest.txt')
	trainingSet = []
	traininglabels = []
	for line in frTrain.readlines():
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		traininglabels.append(float(currLine[21]))
	trainWeights = stocGradAscent1(np.array(trainingSet), traininglabels, 500)
	errorCount = 0
	numTestVec = 0.0
	for line in frTest.readlines():
		numTestVec += 1.0
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(np.array(lineArr),trainWeights)) != int(currLine[21]):
			errorCount += 1
	errorRate = float(errorCount)/numTestVec
	print('the error rate of this test is: %f' % errorRate)
	return errorRate

def multiTest():
	numTests = 10
	errorSum = 0.0
	for k in range(numTests):
		errorSum += colicTest()
	print('after %d iterations the average error rate is: %f' % (numTests, errorSum/float(numTests)))

if __name__ == '__main__':
	multiTest()