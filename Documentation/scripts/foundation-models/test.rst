

.. raw:: html


    <p style="text-align: justify;"><span style="color:#000080;"><i>

    The output of these two streams are fed into a feature enhancer for transforming the two sets of features into a single unified representation space. The feature enhancer includes multiple feature enhancer layers. Deformable self-attention is utilized to enhance image features, and regular self-attention is used for text feature enhancers.
    </p></span></i>    


.. figure:: /Documentation/images/foundation-models/grounding-DINO/7.webp
   :width: 700
   :align: center
   :alt: Alternative text for the image


.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>

   Grounding DINO aims to detect objects from an image specified by an input text. In order to effectively leverage the input text for object detection, a language-guided query selection is used to select most relevant features from both the image and text inputs. These queries guide the decoder in identifying the locations of objects in the image and assigning them appropriate labels based on the text descriptions.
   </p></span></i>    


.. figure:: /Documentation/images/foundation-models/grounding-DINO/8.webp
   :width: 700
   :align: center
   :alt: Alternative text for the image


.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>

    A cross-modality decoder is then used to integrate text and image modality features. The cross-modality decoder operates by processing the fused features and decoder queries through a series of attention layers and feed-forward networks. These layers allow the decoder to effectively capture the relationships between the visual and textual information, enabling it to refine the object detections and assign appropriate labels. After this step, the model proceedes with the final steps in the object detection including bounding box prediction, class specific confidence filtering and label assignment.
   </p></span></i> 

    <p><span style="color:white;">'</p></span>

    <span style="color:blue;"><streams>How it works?</strong></span>

Here is how Grounding DINO would work on this image:


.. figure:: /Documentation/images/foundation-models/grounding-DINO/8.webp
   :width: 700
   :align: center
   :alt: Alternative text for the image


