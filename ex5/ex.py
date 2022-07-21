
from sklearn import cluster
import numpy as np
from sklearn.datasets import load_iris


def load_data():
    iris = load_iris()  # あやめのデータをロード
    return iris.feature_names, iris.data, iris.target_names, iris.target



def create_cross_table(truth, predict):
    result = [[0] * len(set(truth)) for _ in range(len(set(predict)))]
    for p, t in zip(predict, truth):
        result[p][t] += 1
    return result


def purity(CT):
    return np.sum(np.max(CT, axis=1)) / np.sum(CT)


if __name__ == "__main__":
    _, data, _, target = load_data()  # データの読み込み

    k_means = cluster.KMeans(n_clusters=len(set(target)))
    k_means.fit(data)  # k_meansのfitting
    predicted = k_means.predict(data)
    truth = target.copy()
    for d, p, t in zip(data, predicted, truth):
        print(f"data: {d}   truth: {t}  purity: {p}")
    CT = create_cross_table(truth, predicted)
    purity_val = purity(CT)
    print(f"Purity: {purity_val}")
