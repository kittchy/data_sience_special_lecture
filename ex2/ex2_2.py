from sklearn.datasets import load_iris
from scipy.spatial import distance
import numpy as np

iris = load_iris()

iris_category_mean = np.average(iris.data, axis=0).reshape(4, 1)
iris_covariance = np.cov(iris.data, rowvar=False)

select_iris_data_index = np.random.randint(0, 149, 6)
iris_category = iris.target_names

for i in range(0, 6, 2):
    iris_data1 = iris.data[select_iris_data_index[i]]
    iris_data2 = iris.data[select_iris_data_index[i + 1]]
    iris_euclid = distance.euclidean(
        iris.data[select_iris_data_index[i]], iris.data[select_iris_data_index[i + 1]]
    )
    iris_mahalanobis = distance.mahalanobis(
        iris.data[select_iris_data_index[i]],
        iris.data[select_iris_data_index[i + 1]],
        np.linalg.pinv(iris_covariance),
    )

    print(f"試行{int(i / 2 + 1)}")
    print(
        f"1つ目のデータ: index = {select_iris_data_index[i]}, {iris_category[iris.target[select_iris_data_index[i]]]}: {iris_data1}"
    )
    print(
        f"2つ目のデータ: index = {select_iris_data_index[i+1]}, {iris_category[iris.target[select_iris_data_index[i+1]]]}: {iris_data2}"
    )
    print(f"Euclid(x, y) = {iris_euclid:.4f}")
    print(f"Mahalanobis(x, y) = {iris_mahalanobis:.4f} \n")