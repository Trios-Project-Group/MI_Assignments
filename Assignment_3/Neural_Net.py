'''
Design of a Neural Network from scratch

*************<IMP>*************
Mention hyperparameters used and describe functionality in detail in this space
- carries 1 mark
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#Base Class for any Layer.
class Layer:

        #Constructor to define the input and output for a layer initially None.
        def __init__(self):
                input = None
                output = None

        #Forward Propogation to find output Y for a layer taking input X.
        def forward_network_calculation(self, input):
                raise NotImplementedError

        #Backward propogation to update corresponding weights. 
        def backward_network_tuning(self, output_error, lr):
                raise NotImplementedError

#Fully_Connected_Layer - each input neuron is connected to each output neuron. 
class Fully_Connected_Layer(Layer):

        #input_size = Number of neurons for input layer.
        #output_size = Numbere of neurons for output layer.
        def __init__(self, input_size, output_size):
                self.weights = np.random.rand(input_size, output_size) - 0.5
                self.bias = np.random.rand(1, output_size) - 0.5

        #Does y = x*w + b and returns the output as y.
        def forward_network_calculation(self, input):
                self.input = input
                self.output = np.dot(self.input, self.weights) + self.bias
                return self.output
        
        #Used to tune weights w and b so that we can reduce the error.
        def backward_network_tuning(self, output_error, lr):
                #Calculate dE/dX and dE/dW using given formulae.
                input_error = np.dot(output_error, self.weights.T)
                weights_error = np.dot(self.input.T, output_error)

                #Tune or update parameters using Gradient descent.
                self.weights -= lr * weights_error
                self.bias -= lr * output_error
                return input_error

class Activation_Layer(Layer):

        def __init__(self, activation_function, derivative_activation_function):
                self.activation_function = activation_function
                self.derivative_activation_function = derivative_activation_function

        #Just apply the activation function on the input vector to give output vector of same dimension.
        def forward_network_calculation(self, input):
                self.input = input
                self.output = self.activation_function(self.input)
                return self.output

        #Finding dE/dX from dE/dY which is output_error.
        #No need to use learning rate as no learnable parameters for tuning.
        def backward_network_tuning(self, output_error, lr):
                return self.derivative_activation_function(self.input) * output_error

#Few Activation Functions and their derivatives implemented here:
def sigmoid(i):
        return 1/(1 + np.exp(-i))

def derivative_sigmoid(i):
        return sigmoid(i)*(1 - sigmoid(i))

def tanh(j):
        return np.tanh(j)

def derivative_tanh(j):
        return 1 - np.tanh(j)**2

#Loss functions and their derivatives:
def MSE(true_labels, predicted_labels):
        return np.mean(np.power((true_labels - predicted_labels), 2))

def derivative_MSE(true_labels, predicted_labels):
        return 2*(predicted_labels - true_labels)/true_labels.size

class NN:

        ''' X and Y are dataframes '''
        #Constructor used for instialisations
        def __init__(self):
                self.list_of_layers = []
                self.loss_function = None
                self.derivative_loss_function = None

       #Function used to add layers 
        def addition_of_layer(self, layer):
                self.list_of_layers.append(layer)

        #Function to assign loss function and its derivative.
        def assign_loss_function(self, loss_function, derivative_loss_function):
                self.loss_function = loss_function
                self.derivative_loss_function = derivative_loss_function

        #Finally the fit function to initiate forward and backward propogation.
        def fit(self, X, Y, epochs, lr):
                '''
                Function that trains the neural network by taking x_train and y_train samples as input
                '''
                len_of_train_set = len(X)

                for i in range(epochs):
                        #Error variable initialised to 0
                        error = 0
                        #Forward propogation to find the output
                        for j in range(len_of_train_set):
                                output = X[j]
                                for layer in self.list_of_layers:
                                        output =  layer.forward_network_calculation(output)
					#calculate forward prop from end -to -end
					
                                
                                #Calculate error using loss function
                                error += self.loss_function(Y[j], output)

                                #Backward propogation - find dE/dY to be passed to each layer
                                derivative_error = self.derivative_loss_function(Y[j], output)
                                for layer in reversed(self.list_of_layers):
                                        derivative_error = layer.backward_network_tuning(derivative_error, lr)
                                
                        #Calculate the average derived error for all training records considered.
                        error /= len_of_train_set
                        print('Epoch (%d/%d) : Error=%f' % (i+1, epochs, error))
                                

	
        def predict(self,X):

                """
                The predict function performs a simple feed forward of weights
                and outputs yhat values 

                yhat is a list of the predicted value for df X
                """
                len_of_test_set = len(X)
                yhat = []

                #For loop for each row in the given test set.
                for i in range(len_of_test_set):
                        output = X[i]
                        #Forward propogation through all layers to find output.
                        for layer in self.list_of_layers:
                                output = layer.forward_network_calculation(output)
                        yhat.append(output)
                return yhat

        def CM(self, y_test,y_test_obs):
                '''
                Prints confusion matrix 
                y_test is list of y values in the test dataset
                y_test_obs is list of y values predicted by the model

                '''

                for i in range(len(y_test_obs)):
                        if(y_test_obs[i]>0.6):
                                y_test_obs[i]=1
                        else:
                                y_test_obs[i]=0
		
                cm=[[0,0],[0,0]]
                fp=0
                fn=0
                tp=0
                tn=0
		
                for i in range(len(y_test)):
                        if(y_test[i]==1 and y_test_obs[i]==1):
                                tp=tp+1
                        if(y_test[i]==0 and y_test_obs[i]==0):
                                tn=tn+1
                        if(y_test[i]==1 and y_test_obs[i]==0):
                                fp=fp+1
                        if(y_test[i]==0 and y_test_obs[i]==1):
                                fn=fn+1
                cm[0][0]=tn
                cm[0][1]=fp
                cm[1][0]=fn
                cm[1][1]=tp

                p= tp/(tp+fp)
                r=tp/(tp+fn)
                f1=(2*p*r)/(p+r)
		
                print("Confusion Matrix : ")
                print(cm)
                print("\n")
                print(f"Precision : {p}")
                print(f"Recall : {r}")
                print(f"F1 SCORE : {f1}")

#Function to fill missing values for weight. 
def fill_weight():
        df = data['Weight'].copy()
        for i in range(len(data['Weight'])):
                if(np.isnan(data['Weight'][i])):
                        v1 = 0
                        v2 = 0
                        category = data['Community'][i]
                        for j in range(i-1,-1,-1):
                                if(category==data['Community'][j]):
                                        v1 = df[j]
                                        break
                        for k in range(i+1,len(data['Weight'])):
                                if(category==data['Community'][k] and not(np.isnan(df[k]))):
                                        v2 = df[k]
                                        break
                        if(v1!=0 and v2!=0):
                                res = (v1+v2)/2
                        elif(v1==0):
                                res = v2
                        else:
                                res = v1
                        df[i] = round(res,0)
        data['Weight'] = df
                        
if __name__=="__main__":
        
        #Initial Preprocessing is done which is commented as the updated csv file is used after data is stored.
        '''
        #Read the csv file
        data = pd.read_csv("LBW_Dataset.csv")
	
        #Data Preprocessing:
	
        #Fill missing values of Age with mean as they almost follow a normal distribution and unknown would be varying on either side of median:
        data['Age'].fillna(value=round(data['Age'].mean(),0), inplace=True)
	
	
        #Filling Nan values of Weight based on the average nearest weights of another women belonging to same community of upper and lower values in the same column. 
        fill_weight()
	
        #Missing values in Delivery Phase is filled with 1 as those missing values belong to below 24 years age and all below 24 years are having 1 as value. 
        data['Delivery phase'].fillna(value='1', inplace=True)
	
        #Again HB is a normal distribution hence is replaced with mean value.
        data['HB'].fillna(value=round(data['HB'].mean(), 1), inplace=True)
	
        #BP has an outlier, hence mean is not choosen as its more prone to outlier instead median is choosen as less prone to outliers.
        data['BP'].fillna(value=data['BP'].median(), inplace=True)
	
        #All values are 5 hence is replaced with 5 using bfill.
        data['Education'].fillna(method='bfill', inplace=True)
	
        #Missing values are replaced by 1 for residence as all those which are missing belong to community 1 and most of community one are residents of same town
        data['Residence'].fillna(value=1, inplace=True)
	
        #Stored it into one csv file.
        data.to_csv("LBW_cleaned_dataset.csv", index=False)
	
        '''

        #Read from updated csv file ater preprocessing.
        data = pd.read_csv("LBW_Preprocessed_Dataset.csv")

        #Read the input features and target variables or neural network
        X = np.array(data.iloc[:,:9].to_numpy().reshape(len(data['IFA']), 1, 9), dtype=np.float32)
        Y = np.array(data.iloc[:, 9].to_numpy().reshape(len(data['Result']), 1, 1), dtype=np.float32)

        # Training data
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25) 

        # Network Architecture
        net = NN()
        net.addition_of_layer(Fully_Connected_Layer(9, 12))
        net.addition_of_layer(Activation_Layer(sigmoid, derivative_sigmoid))
        net.addition_of_layer(Fully_Connected_Layer(12, 5))
        net.addition_of_layer(Activation_Layer(tanh, derivative_tanh))
        net.addition_of_layer(Fully_Connected_Layer(5, 1))
        net.addition_of_layer(Activation_Layer(sigmoid, derivative_sigmoid))

        # Train
        net.assign_loss_function(MSE, derivative_MSE)
        net.fit(x_train, y_train, epochs=75, lr=0.05)

        # Test
        out = net.predict(x_test)

        #Confusion matrix and metrics
        net.CM(y_test, out)
