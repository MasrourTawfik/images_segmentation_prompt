Visual Transformer (ViT)
========================


.. image:: /Documentation/images/vit.gif
   :width: 700
   :align: center
   :alt: Alternative Text



1. introduction
-----------------





.. raw:: html
      
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Vision Transformers are type of deep learning model and they are designed for computer vision tasks, they are inspired by the success of Transformer models in natural language processing. Traditionally computer used a technique called convolutional neural networks for computer vision tasks but now the vision Transformers are newer approach that gained a lot of attention.
    </i></span></p>


.. figure:: /Documentation/images/vit1.jpg
    :width: 700
    :align: center
    :alt: Alternative Text

.. raw:: html
      
    <p style="text-align: justify;"><span style="color:#000080;">
    
    </span></p>


For more Understanding Vision Transformers

.. admonition:: link for more information

   .. container:: custom-red-box

      * `Vision Transformers <https://paperswithcode.com/method/vision-transformer>`__



.. raw:: html
      
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    The vision Transformer architecture. In this example, an image is split into nine patches. A special “<cls>” token and the nine flattened image patches are transformed via patch embedding and <strong><i> n </i></strong>Transformer encoder blocks into ten representations, respectively. The “<cls>” representation is further transformed into the output label.
    
    </i></span></p>

.. figure:: /Documentation/images/Patch_embeddingint.jpg
    :width: 700
    :align: center
    :alt: Alternative Text


.. raw:: html
      
    <p style="text-align: justify;"><span style="color:#000080;">
    
    </span></p>

For more Understanding Vision Transformers

.. admonition:: link for more information

   .. container:: custom-red-box

      * `The vision Transformer architecture <https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html#fig-vit>`__


.. note::

    Let’s explain how the vision transformer works step by step with an example.


2. Patch Embedding 
-----------------------


* **example**

.. figure:: /Documentation/images/Patch_embedding.jpg
    :align: center
    :alt: Alternative Text

.. raw:: html
      
    <p style="text-align: justify;"><span style="color:#000080;">
    Patch = Square region of the image (4 patches in the example above)
    </span></p>

.. figure:: /Documentation/images/Patch_embedding1.jpg
    :align: center
    :alt: Alternative Text
.. raw:: html
      
    <p style="text-align: justify;"><i>

    In the example, we have an<span style="color:#000080;"> image size 224x224</span> pixels <span style="color:#000080;">the patch size is 16x16 pixels</span>, so we divide the width and height of the image by the patch size to get the total number of patches. In this case we would end up with <span style="color:#000080;">196 patches </span>covering the entire image.
    </i></p>

    <p style="text-align: justify;"><span style="color:#000080;">

    <i>An additional concept is the stride, meaning how many pixels the sliding moves each time. The stride used in the original paper is also 16.  So there would be no overlap between the patches because stride is equal to the patch size.
    </i></span></p>




3. Flattening and Positional Encoding 
----------------------------------------


.. figure:: /Documentation/images/Patch_embedding2.jpg
    :align: center
    :alt: Alternative Text












