=> Explanation Of The Implementation & Design 
-> The Neural network designed here uses modular approach to provide ease of user interface.
-> The whole concept is in terms of classes and objects encapsulated from outside world.
-> Each layer irrespective of its type inherits the bae class Layer.
-> This approch helps in tuning hyperparameters without changing the core implementation of layers.
-> It is scalable as any number of layers can be added without any change in core.
-> Any number of loss functions or activation functions can be added but a layercan take one activation function at a time.

=> List Of Hyper - Parameters
-> Test and Train Size
-> Weights
-> Bias
-> Learning rate (lr)
-> Number of Epochs

=> Key Features Of Our Implementation & Design
-> The architecture is as follows
1) Input Layer: Input to Neuarl network with 9 neurons (Dimension: 1 X 9).
2) Hidden Layer 1 (Fully Connected Layer): Takes input from Input Layer.
        Number of neurons - 12
        Dimension of Input in this layer - (1 X 9)
        Dimension of Weight - (9 X 12)
        Dimension of Bias - (1 X 12)
        Dimension of Intermideate Output - (1 X 12)
        Then it is passed throuch Activation layer - Sigmoid (Doesn't change dimension)
        Final dimension of output - (1 X 12)
3) Hidden Layer 2 (Fully Connected Layer): Takes input from Hidden Layer 1.
        Number of neurons - 5
        Dimension of Input in this layer - (1 X 12)
        Dimension of Weight - (12 X 5)
        Dimension of Bias - (1 X 5)
        Dimension of Intermideate Output - (1 X 5)
        Then it is passed throuch Activation layer - Tanh (Doesn't change dimension)
        Final dimension of output - (1 X 5)
4)  Output Layer (Fully Connected Layer): Takes input from Hidden Layer 2.
        Number of neurons - 1
        Dimension of Input in this layer - (1 X 5)
        Dimension of Weight - (5 X 1)
        Dimension of Bias - (1 X 1)
        Dimension of Intermideate Output - (1 X 1)
        Then it is passed throuch Activation layer - Sigmoid (Doesn't change dimension)
        Final dimension of output - (1 X 1)

=>Out Of The Box Implementation , beyond the basics
-> Have tried implementing a scalable Neural network from scratch.
-> Tried to combine few important chracteristics like inheritance, encapsulation into Neural network for security and many other reasons.

=>Steps to Execute the python script
-> Three files are uploaded:
1) Read_Me.txt - Explains the implementation, design and key components.
2) Neural_Net.py - Main file with code and comments for better readability.
3) LBW_Preprocessed_Dataset - The dataset produced after preprocessing.
-> Run Neural_Net.py file with the LBW_Preprocessed_Dataset in same directory.
->The code gives the desired results - confusion matrix and other corresponding metrics.