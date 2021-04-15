#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
df = pd.read_csv('amc.csv',index_col=[0])


# In[21]:


import plotly.express as px
from plotly.subplots import make_subplots

fig = px.line(df, x="Time", y="Price", title='AMC Data')
fig2 = px.line(df, x="Time", y="GEX", title='AMC DATA')

fig2.update_traces(yaxis="y2")

option= [[{"secondary_y": True}]]

subfig = make_subplots(specs=[[{"secondary_y": True}]])

# create two independent figures with px.line each containing data from multiple columns

subfig.add_traces(fig.data + fig2.data)

subfig.layout.xaxis.title="Time"
subfig.layout.yaxis.title="Price"
#subfig.layout.yaxis2.type="log"
subfig.layout.yaxis2.title="GEX"

# recoloring is necessary otherwise lines from fig und fig2 would share each color
# e.g. Linear-, Log- = blue; Linear+, Log+ = red... we don't want this
subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
subfig.show()
#fig.show()


# In[ ]:


#X axis should be time.
#Left y axis is Price
#right y axis is GEX.


# In[3]:





# In[4]:





# In[ ]:




