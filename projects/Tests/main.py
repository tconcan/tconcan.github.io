import pandas as pd
import igraph as ig
import numpy as np 
import networkx as nx
import plotly.graph_objects as go

edges = pd.read_csv("./data/topmusic.txt", sep=", ", header=None)
g = ig.Graph.TupleList(edges.values.tolist())
G = g.to_networkx()
mapping = {i: name for i, name in enumerate(g.vs["name"])}
nx.relabel_nodes(G, mapping, copy=False)

layout_2D = nx.spring_layout(G, seed=41, iterations=200) 
x2 = [pos[0] for pos in layout_2D.values()]
y2 = [pos[1] for pos in layout_2D.values()]

layout_3D = nx.spring_layout(G, seed=41, dim=3)
x3 = [pos[0] for pos in layout_3D.values()]
y3 = [pos[1] for pos in layout_3D.values()]
z3 = [pos[2] for pos in layout_3D.values()]

node_sizes = [(np.log(G.degree(node)) + 1) * 10 for node in G.nodes()]
node_trace_2D = [go.Scatter(x=x2, y=y2, mode='markers+text',
                           text=list(G.nodes()), textposition='top center',
                           marker=dict(color='royalblue', size=node_sizes, 
                                       line=dict(color='black', width=0.5)),
                           hoverinfo='text', hovertext=list(G.nodes()))]

node_trace_3D = [go.Scatter3d(x=x3, y=y3, z=z3, mode='markers+text',
                              text=list(G.nodes()), textposition='top center',
                              marker=dict(color='royalblue', opacity=0.95,
                                          size=node_sizes, line=dict(color='black',
                                                                     width=0.5)),
                              hoverinfo='text', hovertext=list(G.nodes()))]

edge_x2, edge_y2 = [], []
for edge in G.edges():
    x0, y0 = layout_2D[edge[0]]
    x1, y1 = layout_2D[edge[1]]
    edge_x2.extend([x0, x1, None])
    edge_y2.extend([y0, y1, None])
edge_trace_2D = [go.Scatter(x=edge_x2, y=edge_y2, mode='lines',
                            line=dict(width=0.2, color='black'), hoverinfo='none')]

edge_x3, edge_y3, edge_z3 = [], [], []
for edge in G.edges():
    x0, y0, z0 = layout_3D[edge[0]]
    x1, y1, z1 = layout_3D[edge[1]]
    edge_x3.extend([x0, x1, None])
    edge_y3.extend([y0, y1, None])
    edge_z3.extend([z0, z1, None])
edge_trace_3D = [go.Scatter3d(x=edge_x3, y=edge_y3, z=edge_z3, mode='lines',
                            line=dict(width=0.5, color='black'), hoverinfo='none')]

fig_2D = go.Figure(data=edge_trace_2D + node_trace_2D)
fig_2D.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False),
                    showlegend=False, paper_bgcolor='white', plot_bgcolor='white')

fig_3D = go.Figure(data=edge_trace_3D + node_trace_3D)
fig_3D.update_layout(scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False),
                            zaxis=dict(visible=False), aspectmode='manual',
                            aspectratio=dict(x=1, y=1, z=1)), showlegend=False)

fig_2D.write_image(f"./plots/2D.png", height=6000, width=6000, scale=1.0)
fig_3D.write_html(f"./plots/3D.html")








