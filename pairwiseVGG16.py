import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_distances

# Carregar o modelo pré-treinado VGG16 sem a camada de classificação
base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')
model = Model(inputs=base_model.input, outputs=base_model.output)

# Carregar suas imagens e pré-processá-las
# ...

# Extrair vetores de características para as imagens
features = model.predict(preprocessed_images)

# Calcular a matriz de distâncias cosseno entre os vetores de características
similarity_matrix = cosine_distances(features)

# Dada uma imagem de consulta, encontre as imagens mais similares
query_image_features = model.predict(preprocess_query_image)
query_distances = cosine_distances(query_image_features, features)
most_similar_indices = np.argsort(query_distances)[0]

# Recomende as imagens mais similares para o usuário
recommended_images = [images[i] for i in most_similar_indices]

# Exibir as recomendações ou realizar outras ações
print("Imagens recomendadas:", recommended_images)
