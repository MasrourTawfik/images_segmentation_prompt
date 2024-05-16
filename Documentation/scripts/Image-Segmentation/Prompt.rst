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
    <p style="text-align: justify;"><span style="color:blue;"><i>
    - Model:</span><span style="color:#000080;"> Identifier or configuration for a generative model.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>
    - key:</span><span style="color:#000080;"> API key for accessing the generative model's service.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>
    - Images_dir:</span><span style="color:#000080;"> Directory path where image files are stored.

    </i></span></p>
    <p style="text-align: justify;"><span style="color:blue;"><i>
    - Images_extensions:</span><span style="color:#000080;"> List of image file extensions to consider.
    </i></span></p>

    <p><span style="color:white;">'</p></span>

**Operations:**

.. raw:: html

    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Configures the generative model with the provided API key (gai.configure).
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Configures the generative model with the provided API key (gai.configure).
    </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Retrieves and stores paths to images within the specified directory that match the given extensions using sv.list_files_with_extensions.
      </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    .  Initializes a dictionary (prompts_dict) to store the generated prompts indexed by image name.
      </i></span></p>

    <p><span style="color:white;">'</p></span>

**Prompt Generation (generate_prompts):**

.. raw:: html

    <span style="color:blue;"><strong>Parameter:</strong>
    </span>
    <p style="text-align: justify;"><span style="color:blue;"><i>
    . number_of_prompts:</span><span style="color:#000080;"> Specifies how many prompts to generate per image.
     </i></span></p>

    <span style="color:blue;"><strong>Operations:</strong></span>

    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Iterates over each image file retrieved during initialization.
     </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . For each image, it opens the image file and generates the specified number of prompts using the configured model.
     </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Each prompt's text is added to prompts_dict under the corresponding image name.
     </i></span></p>

    <span style="color:blue;"><strong>Output:</strong></span>
    <p style="text-align: justify;"><span style="color:#000080;"><i>
    . Returns prompts_dict, a dictionary where each key is an image name and the value is a list of generated prompts for that image.
     </i></span></p>
    <span style="color:blue;"><strong>Key Functionalities:</strong></span>


    <p style="text-align: justify;"><i>
    . <span style="color:blue;">Image Handling:</span> <span style="color:#000080;">Opens image files and prepares them for prompt generation.
     </i></span></p>
    <p style="text-align: justify;"><i>
    . <span style="color:blue;">Prompt Generation:</span><span style="color:#000080;">Leverages a deep learning model to generate creative or descriptive text based on the image content.
     </i></span></p>
    <p style="text-align: justify;"><i>
    . <span style="color:blue;">Data Management: </span><span style="color:#000080;">Efficiently manages and catalogs prompts for multiple images, facilitating easy retrieval and usage.
     </i></span></p>

Features
----------

