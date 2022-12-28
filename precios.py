#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import openpyxl
import pickle


# In[11]:


precios = pd.read_excel('PRECIOS PUBLICO.xlsx') #subo el listado de precios por barra y fecha


# In[12]:


precios.columns = map(str.lower, precios.columns) #Lowercase a los headers de columnas
precios.drop(columns=['unnamed: 6', 'unnamed: 7','talle'],inplace=True) # Elimino columnas que no sirven
precios.dropna(inplace=True) #drop de Nan values
precios['precio'] = precios['precio'].astype(int) #convierto la columna precio en INT
precios['fecha'] = precios['fecha'].dt.strftime("%d/%m/%Y")


# In[13]:


precios_general = precios.drop(columns=['color']) #para esta tabla el color no hace falta. Drop.
precios_general = precios_general.groupby('producto').apply(lambda x: x.loc[x.precio.idxmax()])
#Agrupo por producto, buscando el precio mas alto por articulo
precios_general.drop(columns=['producto'],inplace=True) #reacomodo la tabla
precios_general = precios_general.reset_index() #reacomodo la tabla
precios_general = precios_general[(precios_general['fecha'] > '2022-08-01')] #filtro por fecha 


# In[14]:


precios_jeans = precios.groupby(['producto','color']).apply(lambda x: x.loc[x.precio.idxmax()]) 
#Agrupo por producto y color, buscando el precio mas alto por articulo
precios_jeans = precios_jeans.drop(columns=['producto','color']) #reacomodo tabla
precios_jeans = precios_jeans.reset_index() #reacomodo la tabla
precios_jeans = precios_jeans[(precios_jeans['fecha'] > '2022-01-01')] #filtro por fecha 


# In[ ]:


# Serializar la variable precios_general y almacenarla en un archivo binario
with open("precios_general.pickle", "wb") as f:
    pickle.dump(precios_general, f)

# Serializar la variable precios_jean y almacenarla en un archivo binario
with open("precios_jeans.pickle", "wb") as f:
    pickle.dump(precios_jeans, f)

