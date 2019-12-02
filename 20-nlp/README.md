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
