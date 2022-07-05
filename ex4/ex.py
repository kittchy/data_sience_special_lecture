import numpy as np


def pageMat(mat):
    return (mat.T / np.sum(mat, axis=1))


def pageRank(mat):
    e_vals, e_vecs = np.linalg.eig(pageMat(mat))
    # print("Eigenvalue", np.round(e_vals.real, 3))
    # print("Eigenvector", np.round(e_vecs[:, 0].real, 3))
    myVec = np.abs(e_vecs[:, 0].real)
    sumVec = np.sum(myVec)
    pageVec = myVec / sumVec
    indices = np.argsort(pageVec)[::-1]
    print("Web Id:", indices+1)
    print("PageRank:", np.round(pageVec[indices], 3))
    return indices, pageVec


def calcHITS(mat):
    A = np.dot(mat.T, mat)
    H = np.dot(mat, mat.T)
    eA_vals, eA_vecs = np.linalg.eig(A)
    eH_vals, eH_vecs = np.linalg.eig(H)
    myVecA = np.abs(eA_vecs[:, 0].real)
    myVecH = np.abs(eH_vecs[:, 0].real)
    # Authority
    indicesA = np.argsort(myVecA)[::-1]
    print("Authority Id:", indicesA + 1)
    print("Authority:", np.round(myVecA[indicesA], 3))
    indicesH = np.argsort(myVecH)[::-1]
    print("Hub Id:", indicesH + 1)
    print("Hub:", np.round(myVecH[indicesH], 3))
    return ((indicesA, myVecA), (indicesH, myVecH))


if __name__ == "__main__":
    np.set_printoptions(precision=3, floatmode='fixed')
    
    import pandas as pd
    url = 'http://www.tutarc.org/Seminar/Python/data/PageRankSample.csv'
    # url = 'http://www.tutarc.org/Seminar/Python/data/HITSsample.csv'
    cr = pd.read_csv(url)
    data = cr.values
    pMat = data[:, :]
    pMat = pMat.astype(float)
    A = np.array(pMat)

    print("(1)隣接行列")
    print(A)
    # print(pageMat(A))

    print("(2)PageRank")
    pageRank(A)
    
    print("(3)HITS")
    calcHITS(A)