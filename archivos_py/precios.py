#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import pickle
import datetime
import os


# In[5]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_excel")


# In[6]:


precios = pd.read_excel('PRECIOS PUBLICO.xlsx') #subo el listado de precios por barra y fecha


# In[3]:


precios.columns = map(str.lower, precios.columns) #Lowercase a los headers de columnas
precios.drop(columns=['unnamed: 6', 'unnamed: 7','talle'],inplace=True) # Elimino columnas que no sirven
precios.dropna(inplace=True) #drop de Nan values
precios['precio'] = precios['precio'].round().astype(int)


# In[4]:


precios_general = precios[precios['fecha'] > '2022-01-01']
precios_general = precios_general.sort_values(['precio', 'fecha'], ascending=[False, False])
precios_general = precios_general.groupby('producto').first()
precios_general.drop(columns='color', inplace=True)
precios_general = precios_general.reset_index()


# In[5]:


precios_jeans = precios[(precios['fecha'] > '2022-01-01')] #filtro por fecha 
precios_jeans = precios_jeans.groupby(['producto','color']).apply(lambda x: x.loc[x['precio'].idxmax()]) 
#Agrupo por producto y color, buscando el precio mas alto por articulo
precios_jeans = precios_jeans.drop(columns=['producto']) #reacomodo tabla
precios_jeans = precios_jeans.reset_index(drop=True) #reacomodo la tabla


# In[ ]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_pickle")


# In[ ]:


# Serializar la variable precios_general y almacenarla en un archivo binario
with open("precios_general.pickle", "wb") as f:
    pickle.dump(precios_general, f)

# Serializar la variable precios_jean y almacenarla en un archivo binario    
with open("precios_jeans.pickle", "wb") as f:
    pickle.dump(precios_jeans, f)

