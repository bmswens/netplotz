# netplotz

Utilize plotly to visualize networkx graphs.

## Getting Started

### Prerequisites

Package comes with a requirments.txt file.
Main requirements are:

plotly

networkx

numpy

scipy

```
pip install -r requirements.txt
```

### Installing

If you want to import it and use it in your own scripts you can install it with

```
pip install git+https://github.com/bmswens/netplotz
```

## Use

In your own code:
```
import networkx
import plotly.offline as offline
import netplotz as netp

graph = networkx.complete_graph(10)
figure = netp.plot(graph, 'kamada_kawai_layout')

offline.plot(figure)
```

## Authors

* **Brandon Swenson** - *Initial work* - [bmswens](https://github.com/bmswens)

See also the list of [contributors](https://github.com/bmswens/netplotz/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
