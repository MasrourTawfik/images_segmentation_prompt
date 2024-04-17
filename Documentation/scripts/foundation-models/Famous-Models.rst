Famous Models
===============

.. raw:: html

    <p><span style="color:white;">'</p></span>


.. figure:: /Documentation/images/foundation-models/grounding-DINO/1.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image

grounding DINO
---------------

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    As of March 2023, there is a new SOTA zero-shot object detection model - Grounding DINO. In this post, we will talk about the advantages of Grounding DINO, analyze the model architecture, and provide real prompt examples. 
   </i></span></p>

    <p><span style="color:white;">'</p></span>
    

1. Introduction
_________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>

    Most object detection models are trained to identify a narrow predetermined collection of classes. The main problem with this is the lack of flexibility. Every time you want to expand or change the set of recognizable objects, you have to collect data, label it, and train the model again. This — of course — is  time-consuming and expensive.
   </i></span></p>

    <p style="text-align: justify;"><span style="color:#000080;"><i>

    Zero-shot detectors want to break this status quo by making it possible to detect new objects without re-training a model. All you have to do is change the prompt and the model will detect the objects you describe.
   </i></span></p>

    <p style="text-align: justify;"><span style="color:#000080;"><i>

    Below we see two images visualizing predictions made with</span><span style="color:red;"><strong> Grounding DINO</span></strong><span style="color:#000080;"> — the new SOTA zero-shot object detection model.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>

    In the case of the images below, we asked the model to identify the class <strong>" '</span><span style="color:red;">piano</span><span style="color:#000080;">', '</span><span style="color:red;">guitar</span><span style="color:#000080;">','</span><span style="color:red;">phone</span><span style="color:#000080;">','</span><span style="color:red;">hat</span><span style="color:#000080;">' "</span></strong> <span style="color:#000080;"> a class belonging to the COCO dataset. The model successfully detected all objects of this class without any issues.
   </i></span></p>

    <p><span style="color:white;">'</p></span>

   <strong> text prompt :</strong>['<span style="color:blue;">piano</span>', '<span style="color:blue;">guitar</span>', '<span style="color:blue;">phone</span>', '<span style="color:blue;">hat</span>'] 


.. figure:: /Documentation/images/foundation-models/grounding-DINO/2.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image


.. figure:: /Documentation/images/foundation-models/grounding-DINO/3.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image



.. figure:: /Documentation/images/foundation-models/grounding-DINO/4.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image

.. raw:: html

    <p><span style="color:white;">'</p></span>


2. Grounding DINO Performance
_______________________________

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Grounding DINO achieves a <strong>52.5 AP</strong> on the COCO detection zero-shot transfer benchmark — without any training data from COCO. After finetuning with COCO data, Grounding DINO reaches <strong>63.0 AP</strong> . It sets a new record on the ODinW zero-shot benchmark with a mean of <strong>26.1 AP</strong>.
    </p></span></i>
    <p><span style="color:white;">'</p></span>
    
*GLIP T vs. Grounding DINO T speed and mAP comparison*

.. figure:: /Documentation/images/foundation-models/grounding-DINO/5.webp
   :width: 700
   :align: center
   :alt: Alternative text for the image


.. raw:: html

    <p><span style="color:white;">'</p></span>
    
  
3. Advantages of Grounding DINO
________________________________


.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Zero-Shot Object Detection — Grounding DINO excels at detecting objects even when they are not part of the predefined set of classes in the training data. This unique capability enables the model to adapt to novel objects and scenarios, making it highly versatile and applicable to various real-world tasks.
    </p></span></i>    
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Referring Expression Comprehension (REC) — Identifying and localizing a specific object or region within an image is based on a given textual description. In other words, instead of detecting people and chairs in an image and then writing custom logic to determine whether a chair is occupied, prompt engineering can be used to ask the model to detect only those chairs where a person is sitting. This requires the model to possess a deep understanding of both the language and the visual content, as well as the ability to associate words or phrases with corresponding visual elements.
    </p></span></i>    
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Elimination of Hand-Designed Components like NMS — Grounding DINO simplifies the object detection pipeline by removing the need for hand-designed components, such as Non-Maximum Suppression (NMS). This streamlines the model architecture and training process while improving efficiency and performance.
    </p></span></i>

    <p><span style="color:white;">'</p></span>


.. admonition::  For more information 

   .. container:: blue-box
    
    * `"Non-Maximum Suppression (NMS)." <https://blog.roboflow.com/grounding-dino-zero-shot-object-detection/#introduction>`__



.. raw:: html

    <p><span style="color:white;">'</p></span>


4. Grounding DINO Architecture
________________________________



.. raw:: html

    <span style="color:blue;"><streams>Model architecture</strong></span>
    
    <p style="text-align: justify;"><span style="color:#000080;"><i>

    Grounding DINO aims to merge concepts found in the </span><span style="color:blue;">DINO</span><span style="color:#000080;"> and </span><span style="color:blue;">GLIP</span><span style="color:#000080;"> papers. DINO, a transformer-based detection method, </span><span style="color:blue;">offers state-of-the-art object detection performance</span><span style="color:#000080;"> and end-to-end optimization, eliminating the need for handcrafted modules like NMS (Non-Maximum Suppression).
    </p></span></i>    
  
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    On the other hand, GLIP focuses on </span><span style="color:blue;">phrase grounding.</span><span style="color:#000080;"> This task involves associating phrases or words from a given text with corresponding visual elements in an image or video, effectively linking textual descriptions to their respective visual representations.
    </p></span></i>    


    <p style="text-align: justify;"><span style="color:blue;"><i>
    Text backbone and Image backbone </span><span style="color:#000080;"> — Multiscale image features are extracted using an image backbone like Swin Transformer, and text features are extracted with a text backbone like BERT.
    </p></span></i> 

.. figure:: /Documentation/images/foundation-models/grounding-DINO/10.webp
   :width: 700
   :align: center
   :alt: Alternative text for the image


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


.. raw:: html


    <p style="text-align: justify;"><span style="color:#000080;"><i>
    The model will first use its understanding of language to identify the objects that are mentioned in the text prompt. For example, in the description “two dogs with a stick,” the model would identify the words “dogs” and “stick” as objects
   </p></span></i>  

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    The model will then generate a set of object proposals for each object that was identified in the natural language description. The object proposals are generated using a variety of features such as the color, shape, and texture of the objects
   </p></span></i>  

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    Next, the score for each object proposal is returned by the model. The score is a measure of how likely it is that the object proposal contains an actual object
   </p></span></i>  

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    The model would then select the top-scoring object proposals as the final detections. The final detections are the objects that the model is most confident are present in the image
   </p></span></i>  

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    In this case, the model would likely detect the two dogs and the stick in the image. The model would also likely score the two dogs higher than the stick, because the dogs are larger and more prominent in the image.
   </p></span></i>  


    <p><span style="color:white;">'</p></span>

Segment Anyting Model
-------------------------
