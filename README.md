<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Implementation of Basic CNN Model to Predict Hand Signs</h1>

<p>The CNN model is built using the following layers:</p>

<ul>
    <li>Input with shape 28 X 28 X 1</li>
    <li>2D convolutional layer with 32 filters</li>
    <li>ReLU activation function</li>
    <li>2D convolutional layer with 64 filters</li>
    <li>ReLU activation function</li>
    <li>MaxPooling2D layer</li>
    <li>Flatten layer to convert output of MaxPooling to 2D space</li>
    <li>Dense layer followed by Dropout (rate = 0.2)</li>
    <li>Final Dense layer for classification with softmax activation function</li>
</ul>

<img src="https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/c28263fc-a614-4abf-bc01-488269f53b97" alt="American Sign Language">

<h2>Training Results</h2>

<p>Final result of training the model on train and validation datasets with a 70/30 ratio split:</p>

<table>
    <tr>
        <th>Epoch</th>
        <th>Loss</th>
        <th>Accuracy</th>
        <th>Validation Loss</th>
        <th>Validation Accuracy</th>
    </tr>
    <tr>
        <td>1/10</td>
        <td>2.3305</td>
        <td>0.3428</td>
        <td>1.1549</td>
        <td>0.7266</td>
    </tr>
    <tr>
        <td>2/10</td>
        <td>0.9446</td>
        <td>0.7242</td>
        <td>0.5028</td>
        <td>0.8849</td>
    </tr>
    <tr>
        <td>3/10</td>
        <td>0.5081</td>
        <td>0.8552</td>
        <td>0.2357</td>
        <td>0.9611</td>
    </tr>
    <tr>
        <td>4/10</td>
        <td>0.3027</td>
        <td>0.9160</td>
        <td>0.1330</td>
        <td>0.9836</td>
    </tr>
    <tr>
        <td>5/10</td>
        <td>0.1812</td>
        <td>0.9538</td>
        <td>0.0616</td>
        <td>0.9981</td>
    </tr>
    <tr>
        <td>6/10</td>
        <td>0.1168</td>
        <td>0.9742</td>
        <td>0.0336</td>
        <td>0.9998</td>
    </tr>
    <tr>
        <td>7/10</td>
        <td>0.0772</td>
        <td>0.9844</td>
        <td>0.0189</td>
        <td>1.0000</td>
    </tr>
    <tr>
        <td>8/10</td>
        <td>0.0575</td>
        <td>0.9894</td>
        <td>0.0120</td>
        <td>1.0000</td>
    </tr>
    <tr>
        <td>9/10</td>
        <td>0.0422</td>
        <td>0.9919</td>
        <td>0.0073</td>
        <td>1.0000</td>
    </tr>
    <tr>
        <td>10/10</td>
        <td>0.0339</td>
        <td>0.9942</td>
        <td>0.0048</td>
        <td>1.0000</td>
    </tr>
</table>

<img src="https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/985c961f-4111-4b74-ae25-8209dc69ff3d" alt="Accuracy Plot">
<img src="https://github.com/Nis-nischith/Machine-Learning-1/assets/119352488/9dafa009-c2b5-44e5-99a3-3f78c395bab2" alt="Loss Plot">

</body>
</html>
