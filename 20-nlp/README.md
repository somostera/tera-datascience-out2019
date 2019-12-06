# Aula #19 – Processamento de Linguagem Natural & Análise de Sentimento

Nessa aula, vamos aprender sobre processamento de linguagem natural (NLP) através de duas atividades:

* análise de sentimento em um dataset de reviews de produtos (`nlp_parte_1.ipynb`); e

* construção de uma ferramenta para medir a combinação de ingredientes usando um dataset de receitas (`nlp_parte_2.ipynb`).

## Pré-aula

Recomendo a leitura desses dois posts para melhor acompanhamento da aula.

* [Bag of words](http://datameetsmedia.com/bag-of-words-tf-idf-explained/) - técnicas básicas para o processamento de linguagem natural;

* [distância entre vetores](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/).

### Datasets que vamos utilizar

Faça o download dos datasets que utilizaremos durante a aula.

Passo 1: dentro do diretório referente a aula de nlp, na pasta `data/datasets`, crie as seguintes pastas:

* `b2w_reviews`

* `recipes`

Passo 2: faça download dos dados através dos links abaixo:

* https://github.com/b2wdigital/b2w-reviews01/blob/master/B2W-Reviews01.csv

* https://storage.googleapis.com/recipe-box/recipes_raw.zip

Passo 3: coloque os arquivos nas pastas que criamos no passo 1:

* `b2w_reviews`: coloque o arquivo `csv` dentro da pasta `19-nlp/data/datasets/b2w_reviews`.

* `recipes`: extraia o dataset `recipes_raw_nosource_ar.json` na pasta `19-nlp/data/datasets/recipes`.


## Pós-aula

### Links indicados

Falamos de muitas coisas durante a aula e acho que seria muito bom continuar (e reforçar) o aprendizado com os seguintes links:

* [conselhos para aplicar NLP na indústria](https://medium.freecodecamp.org/industrial-strength-natural-language-processing-de2588b6b1ed)
Super recomendo a leitura para todos, já que esses conselhos e observações complementam o que já discutimos durante a aula: não há necessidade de complicar demais uma aplicação.

* [vídeo detalhado sobre o funcionamento do word2vec](https://www.youtube.com/watch?v=ERibwqs9p38)
Essa é uma aula do curso de deep learning para NLP de Stanford e fala sobre o word2vec, incluindo um passo-a-passo de algumas fórmulas.

* [indo além do word2vec](https://towardsdatascience.com/https-medium-com-tanaygahlot-moving-beyond-the-distributional-model-for-word-representation-b0823f1769f8)
Esse post fala sobre algumas soluções para: (i) palavras raras; (ii) múltiplos sentidos de uma palavra; (iii) presença de relações linguísticas entre algumas palavras.

* [usando nltk para pré-processar texto](https://machinelearningmastery.com/clean-text-machine-learning-python/)
Na aula, fizemos praticamente todo o pré-processamento usando o `spacy`. Esse post descreve como fazer grande parte do que fizemos na aula "manualmente" ou usando a biblioteca `nltk`.

* [aplicação do word2vec para encontrar questões similares no Quora](https://towardsdatascience.com/finding-similar-quora-questions-with-word2vec-and-xgboost-1a19ad272c0d)
Esse é um exemplo de uma aplicação que pode ser construída usando `word2vec`. Além de usar o `word2vec`, também é utilizado o `WMD`, que é um método poderoso para calcular a similaridade entre sentenças.

* [várias referências de recursos de NLP](https://github.com/keon/awesome-nlp)
Além de recursos para aprendizado, também tem links para bibliotecas de NLP de várias linguagens, inclusive `Javascript`, por exemplo!

* [curso do fast.ai sobre NLP](https://www.fast.ai/2019/07/08/fastai-nlp/)
Curso com vídeos e notebooks que passa por técnicas mais tradicionais de NLP e chega até técnicas mais recentes, usando deep learning.

Esses dois posts abaixo foram os mencionados durante a aula na parte sobre o `word2vec`:

* [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/)
Um guia ilustrado ao `word2vec`.

* [Learning Word Embedding](https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html)
Uma introdução com direito a fórmulas matemáticas ao tema dos `word vector models`.

### Exemplos de aplicações de NLP na indústria

* [busca do Google com BERT](https://blog.google/products/search/search-language-understanding-bert)

* [recomendações no Airbnb](https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e)

* [extração de keywords no Pinterest](https://medium.com/pinterest-engineering/understanding-pins-through-keyword-extraction-40cf94214c18)
