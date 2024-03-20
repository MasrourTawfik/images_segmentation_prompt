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
