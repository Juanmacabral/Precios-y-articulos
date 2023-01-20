#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import ExcelWriter
import datetime
import pickle
import os


# In[ ]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_pickle")


# In[2]:


# Cargar la variable desde el archivo
with open("articulos.pickle", "rb") as f:
    articulos = pickle.load(f)

# Cargar la variable precios_general desde el archivo binario
with open("precios_general.pickle", "rb") as f:
    precios_general = pickle.load(f)

# Cargar la variable precios_jean desde el archivo binario
with open("precios_jeans.pickle", "rb") as f:
    precios_jeans = pickle.load(f)
    
# Cargar la variable precios_jean desde el archivo binario
with open("filtro.pickle", "rb") as f:
    filtro = pickle.load(f)



# In[ ]:


os.chdir("C:/Users/Juan M Cabral/Desktop/Pycharm/Precios/archivos_py")


# In[3]:


articulos_jeans = articulos.loc[articulos['grupos de telas'].isin(filtro)] #filtro por jeans
articulos_general = articulos.loc[~articulos['grupos de telas'].isin(filtro)]#filtro por todo lo que NO sea jeans


# In[4]:


jeans_final = articulos_jeans.merge(precios_jeans) #junto 2 planillas
articulos_general_final = articulos_general.merge(precios_general) ##junto 2 planillas


# In[6]:


#reacomodo las columnas, en ambos casos
jeans_final = jeans_final.reindex(columns=['producto', 'descripcion', 'diseñadora', 'tipo de prenda', 'origen', 
'segmento / linea','grupos de telas','color', 'precio', 'fecha','produccion','tmp a central', 'central','transito',
'stock locales', 'total'])
articulos_general_final = articulos_general_final.reindex(columns=['producto', 'descripcion', 'diseñadora', 'tipo de prenda',
'origen','segmento / linea', 'grupos de telas', 'precio', 'fecha','produccion','tmp a central', 'central', 
'transito', 'stock locales', 'total'])

#modifico type, de object a int
jeans_final = jeans_final.astype({'precio':"int", 'produccion':"int", 'tmp a central':"int",
                                  'central':"int", 'transito':"int", 'stock locales':"int", 'total':"int"})

articulos_general_final = articulos_general_final.astype(
                                 {'precio':"int", 'produccion':"int", 'tmp a central':"int",
                                  'central':"int", 'transito':"int", 'stock locales':"int", 'total':"int"})


# In[8]:


#exporto a un excel ambas tablas
with pd.ExcelWriter(r'\\NasConbra011\Administra\Reportes\precios.xlsx') as writer:
    articulos_general_final.to_excel(writer, sheet_name='Articulos general', index=False)
    jeans_final.to_excel(writer, sheet_name='Jeans', index=False)


