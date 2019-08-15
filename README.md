# SentimentAnalysis

These files track my fun learning of basic sentiment analysis techniques using 3 datasets of reviews
1. Yelp
2. Amazon
3. IMDB

## Files
### text_classification_IMDB_reviews_BOW
This file was really a warm up to the topic. It uses the IMDB data set that comes with a vector embedding of words similar to the Bag of Words approach where
a word's value comes from it index in a dictionary. I was able to get 84% accuracy here on a test set of 25k reviews using a 
simple Neural Network

### baseline_bow
This file serves as my baseline model using a Bag of Words approach to embed the reviews as well as a simple Logicstical Reggression model. The accuracy after training only on 75% of the Yelp reviews is as follows:
Yelp: 94%
Amazon: 74%
IMDB: 66%

### Future Work: using Word2Vec to embed words, using a CNN to build the model, trying out Google's [BERT](https://github.com/google-research/bert) if possible
