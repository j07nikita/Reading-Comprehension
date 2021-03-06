# Reading Comprehension 
## Team name: Flying Squad 
## Description
The basic idea is to enable computers to read a document and answer general queries against it. While this sounds like a basic seventh grade task, getting machines to do it requires some understanding about NLP and training neural networks.
The task at hand is therefore to identify types of questions, open or closed domains, and to design an approach that could solve the task of reading and selecting what part of the text could potentially answer the question. As we understand it, this is essentially a question answering task with respect to a short text.
## Related Readings
   #### Comprehension Reader
   Given a question q consisting of l tokens {q1 ,. . . ,ql} and a document of n paragraphs where a single paragraph p 
   consists of m tokens {p 1 , . . . , p m }, we develop an RNN model that we apply to each paragraph in turn and then 
   finally aggregate the predicted answers. Our method works as follows:
   ##### Paragraph Encoding
   We first represent all tokens pi in a paragraph p as a sequence of feature vectors p̃i and pass them as the input to 
   a recurrent neural network.The feature vector p̃i is comprised of the following parts: 
   * Word embeddings
   * Token features   
   ##### Question Encoding
   The question encoding is simpler, as we only apply another recurrent neural network on top of the word embeddings of 
   qi and combine the resulting hidden units into one single P vector: {q1 , . . . , ql} → q.
   #### Prediction
   At the paragraph level, the goal is to predict the span of tokens that is most likely the correct answer. We take the 
   the paragraph vectors {p1 , . . . , pm} and the question vector q as input,and simply train two classifiers 
   independently for predicting the two ends of the span. Concretely,we use a bilinear term to capture the similarity 
   between pi and q and compute the probabilities of each token being start and end as:
   * P_start(i) ∝ exp(pi Ws q)
   * P_end(i) ∝ exp(pi We q)
   
   To make scorescompatible across paragraphs,we use the unnormalized exponential and take argmax over all considered 
   paragraph spans for our final prediction.
## Baseline
We chose to take the similarity based approach, due to the experiments that can be performed in this at the level of word embedding method and grouping of text to be embedded. The idea is to create word embeddings, and then embedding the entire paragraph. We then match words with their presence in the paragraphs to calculate probability. Questions and pasages hhave their own vectors, the sequence of passage vectors need to be weighted according to their relations to the question. This is the approach we plan to start with for the task at hand.
## Dataset
The Stanford Question Answering Dataset **(SQuAD)** is a dataset for machine comprehension based on Wikipedia.
The dataset contains 87k examples for training and 10k for development, with a large hidden test set.
