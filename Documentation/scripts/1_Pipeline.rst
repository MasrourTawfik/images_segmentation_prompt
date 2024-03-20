Pipeline
=============


.. _transformer_architecture:

1. Transformer Architecture Explained
-------------------------------------

.. figure:: /Documentation/images/arch1.png
   :width: 400
   :align: center
   :alt: Alternative Text

The Transformer is a groundbreaking architecture in the field of natural language processing. In this context, we will explain the various aspects of this architecture.

    * **Introduction (Attention is All You Need)**

       
       `paper Attention is all you need <https://arxiv.org/pdf/1706.03762.pdf>`__

      This introduction highlights the basics of the Transformer, as described in the paper "Attention is All You Need".

    * **Tokenization**

      Tokenization is the process of converting text into tokens, the basic units on which the model operates.

    * **Embedding**

      Embedding transforms tokens into dense vectors, which represent words numerically.

    * **Positional encoding**

      Positional encoding adds information about the order of words in the sequence.

    * **Transformer block**

      The Transformer block is the centerpiece of this architecture, comprising layers of attention and fully connected neural networks.

    * **Softmax**

      Softmax is an activation function used to compute probability scores on the model's output.

.. _visual_transformer:

2. Visual Transformer (ViT)
----------------------------
`AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE  <https://arxiv.org/pdf/2010.11929v2.pdf>`__


Explain the functioning and usage of the Visual Transformer.

.. figure:: /Documentation/images/ViT.png
    :width: 400
    :align: center
    :alt: Alternative Text

.. _detection_transformer(DeTR):

3. Detection Transformer
-------------------------

DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 object detection (118k annotated images). It was introduced in the paper `End-to-End Object Detection with Transformers <https://arxiv.org/abs/2005.12872>`__
 by Carion et al. and first released in this repository. `repository <https://github.com/facebookresearch/detr>`__


Explain the functioning and usage of the Detection Transformer (DeTR).

.. figure:: /Documentation/images/DTR.jpg
    :width: 400
    :align: center
    :alt: Alternative Text
