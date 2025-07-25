# -*- coding: utf-8 -*-
"""SVM

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wtvgu-Av7vEPHJTfD-ST4TvQMazMd0hF

## Cleaning Data
"""

import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

df = pd.read_csv("Healthcare-Diabetes.csv")
df.head()

df.info()

# mengecek jumlah null tiap field
for i in df.columns:
  print(f"{i} null sum: {df[i].isnull().sum()}")

# mengecek duplikasi data
print(df.duplicated().sum())

# menghapus outliers
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Buat salinan df
df_clean = df.copy()

# Inisialisasi mask (True untuk baris yang valid)
mask = pd.Series([True] * len(df), index=df.index)

# Daftar kolom yang ingin dikecualikan
exclude_columns = ['Outcome', 'Id']

for column in df.select_dtypes(include=np.number):
    if column in exclude_columns:
        continue  # Lewati kolom yang dikecualikan

    # Visualisasi boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[column])
    plt.title(f"Box Plot untuk {column}")
    plt.show()

    # Hitung IQR dan batas outlier
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Deteksi outlier
    outliers = (df[column] < lower_bound) | (df[column] > upper_bound)
    print(f"Jumlah outlier dalam kolom '{column}': {outliers.sum()}")

    # Gabungkan mask untuk menyaring outlier
    mask &= ~outliers

# Hapus semua baris yang mengandung outlier
df_clean = df[mask]

# Simpan hasil bersih ke variabel df
df = df_clean

print("Jumlah total baris setelah menghapus outlier:", len(df))

# menyimpan dataset bersih
df.to_csv('dataset_bersih.csv', index=False)
print("Dataset sudah terdownload")

"""## SVM"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv('dataset_bersih.csv')
print(data.head())

# Definisikan fitur dan target
X = data[['Glucose', 'Age']]
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build dan train model
svm = SVC(kernel="linear", C=1.0)
svm.fit(X_train, y_train)

# Plot decision boundary
DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel='Glucose',
    ylabel='Age',
)

# Scatter plot training data
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, s=20, edgecolors="k")

# Evaluasi model
y_pred = svm.predict(X_test)

print("===== EVALUASI MODEL =====")
print("Akurasi :", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Tampilkan plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('dataset_bersih.csv')
print(data.head())

# Definisikan fitur dan target
X = data[['Glucose', 'Age']]
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build dan train model dengan kernel poly
svm = SVC(kernel="poly", degree=3, C=1.0)
svm.fit(X_train, y_train)

# Plot decision boundary
DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel='Glucose',
    ylabel='Age',
)

# Scatter plot
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, s=20, edgecolors="k")

# Evaluasi model
y_pred = svm.predict(X_test)

print("===== EVALUASI MODEL =====")
print("Akurasi :", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Tampilkan plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('dataset_bersih.csv')
print(data.head())

# Definisikan fitur dan target
X = data[['Glucose', 'Age']]
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build dan train model dengan kernel RBF
svm = SVC(kernel="rbf", C=1.0, gamma='scale')
svm.fit(X_train, y_train)

# Plot decision boundary
DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel='Glucose',
    ylabel='Age',
)

# Scatter plot
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, s=20, edgecolors="k")

# Evaluasi model
y_pred = svm.predict(X_test)

print("===== EVALUASI MODEL =====")
print("Akurasi :", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Tampilkan plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv('dataset_bersih.csv')
print(data.head())

# Definisikan fitur dan target
X = data[['Glucose', 'Age']]
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build dan train model dengan kernel sigmoid
svm = SVC(kernel="sigmoid", C=1.0, gamma='scale', coef0=0)
svm.fit(X_train, y_train)

# Plot decision boundary
DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel='Glucose',
    ylabel='Age',
)

# Scatter plot
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, s=20, edgecolors="k")

# Evaluasi model
y_pred = svm.predict(X_test)

print("===== EVALUASI MODEL =====")
print("Akurasi :", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Tampilkan plot
plt.show()