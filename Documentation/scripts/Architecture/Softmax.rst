

Softmax in Transformers
=======================
.. raw:: html
      
   <p style="text-align: justify;"><span style="color:#000080;">

    In transformers, the softmax function is commonly used as part of the mechanism for calculating attention scores, which are critical for the self-attention mechanism that forms the basis of the model. It is essential for several reasons:
   </span></p>

    <p style="text-align: justify;">
    
     -<span style="color:blue;"> Attention Weights</span>: <span style="color:#000080;">Transformers use attention mechanisms to weigh the importance of different input tokens when generating an output. Softmax is used to convert the raw attention scores, often called “logits,” into a probability distribution over the input tokens. This distribution assigns higher attention weights to more relevant tokens and lower weights to less relevant ones.
    
    </span></p>
    <p style="text-align: justify;">
     - <span style="color:blue;"> Probability Distribution</span>:<span style="color:#000080;"> Softmax ensures that the attention scores are transformed into a valid probability distribution, with all values between 0 and 1 and the sum equal to 1. This property is important for correctly weighing the input tokens while taking into account their relative importance.
    
    </span></p>
    <p style="text-align: justify;">
     - <span style="color:blue;"> Stabilizing Gradients</span>:<span style="color:#000080;">The softmax function has a smooth gradient, which makes it easier to train deep neural networks like transformers using techniques like backpropagation. It helps with gradient stability during training, making it easier for the model to learn and adjust its parameters.
    </span></p>
    
    <p style="text-align: justify;"><span style="color:#000080;">

    The softmax function is typically applied to the raw attention scores obtained from the dot product of query and key vectors in the self-attention mechanism. The formula for computing the softmax attention weights for a given query token in a transformer is as follows:
   </span></p>


.. math::

   \text{Softmax}(QK^\top) = \frac{\exp(QK_i^\top)}{\sum_j \exp(QK_j^\top)}


.. raw:: html
      
   <p style="text-align: justify;"><span style="color:#000080;">

    Here, :math:`Q` represents the query vector, :math:`K` represents the key vectors of the input tokens, and the exponential function (\exp) is used to transform the raw scores into positive values. The denominator ensures that the resulting values form a probability distribution.
   </span></p>
    <p style="text-align: justify;"><span style="color:#000080;">

    In summary, the softmax function is a crucial component of transformers that enables them to learn how to weigh input tokens based on their relevance to the current context, making the model’s self-attention mechanism effective in capturing dependencies and relationships in the data.
    </span></p>
    <p style="text-align: justify;"><span style="color:#000080;">

    And the most important thing is the softmax is used to prevent exploding gradient or vanishing gradient problems.
   </span></p>