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
