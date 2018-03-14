import pandas as pd
import numpy as np
from trainers import AdalineGD

multiplier = (float(71450 + 70891 + 81175)/3.0)/10000.0

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)


# versicolor and virginica
y = df.iloc[50:150, 4].values
y = np.where(y == 'Iris-virginica', -1, 1)

# sepal width and petal width
X = df.iloc[50:150, [0,2]].values


import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

eta = multiplier/100000.0
print eta
ada = AdalineGD(epochs=100, eta=eta)

X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

ada.train(X_std, y)

plot_decision_regions(X_std, y, clf=ada)
plt.title('Adaline - Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.show()

plt.plot(range(1, len( ada.cost_)+1), ada.cost_)
plt.xlabel('Iterations')
plt.ylabel('Sum-squared-error')
plt.show()
