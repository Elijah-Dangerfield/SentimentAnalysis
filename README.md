# SentimentAnalysis

These files track my fun learning of basic sentiment analysis techniques using 3 datasets of reviews. The goal here is to be able to determine wether a specific review is positive or negative. This is currently on-going for me. I've listed next steps for me at the bottom of this readme.
#### Review Data:
1. Yelp 1000 reviews
2. Amazon 1000 reviews
3. IMDB 748 reviews

## Files
### Util.py
This file just contains methods I found myself needing to use on mutliple occasions. I call these rather than re-write them.

### baseline_bow_logistic_regression
This file serves as my baseline model using a Bag of Words approach to vectorize the reviews as well as a simple Logicstical Reggression model. Training was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 94%,  Amazon: 74%, IMDB: 66%

### nn_bow
This file uses the same Bag of Words approach to creating feature vectors but tests wether or not a simlple neural network will perform better. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 95%, Amazon: 73%, IMDB: 72%

### word_embed
This file uses the built in Keras embedding layer to create more meaningful word vectors. Still uses a simple NN. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 96%, Amazon: 76%, IMDB: 72%

### nn_pretrained_embeddings
This file uses GloVe's pretrained word embeddings. Still uses a simple NN. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 94%, Amazon: 72%, IMDB: 71%

### cnn_pretrained_embeddings
This file uses GloVe's pretrained word embeddings. This time however we use a Convolutional Neural Net. Training again was only performed on 75% of the yelp reviews. These are the accuracy results for the entire dataset: 
##### Yelp: 95% ,Amazon: 73%, IMDB: 72%

### cnn_splits
This files uses Scikit leans Random search to explore differing hypter peramters for the CNN model. I found that the best parameters are as follows: 
#### Best Accuracy : 0.8160  Test Accuracy : 0.8120
##### {'vocab_size': 5000, 'num_filters': 32, 'maxlen': 100, 'kernel_size': 3, 'embedding_dim': 100}

### cnn_full_split
This files uses the parameters found in cnn_splits to train a model using the combination of the 3 data sets with a 75/25 taining test split. I also added a Dropout layer considering i've been working with a small dataset. Not sure that helped too much considering these results:

##### Training Accuracy: 100% , Testing Accuracy: 83%

## Results so far
##### It is very interesting but at least for this dataset, simply using Keras's built in word embedding performs best. However, it is not much better than the other models with what seems to be a natural 80% cap given our dataset.



## Future Work
##### using Word2Vec to embed words
##### looking at different networks such as LSTM
##### finding and using a larger dataset
##### tuning hyperperameters in models
##### try out differing test, train folds
##### trying out Google's [BERT](https://github.com/google-research/bert) if possible
