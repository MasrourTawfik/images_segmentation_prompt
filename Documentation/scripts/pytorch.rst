Introduction to Tensors in PyTorch
===================================

The purpose of this documentation is to provide a comprehensive introduction to tensors in PyTorch,
emphasizing their importance and usage within the context of machine learning models.

1. Introduction to Tensors
---------------------------

Tensors are specialized data structures similar to arrays and matrices, used to encode the inputs, outputs, and
parameters of a model in PyTorch. They are optimized for computation on GPUs and automatic differentiation.

.. code-block:: python

    import torch

    # Create a tensor
    x = torch.tensor([[1, 2], [3, 4]])
    print(x)

2. Initializing Tensors
-------------------------

Tensors can be initialized in various ways, including directly from data, from NumPy arrays, or from other tensors.
Initializing tensors is flexible and intuitive, simplifying the process of tensor creation.

.. code-block:: python

    import torch
    import numpy as np

    # Initialize from data
    data = [[1, 2], [3, 4]]
    x_data = torch.tensor(data)

    # Initialize from NumPy array
    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)

    print(x_data)
    print(x_np)

3. Attributes of Tensors
--------------------------

Tensor attributes include their shape, data type, and the device on which they are stored. These attributes are useful
for understanding and manipulating tensors effectively.

.. code-block:: python

    import torch

    # Create a tensor
    tensor = torch.rand(3, 4)

    # Get tensor attributes
    print(f"Shape of tensor: {tensor.shape}")
    print(f"Datatype of tensor: {tensor.dtype}")
    print(f"Device tensor is stored on: {tensor.device}")

4. Operations on Tensors
--------------------------

PyTorch offers a wide range of tensor operations, including arithmetic operations, linear algebra, matrix manipulation,
sampling, and more. Tensors can also be used for operations in GPU mode, providing optimized performance.

.. code-block:: python

    import torch

    # Arithmetic operations
    x = torch.tensor([[1, 2], [3, 4]])
    y = torch.tensor([[5, 6], [7, 8]])

    # Matrix multiplication
    z1 = x @ y
    z2 = torch.matmul(x, y)

    print(z1)
    print(z2)

5. Bridge with NumPy
----------------------

Tensors in PyTorch can share their underlying memory with NumPy arrays, enabling seamless conversion between the two.
This allows for smooth integration between PyTorch and NumPy, facilitating work with data.

.. code-block:: python

    import torch
    import numpy as np

    # Tensor to NumPy array
    tensor = torch.tensor([1, 2, 3, 4])
    numpy_array = tensor.numpy()

    # NumPy array to Tensor
    numpy_array = np.array([5, 6, 7, 8])
    tensor = torch.from_numpy(numpy_array)

    print(tensor)
