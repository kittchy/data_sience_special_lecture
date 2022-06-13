from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()

plt.figure(figsize=(10,10))

# setosa
plt.scatter(x=iris.data[iris.target==0,0],
            y=iris.data[iris.target==0,1],
            label=iris.target_names[0],
            c='red'
)

# versicolor
plt.scatter(x=iris.data[iris.target==1,0],
            y=iris.data[iris.target==1,1],
            label=iris.target_names[1],
            c='blue'
)
# virginica
plt.scatter(x=iris.data[iris.target==2,0],
            y=iris.data[iris.target==2,1],
            label=iris.target_names[2],
            c='green'
)

plt.legend(loc='best', fontsize=14)

plt.title('Iris SepalLength / SepalWidth', size=16)
plt.xlabel(iris.feature_names[0], size=14)
plt.ylabel(iris.feature_names[1], size=14)

plt.savefig("Iris-SepalLength-SepalWidth.pdf")
#plt.show()