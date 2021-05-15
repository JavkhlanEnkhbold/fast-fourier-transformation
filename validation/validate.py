from validation import FFT_Helper
import pandas as pd 
import matplotlib.pyplot as plt 


de = pd.read_csv('/data/de_data.csv', parse_dates=True, index_col=0)

fft = FFT_Helper.plot_FFT(de["wind"])

