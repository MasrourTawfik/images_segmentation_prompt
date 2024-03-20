Learn the Basics
=====================
- pytorch basic
- pytorch neural network

Quickstart
=====================

This section covers the basic APIs for common tasks in machine learning. Refer to the links in each section to dive deeper.

Working with data
---------------------

PyTorch provides two main primitives to work with data: `torch.utils.data.DataLoader` and `torch.utils.data.Dataset`. 
`Dataset` stores the samples and their corresponding labels, and `DataLoader` wraps an iterable around the `Dataset`.

PyTorch offers domain-specific libraries such as TorchText, TorchVision, and TorchAudio, all of which include datasets. For this tutorial, we will be using a TorchVision dataset.

Create Data Loaders
~~~~~~~~~~~~~~~~~~~~~~~~

```python
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

batch_size = 64

# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

# Check the shape of a batch from test data.
for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break```
