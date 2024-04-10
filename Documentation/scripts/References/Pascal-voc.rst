PASCAL VOC
==========

.. raw:: html

    <p>

    </p>

.. figure:: /Documentation/images/References/pascale1.jpg
   :width: 400
   :align: left
   :alt: Alternative text for the image


.. raw:: html

    <p>
    |
    </p>
    <p>
    |
    </p>
    <p>
    |
    </p>
   <p>
    |
    </p>

    
Introduction
--------------

.. raw:: html
    
    <p style="text-align: justify;"><span style="color:#000080;"><i>

     - The PASCAL (Pattern Analysis, Statistical Modeling, and Computational Learning) network, funded by the European Union, plays a pivotal role in advancing research in computer vision and machine learning. One of its notable contributions is the establishment of the Visual Object Classes (VOC) Challenge. Running annually from 2005 to 2012, the VOC Challenge has been instrumental in pushing the boundaries of object detection technologies. Participants were provided with a series of images and corresponding annotations, with the challenge to develop models capable of accurately identifying objects within these images.
   
   </i></span></p>

    <p style="text-align: justify;"><span style="color:#000080;"><i>

      -  In response to the inaugural 2005 challenge, the PASCAL VOC XML format was introduced, quickly becoming a standard labeling format within the field. Unlike the COCO JSON format, which uses a single annotation file for all images within a dataset, the VOC format assigns an individual XML file to each image. This approach offers a fine-grained and image-specific annotation process, facilitating detailed object detection and recognition tasks.
   </i></span></p>

    


One annotation:
----------------
.. raw:: html

    <p>

    </p>


.. figure:: /Documentation/images/References/pascale2.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image


.. raw:: html

    <p>

    </p>


.. figure:: /Documentation/images/References/pascale3.jpg
   :width: 700
   :align: center
   :alt: Alternative text for the image

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>

     -  The XML format is structured hierarchically, resembling a tree, and encapsulates all essential information within an 'annotation' tag. Key fields include:   
    </i></span></p>

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    
     -  notice the open and closed bracket for annotation containing all the necessary information:
    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>

    &#10003; Folder name (not important)
    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>

	&#10003; File name (Extremely important): the file name in the voc xml annotation links the image to the annotation.
    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>

    &#10003; Data about the image:</span> <span style="color:#000080;">

    </i></p>
    <p style="text-align: justify;">
        	<strong>Width</strong>

    </p>
    <p style="text-align: justify;">
        	<strong>Height</strong>

    </p>
    <p style="text-align: justify;">
        	<strong>Depth:</strong> 3 RGB channels

    </span></p>

    <p style="text-align: justify;"><span style="color:blue;"><i>

	 <strong> Object: </strong> </span> <span style="color:#000080;">specifies where objects are annotated. 

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
        -  Bounding box <bnd box> these tags are very important, because it stores the coordinates for the bounding box in the corresponding image.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    	 - The box is created with two coordinates: two points in space and then we connect them.

    </i></span></p>


.. figure:: /Documentation/images/References/pascale4.jpg
   :width: 150
   :height: 165
   :align: right
   :alt: Alternative text for the image

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;">
        -  In pascal voc you get the upper left-hand corner of the box and the bottom right-hand corner of the box so the upper left and bottom right if you draw lines between them then you get a nice neat box.
        
    </span></p>


