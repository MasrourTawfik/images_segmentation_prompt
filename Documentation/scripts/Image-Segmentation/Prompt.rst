Prompt Generator / Analyzer 
=============================

------------------------------------------------------------------------------



.. admonition::  contents 

   .. container:: blue-box





.. raw:: html

    <p><span style="color:white;">'</p></span>


.. figure:: /Documentation/images/IMAGE/promptAnalyzer.jpg
   :width: 100
   :align: center
   :alt: Alternative text for the image


Overview
----------


.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;"><i>

    The prompt_analyzer</span><span style="color:#000080;"> is designed to analyze sets of prompts associated with images and generated using gemini pro vision model. After properly </span><span style="color:blue;">processing the prompts</span><span style="color:#000080;">, removing similarities based on user set threshold, </span><span style="color:blue;">the prompt_analyzer</span><span style="color:#000080;"> evaluates them based on complexity and readability to identify the most effective prompts.
    It leverages various Python libraries including NLTK for natural language processing, scikit-learn for feature extraction and cosine similarity, and others for specific linguistic tasks.
   </i></span></p>

    <p><span style="color:white;">'</p></span>
    
Prompt Gemini Generator
-------------------------

.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    The prompt_generator class is designed to automate the creation of textual prompts for images using </span><span style="color:blue;">Gemini pro Vision API.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    
    </i></span></p>
    The prompt_generator class automates the process of generating text from images, offering a bridge between visual content and textual descriptions through advanced machine learning techniques.
    <p style="text-align: justify;"><span style="color:#000080;"><i>

**Parameters:**

.. raw:: html

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    - Model: Identifier or configuration for a generative model.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    - key: API key for accessing the generative model's service.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    - Images_dir: Directory path where image files are stored.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    - Images_extensions: List of image file extensions to consider.
    </i></span></p>
    
    <p><span style="color:white;">'</p></span>
