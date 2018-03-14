import matplotlib.pyplot as plt
import numpy as np

class Iris:
    def __init__(self, t):
        self.iris_type = ''
        self.slenghts = []
        self.swidths = []
        self.plenghts = []
        self.pwidths = []

    def receive(self, l):
        self.slenghts.append(l[0])
        self.swidths.append(l[1])
        self.plenghts.append(l[2])
        self.pwidths.append(l[3])

def loadDataset(dataset_path):
    f = open(dataset_path, 'r')
    dataset = []
    gtruth = []
    for line in f:
        attr = list(line[:-1].split(','))
        dataset.append(map(float, [attr[1], attr[3]]))
        if attr[-1] == 'Iris-setosa':
            gtruth.append(0)
        elif attr[-1] == 'Iris-versicolor':
            gtruth.append(1)
        elif attr[-1] == 'Iris-virginica':
            gtruth.append(-1)

    f.close()
    return np.asarray(dataset), np.asarray(gtruth)



def plotDataset(dataset, gtruth):
    setosa = Iris('Iris-setosa')
    versicolor = Iris('Iris-versicolor')
    virginica = Iris('Iris-virginica')
    for attributes, iris_type in zip(dataset, gtruth):
        if iris_type == 'Iris-setosa':
            setosa.receive(attributes)
        elif iris_type == 'Iris-versicolor':
            versicolor.receive(attributes)
        else:
            virginica.receive(attributes)

    plt.figure(1)
    #plt.plot(setosa.slenghts, setosa.plenghts, 'xb', label="Iris-setosa")
    plt.plot(versicolor.slenghts, versicolor.plenghts, '.r', label="Iris-versicolor")
    plt.plot(virginica.slenghts, virginica.plenghts, 'og', label="Iris-virginica")
    plt.xlabel('sepal lenghts')
    plt.ylabel('petal lengths')
    plt.legend(loc='upper left')
    plt.show()
