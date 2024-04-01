The Encoder
===========

.. figure:: /Documentation/images/encoder.webp
   :width:  700
   :align: center
   :alt: Alternative Text


1. Tokenizer 
-------------


.. figure:: /Documentation/images/token.jpg
   :width:  500
   :align: center
   :alt: Alternative Text

.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">
   Tokenization:
   </span></p>
.. raw:: html

    <p style="text-align: justify;"><span style="color:#000080;">
      
   &#10003; Tokenization is the process of dividing a text into smaller units called "tokens."
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; These tokens can be individual words, sub-words, or even individual characters, depending on the desired level of granularity.
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; Each token is then converted into its corresponding numerical identifier from the model's vocabulary.
   </span></p>

.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">
   Vocabulary Building:
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; To build the vocabulary, a set of the most common tokens in the language is typically selected.
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; The vocabulary is limited to a certain number of tokens for performance and efficiency reasons, usually tens of thousands of tokens.
   </span></p>

.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">
   Token ID:
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; Each token is associated with a unique identifier called a "Token ID."
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">
   
   &#10003; These Token IDs serve as numerical references for each token in the model's vocabulary.
   </span></p>

.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">
   Vocabulary Limitations:
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; Due to the limitation of vocabulary size, some words may not be present in the model's vocabulary.
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">

   &#10003; In such cases, these words are usually split into sub-words or characters to represent them using the available tokens in the vocabulary.
   </span></p>

2. Input embedding
-------------------

.. figure:: /Documentation/images/input_embe.jpg
   :width:  500
   :align: center
   :alt: Alternative Text


.. raw:: html

   <p style="text-align: justify;"><span style="color:#000080;">
   Refers to the initial step of converting the discrete tokens of an input sequence into continuous vector representations. This process is essential for the model to work with the input data in a suitable format.
   </span></p>

.. raw:: html

    <p style="text-align: justify;"><span style="color:blue;">
   Tokenization:
   </span></p>

.. figure:: /Documentation/images/input.jpg
   :width:  500
   :align: center
   :alt: Alternative Text

.. raw:: html

   <p style="text-align: justify;"><span style="color:#000080;">
   The input sequence, which could be a sequence of words, subwords, or characters, is first broken down into individual tokens. Each token typically represents a unit of meaning, like a word or a subword.
   </span></p>


    <p style="text-align: justify;"><span style="color:blue;">
   Embedding Representation:
   </span></p>


   <p style="text-align: justify;"><span style="color:#000080;">
   Each token ID is associated with an embedding vector, where these vectors are initially randomly initialized. These vectors are of a fixed size, typically 512 dimensions.
   </span></p>


    <p style="text-align: justify;"><span style="color:blue;">
   Vector Representation:
   </span></p>


   <p style="text-align: justify;"><span style="color:#000080;">
   These embedding vectors are arranged in columns, with each column representing a dimension of the embedding vector. This is different from the usual row-wise representation, where each row represents a token.
   </span></p>


    <p style="text-align: justify;"><span style="color:blue;">
   Random Initialization:
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">  

    The values in the embedding vectors are initially set randomly. These values represent the initial state of the embeddings, and the Transformer model optimizes these values during training to better represent the semantics of the tokens.
   </span></p>
   <p style="text-align: justify;"><span style="color:#000080;">  

    To sum up, the process involves tokenizing the input sentence, looking up each token in the vocabulary to retrieve its ID, then using this ID to obtain the corresponding embedding vector. These embedding vectors are represented in a column-wise format, with each column representing a dimension of the embedding vector. Initially, these vectors are randomly initialized, and the Transformer model learns to optimize them during training.
   </span></p>