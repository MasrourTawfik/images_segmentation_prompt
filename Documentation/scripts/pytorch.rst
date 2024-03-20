learn pytorch
=====================

1. Tensors in pytorch
---------------------
Tensors in PyTorch are similar to arrays and matrices, like NumPy's ndarrays. However, tensors are optimized for GPU computation and automatic differentiation. They can share memory with NumPy arrays, making data transfer efficient. Tensors are used to encode model inputs, outputs, and parameters. If you're familiar with NumPy, you'll find the Tensor API easy to use.

.. code-block:: python

    import torch
    import numpy as np
    

* **Initializing a Tensor**

Tensors in PyTorch can be initialized directly from data, allowing for easy creation without specifying the data type explicitly. The data type of the tensor is automatically inferred based on the provided data. This flexibility simplifies the tensor creation process and makes it more intuitive, especially when working with diverse data types.

.. code-block:: python
    # Create a list of lists representing the data
    data = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
    # Initialize a PyTorch tensor directly from the data
    x_data = torch.tensor(data)
    print(x_data)
