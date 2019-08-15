# SentimentAnalysis

These files track my fun learning of basic sentiment analysis techniques using 3 datasets of review. The goal here is to be able to determine wether a specific review is positive or negative. This is currently on-going for me. I've listed next steps for me at the bottom of this readme.
#### Review Data:
1. Yelp
2. Amazon
3. IMDB

## Files
### text_classification_IMDB_reviews_BOW
This file was really a warm up to the topic. It uses the IMDB data set that comes with a vector embedding of words similar to the Bag of Words approach where
a word's value comes from it index in a dictionary. I was able to get 84% accuracy here on a test set of 25k reviews using a 
simple Neural Network

### baseline_bow_logistic_regression
This file serves as my baseline model using a Bag of Words approach to embed the reviews as well as a simple Logicstical Reggression model. Training was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 94%
##### Amazon: 74%
##### IMDB: 66%

### nn_bow
This file uses the same Bag of Words approach to creating feature vectors but tests wether or not a simlple neural network will perform better. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 95%
##### Amazon: 73%
##### IMDB: 72%


## Future Work
using Word2Vec to embed words
using a CNN to build the model
trying out Google's [BERT](https://github.com/google-research/bert) if possible
