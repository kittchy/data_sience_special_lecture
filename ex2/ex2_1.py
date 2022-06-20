from sklearn.datasets import load_iris
from scipy.spatial import distance
import numpy as np

iris = load_iris()

iris_category_mean = np.average(iris.data, axis=0).reshape(4, 1)
iris_covariance = np.cov(iris.data, rowvar=False)
print(f"平均=\n{iris_category_mean}")
print(f"共分散行列=\n{iris_covariance}")
