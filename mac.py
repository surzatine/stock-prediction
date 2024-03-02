import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols)
print(df.head())
df.head().plot()
plt.show()
