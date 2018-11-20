#!/usr/bin/env python3

import json
import tasks
import plotly as py
import plotly.graph_objs as go

def plot():
    plotDict = json.loads(tasks.counts())
    labels = list(plotDict.keys())
    values = list(plotDict.values())

    data = [go.Bar(
            x=labels,
            y=values,
            text=values,
            textposition = 'outside',
            opacity=0.8,
            marker=dict(
                color='rgb(124,238,102)',
                )
    )]

    layout = go.Layout(
        title='Swedish Pronoun Counts - Twitter Data',
        font=dict(color = "black", size = 10),
        )

    figure = go.Figure(data=data, layout=layout)
    py.offline.plot(figure, filename='Swedish PronounCounts.html')

if __name__ == '__main__':
    plot()
