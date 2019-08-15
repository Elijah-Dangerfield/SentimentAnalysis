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
This file serves as my baseline model using a Bag of Words approach to vectorize the reviews as well as a simple Logicstical Reggression model. Training was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 94%
##### Amazon: 74%
##### IMDB: 66%

### nn_bow
This file uses the same Bag of Words approach to creating feature vectors but tests wether or not a simlple neural network will perform better. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 95%
##### Amazon: 73%
##### IMDB: 72%

### word_embed
This file uses the built in Keras embedding layer to create more meaningful word vectors. Still uses a simple NN. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 96%
##### Amazon: 76%
##### IMDB: 72%

### nn_pretrained_embeddings
This file uses GloVe's pretrained word embeddings. Still uses a simple NN. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 94%
##### Amazon: 72%
##### IMDB: 71%

### cnn_pretrained_embeddings
This file uses GloVe's pretrained word embeddings. This time however we use a Convolutional Neural Net. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 95%
##### Amazon: 73%
##### IMDB: 72%

## Results so far
##### It is very interesting but at least for this dataset, simply using Keras's built in word embedding performs best. However, it is not much better than the other models with what seems to be a natural 80% cap given our dataset. 


## Future Work
##### using Word2Vec to embed words
#### tuning hyperperameters in models
#### try out differing test, train folds
##### trying out Google's [BERT](https://github.com/google-research/bert) if possible
