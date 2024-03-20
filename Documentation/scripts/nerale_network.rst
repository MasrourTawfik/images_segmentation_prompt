Neural Network Wrapper
=======================

1. dataset:
---------

`link to the dataset <https://github.com/imadmlf/taskes/blob/main/cancer_classification.csv>`__

Read the `dataset <https://github.com/imadmlf/taskes/blob/main/cancer_classification.csv>`__ :

To read data from a CSV file using pandas (pd), you can use the read_csv function:


.. code-block:: python

    import pandas as pd 
    df = pd.read_csv('cancer_classification.csv')


2. Training on a simple dataset
-----------------------------

1. `DataPreprocessing <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py>`__ : 

This module likely contains functions or classes for preparing your raw data for analysis. This can include tasks such as handling missing values, encoding categorical variables, scaling numerical features, and splitting the data into training and testing sets.
You can view the code and access the link by clicking on `link to DataPreprocessing class <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py>`__.

2. `DataExploration <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataExploration.py>`__ :

 This part of your pipeline focuses on understanding the structure and characteristics of your dataset. It might include functions or classes for displaying basic statistics (like mean, median, standard deviation), visualizations (like histograms, scatter plots, or correlation matrices), and checking for any anomalies or inconsistencies in the data.
 You can view the code and access the link by clicking on `link to the DataExploration class <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataExploration.py>`__ .


3. `ModelTraining <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/modeltrainer.py>`__ : 

Here, you're training a machine learning model on your preprocessed data. This typically involves selecting an appropriate algorithm (like a neural network), defining a loss function, and optimizing model parameters using an optimization algorithm (like stochastic gradient descent).
You can view the code and access the link by clicking on `link to the ModelTraining class <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/modeltrainer.py>`__.


4. `ModelEvaluation <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/ModelEvaluation.py>`__ :
 After training your model, you need to evaluate its performance. This module likely contains functions or classes for computing various evaluation metrics (like accuracy, precision, recall, or F1-score), generating confusion matrices, and visualizing prediction results.
 You can view the code and access the link by clicking on `link to the ModelEvaluation class  <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/ModelEvaluation.py>`__


5. `NeuralNetwork <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/neural_network.py>`__    :

 This appears to be a class for defining a neural network architecture using the PyTorch library. It specifies the layers, activation functions, and connections between neurons in the network.
 'You can view the code and access the link by clicking on `link to the NeuralNetwork class <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/neural_network.py>`__.


.. code-block::python
    from DataPreprocessing import DataPreprocessing
    from DataExploration import DataExploration
    from ModelEvaluation import ModelEvaluation
    from ModelTraining import ModelTraining
    from neural_network import NeuralNetwork
    import torch



3. Test the `DataPreprocessing <https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py>`__  class
-------------------------------------------------------------------------------------------------------------------------


The `preprocessor` object is created using the `DataPreprocessing`_ class, which prepares the data for training a machine learning model. After splitting the data into training and testing sets using the `split_data()`_ method, it normalizes the data with `normalize_data()`_. Finally, it converts the data into tensors with `tensorize_data()`_, ready for model training and evaluation.

.. code-block:: python

    preprocessor = DataPreprocessing(df)
    x_train, x_test, y_train, y_test = preprocessor.split_data(test_size=0.2, random_state=42)
    x_train, x_test = preprocessor.normalize_data()
    x_train_tensor, x_test_tensor, y_train_tensor, y_test_tensor = preprocessor.tensorize_data()

.. _`DataPreprocessing`: https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py
.. _`split_data()`: https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py#LX
.. _`normalize_data()`: https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py#LX
.. _`tensorize_data()`: https://github.com/imadmlf/Neural_Network_Wrapper/blob/main/DataPreprocessing.py#LX
