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


![american_sign_language](https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/c28263fc-a614-4abf-bc01-488269f53b97)



Final result of tranining the model on train and val dataset with 70/30 ratio split-

Epoch 1/10
601/601 [==============================] - 51s 84ms/step - loss: 0.9696 - accuracy: 0.7122 - val_loss: 0.0612 - val_accuracy: 0.9926

Epoch 2/10
601/601 [==============================] - 56s 93ms/step - loss: 0.0900 - accuracy: 0.9746 - val_loss: 0.0070 - val_accuracy: 1.0000

Epoch 3/10
601/601 [==============================] - 50s 83ms/step - loss: 0.0436 - accuracy: 0.9868 - val_loss: 0.0037 - val_accuracy: 1.0000

Epoch 4/10
601/601 [==============================] - 54s 90ms/step - loss: 0.0327 - accuracy: 0.9896 - val_loss: 0.0012 - val_accuracy: 1.0000

Epoch 5/10
601/601 [==============================] - 50s 83ms/step - loss: 0.0234 - accuracy: 0.9926 - val_loss: 0.0016 - val_accuracy: 0.9999

Epoch 6/10
601/601 [==============================] - 51s 84ms/step - loss: 0.0174 - accuracy: 0.9944 - val_loss: 3.1374e-04 - val_accuracy: 1.0000

Epoch 7/10
601/601 [==============================] - 50s 83ms/step - loss: 0.0143 - accuracy: 0.9953 - val_loss: 1.6623e-04 - val_accuracy: 1.0000

Epoch 8/10
601/601 [==============================] - 54s 90ms/step - loss: 0.0173 - accuracy: 0.9941 - val_loss: 2.8872e-04 - val_accuracy: 1.0000

Epoch 9/10
601/601 [==============================] - 62s 103ms/step - loss: 0.0123 - accuracy: 0.9960 - val_loss: 1.8116e-04 - val_accuracy: 1.0000

Epoch 10/10
601/601 [==============================] - 49s 82ms/step - loss: 0.0150 - accuracy: 0.9947 - val_loss: 6.4468e-04 - val_accuracy: 1.0000
