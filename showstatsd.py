import numpy as np
import xlrd
import time
import pandas as pd
import matplotlib.pyplot as plt
from spreadsheetsSD import *
import gspread
import matplotlib.pyplot as plt

values = dataframee()
df = pd.DataFrame(values[0:],columns=values[0])

plt.plot(df['Start Time'],df['Measure of Violations'],linewidth=4)


plt.xlabel('Time')
plt.ylabel('Measure of Violations')
plt.title('Social Distance Violators')

plt.show()
