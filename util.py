import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def get_full_data_frame():
    filepath_dict = {'yelp': './data/yelp_labelled.txt',
                     'amazon': './data/amazon_cells_labelled.txt',
                     'imdb': './data/imdb_labelled.txt'}
    df_list = []
    for source, path in filepath_dict.items():
        df = pd.read_csv(path, names=['sentence', 'label'], sep='\t')
        df['source'] = source
        df_list.append(df)

    return pd.concat(df_list)

def plot_history(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
