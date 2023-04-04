import matplotlib.pyplot as plt


def create_graph(dataset, fitted_model):
    plt.scatter(x=dataset['Ankle'], y=dataset['Neck'])
    mymodel = fitted_model.params[1] * dataset['Ankle'] + fitted_model.params[0]
    plt.plot(dataset['Ankle'], mymodel)
    plt.show()