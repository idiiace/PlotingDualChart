#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

def return_pandas(File):
    df = pd.read_csv(File,index_col=[0])
    return df

def return_sub_plots(df):
    first = px.line(df, x="Time", y="Price", title='Data')
    second = px.line(df, x="Time", y="GEX", title='DATA')
    second.update_traces(yaxis="y2")
    return [first,second]

def return_merged_plots(first,second):

    option= [[{"secondary_y": True}]]

    main_plot = make_subplots(specs=option)


    main_plot.add_traces(first.data + second.data)
    #titles
    main_plot.layout.xaxis.title="Time"
    main_plot.layout.yaxis.title="Price"
    main_plot.layout.yaxis2.title="GEX"

    #coloring
    main_plot.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    return main_plot

def main(f):
    df=return_pandas(f)
    first,second = return_sub_plots(df)
    figure = return_merged_plots(first,second)
    return figure

    
f=main('amc.csv')
f.show()
