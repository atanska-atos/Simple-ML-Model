# required libraries
import pandas as pd

import prepare_data
from prepare_data import *
from model import *
from graph import *

dataset = pd.read_csv("bodyfat.csv")
prepare_data.print_data(dataset)