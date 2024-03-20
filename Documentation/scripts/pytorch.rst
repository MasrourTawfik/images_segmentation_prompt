Introduction to  PyTorch
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

* **Initializing Tensors**


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

* **Attributes of Tensors**


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

* **Operations on Tensors**



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

* **Bridge with NumPy**


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



2. Datasets & DataLoaders
---------------------------



PyTorch provides two important primitives for working with datasets: torch.utils.data.Dataset and torch.utils.data.DataLoader. These enable us to decouple dataset processing from model training code, enhancing readability and modularity.

* Dataset:

    Stores samples and their corresponding labels.
    Allows for custom transformations.
    Subclasses can be created for specific datasets.

* DataLoader:

    Wraps an iterable around the dataset.
    Facilitates easy access to samples during training.


* **Loading a Dataset**

PyTorch also offers pre-loaded datasets, such as FashionMNIST, for prototyping and benchmarking models. These datasets subclass torch.utils.data.Dataset and implement specific functions for handling the data.
For example, to load the Fashion-MNIST dataset using TorchVision:


.. code-block:: python

    import torch
    from torch.utils.data import Dataset
    from torchvision import datasets
    from torchvision.transforms import ToTensor
    import matplotlib.pyplot as plt


    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor()
    )

    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor()
    )



* **Iterating and Visualizing the Dataset**

We can index Datasets manually like a list: training_data[index]. We use matplotlib to visualize some samples in our training data.

.. code-block:: python

    labels_map = {
        0: "T-Shirt",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle Boot",
        }
    figure = plt.figure(figsize=(8, 8))
    cols, rows = 3, 3
    for i in range(1, cols * rows + 1):
        sample_idx = torch.randint(len(training_data), size=(1,)).item()
        img, label = training_data[sample_idx]
        figure.add_subplot(rows, cols, i)
        plt.title(labels_map[label])
        plt.axis("off")
        plt.imshow(img.squeeze(), cmap="gray")
    plt.show()

