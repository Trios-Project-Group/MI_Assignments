import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
    entropy = 0
    total_samples = df.shape[0] #tuple output and index the row alone
    #unique_classes = df[df.columns[-1]].nunique()
    counts_per_class = df[df.columns[-1]].value_counts() #a series it is
    for class_counts in counts_per_class: #the summation
        class_proportion = class_counts/total_samples
        entropy += -1*class_proportion*np.log2(class_proportion)
    return entropy

def get_entropy(df, attribute, value):
    entropy = 0
    total_samples_attribute = df[attribute].value_counts()[value]
    #unique_classes = df[df.columns[-1]].nunique()
    counts_per_attribute = df.groupby(attribute)[df.columns[-1]].value_counts()[value]
    for counts in counts_per_attribute: #the summation
        proportion = counts/total_samples_attribute
        entropy += -1*proportion*np.log2(proportion)
    return entropy


'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
    entropy_of_attribute = 0
    total_samples = df.shape[0]
    attribute_values = df[attribute].unique()
    entropy_for_values = dict()
    count_attribute_values = df[attribute].value_counts()
    i = df.groupby(attribute)[df.columns[-1]].value_counts()
    for value in attribute_values:
        entropy_for_values[value]=get_entropy(df, attribute, value) 
    for key,values in entropy_for_values.items():
        entropy_of_attribute += (count_attribute_values[key]/total_samples)*entropy_for_values[key]
    return abs(entropy_of_attribute)

'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
	information_gain = 0
	information_gain = get_entropy_of_dataset(df) - get_entropy_of_attribute(df, attribute)
	return information_gain


'''
Return a tuple with the first element as a dictionary which has IG of all columns 
and the second element as a string with the name of the column selected

example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
'''
''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
   
        information_gains={}
        selected_column=''
        IG = 0
        l = len(df.columns)
        columns = df.columns[:l-1]
        for column in columns:
            information_gains[column] = get_information_gain(df,column)
            if(information_gains[column] > IG):
                IG = information_gains[column]
                selected_column = column
        return (information_gains,selected_column)

