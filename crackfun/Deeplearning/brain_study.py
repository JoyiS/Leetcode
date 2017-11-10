import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *
root = tk.Tk()
root.withdraw()
import os
import operator
from pandas.tools import plotting

if __name__ == "__main__":
    inputfile = filedialog.askopenfile()
    data = pd.read_csv(inputfile, sep=';', na_values=".")

    pd.DataFrame.describe(data)

    viqmean = data['VIQ'].mean
    data.groupby('Gender').size()
    genderD = data.groupby('Gender')
    genderD['VIQ'].mean()

    plotting.scatter_matrix(data.loc[data['Gender'] == 'Female'][['Weight', 'Height', 'MRI_Count']])
    plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])