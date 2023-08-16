from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix

# Suponha que y_true são as verdadeiras classes e y_pred são as classes previstas pelo modelo
y_true = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
y_pred = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]

# Calcular acurácia
accuracy = accuracy_score(y_true, y_pred)
print("Acurácia:", accuracy)

# Calcular matriz de confusão
conf_matrix = confusion_matrix(y_true, y_pred)
print("Matriz de Confusão:")
print(conf_matrix)

# Calcular sensibilidade (recall)
recall = recall_score(y_true, y_pred)
print("Sensibilidade (Recall):", recall)

# Calcular especificidade
specificity = conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[0, 1])
print("Especificidade:", specificity)

# Calcular precisão
precision = precision_score(y_true, y_pred)
print("Precisão:", precision)

# Calcular F-score
f_score = f1_score(y_true, y_pred)
print("F-score:", f_score)
