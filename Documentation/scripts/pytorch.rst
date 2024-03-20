
learn pytorch
=====================

1. Tensors in pytorch
---------------------
.. raw:: html

   <p style="text-align: justify;">
     Tensors in PyTorch are similar to arrays and matrices, like NumPy's ndarrays. However, tensors are optimized for GPU computation and automatic differentiation. They can share memory with NumPy arrays, making data transfer efficient. Tensors are used to encode model inputs, outputs, and parameters. If you're familiar with NumPy, you'll find the Tensor API easy to use.
   </p>

.. code-block:: python

    import torch
    import numpy as np
    

* **Initializing a Tensor**

.. raw:: html

   <p style="text-align: justify;">
      Tensors in PyTorch can be initialized directly from data, allowing for easy creation without specifying the data type explicitly. The data type of the tensor is automatically inferred based on the provided data. This flexibility simplifies the tensor creation process and makes it more intuitive, especially when working with diverse data types.
   </p>

.. code-block:: python
    # Create a list of lists representing the data
    data = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]

    # Initialize a PyTorch tensor directly from the data
    x_data = torch.tensor(data)

    print(x_data)
.. raw:: html

   <p style="text-align: justify;">
     In this example, we have a list of lists `data` representing our data points. We then use `torch.tensor(data)` to create a PyTorch tensor `x_data` directly from this data. The data type of the tensor is automatically inferred based on the provided data.
   </p>

.. code-block:: python
    # Create a NumPy array from the data
    np_array = np.array(data)

    # Initialize a PyTorch tensor from the NumPy array
    x_np = torch.from_numpy(np_array)

    print(x_np)

.. raw:: html
    <p style="text-align: justify;">
      In this example, we first create a NumPy array `np_array` from the data. Then, we use `torch.from_numpy(np_array)` to create a PyTorch tensor `x_np` directly from this NumPy array. This allows us to easily convert between NumPy arrays and PyTorch tensors, and the data type is preserved during the conversion process.
   </p>

.. code-block::python
    x_ones = torch.ones_like(x_data) # retains the properties of x_data
    print(f"Ones Tensor: \n {x_ones} \n")

    x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
    print(f"Random Tensor: \n {x_rand} \n")

.. raw:: html
    <p style="text-align: justify;">
     In this example, `torch.ones_like(x_data)` creates a tensor of ones with the same shape as `x_data`, while `torch.rand_like(x_data, dtype=torch.float)` creates a tensor of random values with the same shape as `x_data` but with a specified data type (`torch.float` in this case). These functions are useful for creating tensors with similar shapes while retaining or modifying certain properties.
    </p>

.. code-block::python

    shape = (2,3,)
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape)
    zeros_tensor = torch.zeros(shape)

    print(f"Random Tensor: \n {rand_tensor} \n")
    print(f"Ones Tensor: \n {ones_tensor} \n")
    print(f"Zeros Tensor: \n {zeros_tensor}")

.. raw:: html
    <p style="text-align: justify;">
    In this example, `torch.rand(shape)` creates a random tensor with the specified shape, `torch.ones(shape)` creates a tensor filled with ones, and `torch.zeros(shape)` creates a tensor filled with zeros. The specified shape `(2, 3)` creates a tensor with 2 rows and 3 columns.
    </p>

* **Attributes of a Tensor**
.. raw:: html
    <p style="text-align: justify;">
     Tensor attributes describe their shape, datatype, and the device on which they are stored.
    </p>


.. code-block::python
    tensor = torch.rand(3,4)

    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device tensor is stored on: {tensor.device}")

output:
 `Shape of tensor: torch.Size([3, 4])
 Datatype of tensor: torch.float32
 Device tensor is stored on: cpu`



