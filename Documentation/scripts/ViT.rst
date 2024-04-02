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


.. figure:: /Documentation/images/Patch_embedding1.jpg
    :align: center
    :alt: Alternative Text


.. figure:: /Documentation/images/Patch_embedding2.jpg
    :align: center
    :alt: Alternative Text



3. Flattening and Positional Encoding 
----------------------------------------


.. figure:: /Documentation/images/Patch_embedding2.jpg
    :align: center
    :alt: Alternative Text












