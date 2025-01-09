#!pip install ecdsa
#!pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
from ecdsa import SECP256k1
import sympy
import numpy as np

SatoshiMaxWalletCount = 1000
df = pd.read_csv('Satoshi.csv', delimiter=';', header=0)
SatoshiPX = df.head(SatoshiMaxWalletCount)['X'].apply(lambda x: sympy.Integer(x))
SatoshiPY = df.head(SatoshiMaxWalletCount)['Y'].apply(lambda x: sympy.Integer(x))
SatoshiWallet = df.head(SatoshiMaxWalletCount)['Wallet']

plt.figure(figsize=(16, 12))
plt.plot(SatoshiPX, SatoshiPY, marker='o', linestyle='none', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.tick_params(axis='x', which='both', bottom=True, top=True, labelbottom=True)
plt.tick_params(axis='y', which='both', left=True, right=True, labelleft=True)
plt.title('Satoshi Wallet Public Keys Points')
plt.grid(True)


'''
for i in range(SatoshiMaxWalletCount):
    plt.annotate(str(i+1),  # Sıra numarasını metin olarak ekle; str(i+1) veya SatoshiWallet.iloc[i][:5]
                 xy=(SatoshiPX.iloc[i], SatoshiPY.iloc[i]), xytext=(SatoshiPX.iloc[i], SatoshiPY.iloc[i]), 
                 color='black', 
                 fontsize=12,
                 )
'''

plt.show()

