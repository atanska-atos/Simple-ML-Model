import graphing
from train_model import *


def create_graph(dataset, fitted_model):
    graphing.scatter_2D(dataset, label_x="harness_size",
                        label_y="boot_size",
                        trendline=lambda x: fitted_model.params[1] * x + fitted_model.params[0]
                        )
