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
601/601 [==============================] - 65s 107ms/step - loss: 2.3305 - accuracy: 0.3428 - val_loss: 1.1549 - val_accuracy: 0.7266

Epoch 2/10
601/601 [==============================] - 56s 93ms/step - loss: 0.9446 - accuracy: 0.7242 - val_loss: 0.5028 - val_accuracy: 0.8849

Epoch 3/10
601/601 [==============================] - 52s 86ms/step - loss: 0.5081 - accuracy: 0.8552 - val_loss: 0.2357 - val_accuracy: 0.9611

Epoch 4/10
601/601 [==============================] - 54s 90ms/step - loss: 0.3027 - accuracy: 0.9160 - val_loss: 0.1330 - val_accuracy: 0.9836

Epoch 5/10
601/601 [==============================] - 50s 84ms/step - loss: 0.1812 - accuracy: 0.9538 - val_loss: 0.0616 - val_accuracy: 0.9981

Epoch 6/10
601/601 [==============================] - 52s 86ms/step - loss: 0.1168 - accuracy: 0.9742 - val_loss: 0.0336 - val_accuracy: 0.9998

Epoch 7/10
601/601 [==============================] - 51s 85ms/step - loss: 0.0772 - accuracy: 0.9844 - val_loss: 0.0189 - val_accuracy: 1.0000

Epoch 8/10
601/601 [==============================] - 50s 83ms/step - loss: 0.0575 - accuracy: 0.9894 - val_loss: 0.0120 - val_accuracy: 1.0000

Epoch 9/10
601/601 [==============================] - 51s 85ms/step - loss: 0.0422 - accuracy: 0.9919 - val_loss: 0.0073 - val_accuracy: 1.0000

Epoch 10/10
601/601 [==============================] - 55s 91ms/step - loss: 0.0339 - accuracy: 0.9942 - val_loss: 0.0048 - val_accuracy: 1.0000



![acc](https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/985c961f-4111-4b74-ae25-8209dc69ff3d)

![loss](https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/9dafa009-c2b5-44e5-99a3-3f78c395bab2)
