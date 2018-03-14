from dataset_visualizer import loadDataset, plotDataset
from mlxtend.plotting import plot_decision_regions
from trainers import AdalineGD
import matplotlib.pyplot as plt
import numpy as np

multiplier = (float(7+1+4+5+0 + 7+0+8+9+1 + 8+1+1+7+5)/15.0)

X, y = loadDataset('iris_data')
#plotDataset(ds, gt)
print multiplier
eta = multiplier/100.0
ada = AdalineGD(epochs=5, eta=eta)

#print X

X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

ada.train(X_std, y)

print('Weights: %s' % ada.w_)
plot_decision_regions(X_std, y, clf=ada)
plt.title('Adaline')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.show()

plt.plot(range(1, len(ada.cost_)+1), ada.cost_)
plt.xlabel('Iterations')
plt.ylabel('Misclassifications')
#plt.ylim((0,200))
plt.show()
