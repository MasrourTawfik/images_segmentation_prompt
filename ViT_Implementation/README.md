<img src="./Assets/vit.gif" width="500px"></img>

## Table of Contents

- [Vision Transformer - Pytorch](#vision-transformer---pytorch)
- [Install](#install)
- [Dataset preparation](#Dataset-preparation)
- [ViT components](#ViT-components)


## Vision Transformer - Pytorch

The Vision Transformer (ViT) marks a significant shift in how deep learning approaches image processing tasks, traditionally dominated by Convolutional Neural Networks (CNNs). ViT applies the transformer architecture, originally designed for natural language processing tasks, to image classification challenges. This innovative approach treats an image as a sequence of patches and processes these patches through a series of transformer blocks, leveraging self-attention mechanisms to understand the global context of an image.

Vision Transformers are built on tranformer architecture. So, in order to understand the mechanism of the original transformers architecture, please follow the link below
(LINK TO READ THE DOCS)

As for Vision transformers, the link below provides basic concepts behind Vision Transformers.
(LINK TO READ THE DOCS)

 

## Install

The current Github repository provides ready-to-use packages.

These packages contain:
- ViT principal components that are assembled afterwards to make fully working Visual Transformer architecture
- Utility modules (training, testing, calculating performance indicators, ploting ... )

Please refer to the requirements.txt file for a list of necessary dependencies.


```python
!pip install git+https://github.com/SAAD1190/ViT_Implementation.git
```


## Dataset preparation

### Resize_Tensorize
Provides functionality for resizing and converting images into tensors, preparing them for processing by neural networks.
Suitable parameters as cited in related paper An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale are:

- Size 224x224
- Patch size = 16

### Sample_Viz
Contains utilities for visualizing samples from the dataset, likely to help with understanding the data and debugging labeling process.

### set_seed
A utility script for setting the random seed to ensure reproducibility of results.

### Datasets_DataLoaders
Handles data loading and batching, making it easier to feed data into the model for training or inference.

## ViT components

### PatchEmbedding
Handles the creation of patch embeddings from input images, which is a crucial preprocessing step in Vision Transformer models where images are divided into patches and then projected into an embedding space.


### MLPBlock
In the Vision Transformer (ViT), think of the MLP block as a special mini-factory that improves the details from the image's pieces. Here's a simpler view:

Image in Pieces: ViT chops up the image into little squares, like cutting a picture into puzzle pieces.
Learning from Pieces: It looks at these pieces to understand what the whole picture might be about.
MLP Block's Job: Now, enter the MLP block. Its task is to take the learnings from those pieces and make them clearer or more detailed. It's like taking a rough sketch and filling in the colors and shades to make it look more like the real picture.
Ready for Decisions: After the MLP block has added its details, ViT is better at deciding what's in the image because it has a clearer, more detailed understanding.
So, the MLP block is a crucial step that takes the initial rough understanding and refines it, helping ViT get a clearer, more detailed picture of what it's looking at.

### MultiheadSelfAttentionBlock
Implements the multi-head self-attention mechanism, a core component of the Transformer architecture that allows the model to weigh the importance of different parts of the input data.


### TransformerEncoderBlock
Defines the Transformer Encoder Block, which applies self-attention and is responsible for the bulk of processing within a Transformer model.

### ViT
This is presumably the main script for the Vision Transformer model, integrating all the components into a complete architecture for image classification or other vision tasks.