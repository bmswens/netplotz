__all__ = [
    'create_edge',
    'create_edges',
    'create_data',
    'plot'
]

# for creating visualizations
import plotly.graph_objs as go

# for converting nx.Graph objects into plotly
import networkx as nx


def create_edge(a, b, **kwargs):

    x = [a[0], b[0]]
    y = [a[1], b[1]]

    edge = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        showlegend=False,
        **kwargs
    )

    return edge


def create_edges(connections, **kwargs):

    edges = []

    for connection in connections:

        edge = create_edge(connection[0], connection[1], **kwargs)
        edges.append(edge)

    return edges


def create_data(graph, scatter_layout=None, **kwargs):

    layout_options = {
        'bipartite_layout': nx.bipartite_layout,
        'circular_layout': nx.circular_layout,
        'kamada_kawai_layout': nx.kamada_kawai_layout,
        'shell_layout': nx.shell_layout,
        'spring_layout': nx.spring_layout,
        'spectral_layout': nx.spectral_layout
    }

    # use their preferred layout, defaults to random
    if scatter_layout in layout_options:
        positions = layout_options[scatter_layout](graph)
    else:
        positions = nx.random_layout(graph)

    # get the options for scatter plot if passed
    scatter_options = kwargs.get('scatter_options')

    # default scatter_options
    if not scatter_options:
        scatter_options = {
            'name': 'nodes',
            'text': list(graph.nodes),
            'marker': {
                'symbol': 'circle',
                'size': 18,
                'color': '#d4e3ff',
                'line': {
                    'color': '#000000',
                    'width': 1
                },
                'opacity': 1
            },
        }

    # get the positions of the nodes
    scatter_x = []
    scatter_y = []
    for node in graph.nodes:
        scatter_x.append(positions[node][0])
        scatter_y.append(positions[node][1])

    scatter = go.Scatter(
        x=scatter_x,
        y=scatter_y,
        mode='markers',
        **scatter_options
    )

    # get the edges
    edges = []
    for edge in graph.edges:
        node1 = positions[edge[0]]
        node2 = positions[edge[1]]
        edges.append([node1, node2])

    # get the options for edge plots
    edge_options = kwargs.get('edge_options')

    # default edge_options
    if not edge_options:
        edge_options = {
            'hoverinfo': 'none',
            'line': {
                'color': '#8b8b7a',
                'width': 0.75
            }
        }

    data = create_edges(edges, **edge_options) + [scatter]

    return data


def plot(graph, layout=None, **kwargs):

    data = create_data(graph, **kwargs)

    if not layout:

        noaxis = {
            'showline': False,
            'zeroline': False,
            'showgrid': False,
            'showticklabels': False
        }

        layout = go.Layout(
            xaxis=noaxis,
            yaxis=noaxis,
            hovermode='closest'
        )

    figure = go.Figure(data, layout)

    return figure
