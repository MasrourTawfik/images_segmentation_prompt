AN IMAGE IS WORTH 16X16 WORDS
=============================

Objectives of the Paper
-------------------------
 
.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">  

    What problem is the paper tackling?
    </span>
    
    <span style="color:#00008B;">  

    The paper addresses the challenge of applying Transformer architecture to Computer Vision tasks, aiming to reduce the heavy reliance on Convolutional Neural Networks (CNNs) in the field. It argues that this transition would yield comparable results to traditional CNNs while requiring fewer computational resources for training.
    </span></p>
    

    <p style="text-align: justify;"><span style="color:blue;">  
    What is the relevant background for this problem?
    </span>
    <span style="color:#00008B;">

    Transformers have been extensively used for Natural Language Processing (NLP) tasks, exemplified by state-of-the-art models like BERT and GPT. While there has been some exploration of using transformers for image tasks, it has generally been resource-intensive.
    </span></p>


Paper Contributions
---------------------

What methods did the paper propose to address the problem?

The paper proposes reshaping 2D images into a sequence of flattened 2D patches to adapt the image input for transformers. A learnable embedding is added to the sequence, akin to BERT's [class] token, and position embeddings are incorporated to retain positional information. The transformer encoder comprises alternating layers of multi-headed self-attention and MLP blocks, and during pre-training and fine-tuning, a classification head is attached to the output. The Vision Transformer (ViT) is pre-trained on large datasets and fine-tuned for downstream tasks.

How are the paper’s contributions different from previous related works?


While not the first to apply transformers to Computer Vision (CV), this paper distinguishes itself by successfully employing standalone transformers for CV tasks. Unlike previous approaches, ViT achieves comparable accuracy to CNNs with significantly reduced training time. Additionally, ViT does not rely on convolutions, showcasing the potential of transformers for CV tasks.

How did the paper assess its results?


The methodology was evaluated on multiple datasets, and results were measured through few-shot or fine-tuning accuracy. ViT was compared against popular benchmarks and configurations, demonstrating promising results in image classification tasks. Preliminary studies on self-supervised training showed further accuracy improvements.



Paper Limitations, Further Research, and/or Potential Applications
------------------------------------------------------------

While ViT shows promise, its performance in vision-based tasks beyond classification, such as detection and segmentation, remains unexplored. Further pre-training and scalability studies are suggested to unlock the full potential of transformers in CV. The paper hints at the possibility of transformers becoming universal models, capable of scaling with data across various human tasks, but acknowledges that this vision is yet to be fully realized.






link for more information
---------------------------
.. admonition::  For more information

   .. container:: blue-box
   

      * You can view more by clicking the  `link to the paper "An Image is Worth 16x16 Words:" <https://arxiv.org/pdf/1706.03762.pdf>`__ 
        
      * or simply clicking the picture

    
.. image:: /Documentation/images/References/examples.png
   :width: 700
   :align: center
   :alt: Alternative Text
   :target: https://arxiv.org/pdf/1706.03762.pdf