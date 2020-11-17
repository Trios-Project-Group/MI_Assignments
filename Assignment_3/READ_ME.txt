=> Explanation Of The Implementation & Design 

	#Building the Neural Net

	* A layered , modularized NN architecture is implemented in the design.
	* A class named "Layer" serves as the base class with 2 methods defined within .This class is used to build the Neural Net.
		
		* A 'Fully_Connected_Layer' class inherits the 'Layer' class. Describes the input neurons , the output neurons and the weights
          between them. This layer defines 2 methods namely forward_network_calculation and backward_network_tuning.

		* Weight matrices are randomly initialised , and so is the bias.

		* Followed by the input and output neurons , we have the 'Activation_Layer'. This layer as well inherits the 'Layer' Base class
		  and provides the overrided implementation for forward_network_calculation and backward_network_tuning.

		* The Design uses different activation functions(tanh , sigmoid) and their derivates in between the fully_connected_layers.




	*The design has 3 layers of dimensions [9,12]  --  [12,5] ---  [5,1] .

	*The NN implementation is scalable as any number of layers can be added without any change in core.

    *Any number of loss functions or activation functions can be added but a layercan take one activation function at a time.





=> List Of Hyper - Parameters

		-> Test and Train Size = Train (70%)  , Test (30%)
		-> Weights             = randomly init using np.random function
		-> Bias 			   = randomly initialized
		-> Learning rate (lr)  = 0.05
		-> Number of Epochs    = 75




=> Key Features Of Our Implementation & Design

-> The architecture is as follows


	1) Input Layer: Input to Neural network with 9 neurons (Dimension: 1 X 9).


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
	        Final dimension of output - (1 X 1




=>Out Of The Box Implementation , beyond the basics


  *The program structure and overview is very abstract and canbe easily simulated by adding any additional layers and Activation functions

  *The implementation is structured and makes use of inheritance to reuse the methods of parent class.

  *The data processing methods are done with meaningful interpretations of the data.

  *The implementation is scalable , many layers can be added for simulation purposes without affecting the implementation.



=>Steps to Execute the python script

-> Three files are uploaded:

	1) READ_ME.txt - Explains the implementation, design and key components.
	2) Neural_Net.py - Main script with code and comments for better readability.
	3) LBW_Preprocessed_Dataset - The dataset produced and saved after preprocessing.


RUN:
	-> Run Neural_Net.py file with the LBW_Preprocessed_Dataset in same directory using the command <python3 Neural_Net.py>
  
	->The code gives the desired results - confusion matrix and other corresponding metrics.



