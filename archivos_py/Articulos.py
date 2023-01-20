#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import openpyxl
import pickle
import os


# In[2]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_excel")


# In[3]:


articulos = pd.read_excel("Stk_Dps_Vtas_Loc_FabTem.xls")
#subo el listado de articulos, donde se detalla el stock (no incluye color)


# In[4]:


articulos = articulos.iloc[1:-1, :] #Elimino primera y ultima fila
articulos = articulos.rename(columns=articulos.iloc[0]).drop(articulos.index[0]) #Primera fila pasa a ser header 
articulos.columns = map(str.lower, articulos.columns) #Lowercase a los headers de columnas
lista_columnas = ['pendiente corte', 'cortado', 'taller', 'fabricacion'] # Agrupo columnas a sumar en una lista
articulos['produccion'] = articulos[lista_columnas].sum(axis=1).astype(int) #Sumo columnas anidadas en lista_columnas
articulos = articulos.drop(columns=['temporada', 'año', 'precio','pendiente corte',
                                    'cortado', 'taller', 'fabricacion','venta', '%']) #Elimino columnas que no sirven
articulos = articulos.apply(lambda x: x.astype(str).str.strip() if x.dtype == "object" else x) 
# Elimino espacios en blanco del dataset
filtro = articulos.sort_values(by='grupos de telas')['grupos de telas'].unique()
filtro = [x for x in filtro if "JEAN" in x or "JEANS" in x ]
articulos = articulos.loc[articulos['total'].astype(int) > 100] #filtro columna total por mayores a 100


# In[ ]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_pickle")


# In[10]:


# Serializar la variable articulos y almacenarla en un archivo binario
with open("articulos.pickle", "wb") as f:
    pickle.dump(articulos, f)

# Serializar la variable articulos y almacenarla en un archivo binario
with open("filtro.pickle", "wb") as f:
    pickle.dump(filtro, f)
    


# In[ ]:




