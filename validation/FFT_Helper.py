import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy

def plot_FFT(df):
    fft = abs(pd.Series(np.fft.rfft(df - df.mean()),
    index = np.fft.rfftfreq(len(df), d = 1./8760))**2)
    fft.plot()
    plt.xlim(0, 768)
    plt.xlabel("1/a")
    plt.grid(True)
