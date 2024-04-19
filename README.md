# Machine-Learning-1
Implementation of basic CNN model to predict hand-signs
The CNN model is built by these layers -
1. Input with shape 28 X 28 X 1
2. 2D convolutional layer with number of filters = 32
3. Followed by an activation function ReLU 
4. 2D convolutional layer with number of filters = 64
5. Followed by an activation function ReLU
6. MaxPooling2D layer is applied
7. The output of MaxPooling is flattened into 2D space
8. Followed by Dense layer and droupout with a rate of 0.2
9. Dense layer for final classification with softmax as activation function
