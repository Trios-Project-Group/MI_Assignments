import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
    
    entropy = 0

    total_samples = df.shape[0] #tuple output and index the row alone

    unique_classes = df[df.columns[-1]].nunique()

    counts_per_class = df[df.columns[-1]].value_counts() #a series it is
    
    for class_counts in counts_per_class: #the summation
        
        class_proportion = class_counts/total_samples

        entropy += -1*class_proportion*np.log2(class_proportion)
        
    
    return entropy



def get_entropy_of_attribute(df,attribute):

	
    empty={}   #an empty dict to store the categories within an attr column.
    
    target = df.columns[-1]  #the target column name
    
    print('target: ',target)

    for records in range(len(df)): #iterate the df row by row
        
        category = df.iloc[records][attribute] #getting the value of attribute for current row
        
        target_value = df.iloc[records][target] #getting the target value for that record
                                    
        if category not in empty:  #if that category was not visited

            empty[category]={}  #make a key with category name and value is again a dict

            empty[category][target_value]=1 

        else: #if category already there 

            if target_value not in empty[category]: 

                 empty[category][target_value]=1

            else:
                empty[category][target_value]+=1
                
                
    #every thing is fine now 
    
    print(empty)
    
    res = 0

    for category in empty:

        data_per_category = empty[category]

        p = list(data_per_category.values())

        dr = sum(p)

        entropy=0

        for vals in p:

            entropy += -1*(vals/dr)*np.log2(vals/dr)

        res = res + dr*entropy/len(df)

    
    
    

    return abs(res)
