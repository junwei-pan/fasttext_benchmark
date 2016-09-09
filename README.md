# fasttext_benchmark

Test the fasttext model on text classification over several datasets provided in Xiang Zhang's paper [Character-level Convolutional Networks for Text Classification](http://arxiv.org/abs/1509.01626)([Download Datasets from Google Drive](https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M)), the code is based on the fasttext example on keras: [keras fasttext example](https://github.com/fchollet/keras/blob/master/examples/imdb_fasttext.py).

## Experiment results

- ag_news

| embedding_dim | 1 epoch | 2 epochs | 3 epochs | 4 epochs | 5 epochs |
| --- | --- | --- | --- | --- | --- |
| 20 | 84.89% | 86.70% | 87.86% | 88.54% | 89.50% |
| 50 | 86.29% | 88.01% | 89.34% | 89.92% | 90.32% |


- dbpedia


| embedding_dim | 1 epoch | 2 epochs | 3 epochs | 4 epochs | 5 epochs |
| --- | --- | --- | --- | --- | --- |
| 20 | 94.06% | 96.36% | 97.05% | 97.40% | 97.56% |
| 50 | - | - | - | - | - |

## Reference

 1. [Bags of Tricks for Efficient Text Classification](https://arxiv.org/abs/1607.01759)
 2. [Character-level Convolutional Networks for Text Classification](http://arxiv.org/abs/1509.01626)
 3. [keras fasttext example](https://github.com/fchollet/keras/blob/master/examples/imdb_fasttext.py)
