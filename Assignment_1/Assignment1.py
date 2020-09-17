'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
	entropy = 0
	
	labels = df[df.columns[-1]]
	value, counts = np.unique(labels, return_counts=True)
	norm_counts = counts / counts.sum()
	entropy =  -(norm_counts * np.log(norm_counts)/np.log(2)).sum()
	return entropy



'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
	entropy_of_attribute = 0
	
	value, counts = np.unique(df[attribute], return_counts=True)
	norm_counts = counts / counts.sum()
	class_entropy = []

	for i in value:
		df_class = df[df[attribute] == i]
		labels = df_class[df.columns[-1]]
		target_value, target_counts = np.unique(labels, return_counts=True)
		target_norm_counts = target_counts / target_counts.sum()
		entropy =  -(target_norm_counts * np.log(target_norm_counts)/np.log(2)).sum()
		class_entropy.append(entropy)

	class_entropy = np.array(class_entropy)
	entropy_of_attribute = sum(norm_counts * class_entropy)
	return abs(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
	information_gain = 0
	s = get_entropy_of_dataset(df)
	i = get_entropy_of_attribute(df,attribute)
	information_gain = s - i
	return information_gain



''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
   
	information_gains={}
	selected_column=''
	
	attributes = df.columns
	for i in range(len(attributes)-1):
		if attributes[i] not in information_gains:
			information_gains[attributes[i]] = get_information_gain(df,attributes[i])
		
		
	value = max(information_gains.values())
	selected_column = list(information_gains.keys())[list(information_gains.values()).index(value)]

	'''
	Return a tuple with the first element as a dictionary which has IG of all columns 
	and the second element as a string with the name of the column selected

	example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
	'''
	return (information_gains,selected_column)



'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''
