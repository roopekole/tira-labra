# Implementation document

### Purpose
The purpose of the application is to compare different pathfinding algorithms on different map and coordinate inputs. Inputs can be controlled by the user via the graphical user interface

### Architecture
The application conforms to a three layered architecture. Front end is based on Jinja 2 framework with custom JavaScript event triggers and canvas rendering and is contained in `templates` module. 

The controller is based on Flask framework and contains `views.py` to control the user inputs and `forms.py` to control the input forms on front end templates. 

The the application logic is divided in three modules `utilities` to provide generic web scraping and file processing utilities, `algorithms` which contain the implemented algorithms, and `data_structures` which contain the self-implemented priority queue data structure.

### Time and space complexity
V represents the number of vertices in the graph and E represents the number of edges in the graph. Time and auxiliary space complexities are given as worst-case complexities.

**Time complexity**

Dijkstra = O((V + E log (V))

A* = O(E)

JPS = O(E)

Binary Heap = O(log V)

**Space complexity**

Dijkstra = O(V)

A* = O(V)

JPS = O(V)

Binary Heap = O(V)


### Performance analysis

### Known issues and development ideas
Knowns issues and development ideas are listed in the [issues](https://github.com/roopekole/tira-labra/issues) of the repository.

The major known issues and development ideas are:
* Bug: More intuitive information if end cannot be reached from the start
    * Inform the user why route was not found
    * Eliminate the internal error if start / end completely surrounded by an obstacle
* Parametrizable input map list selection


### Sources
- [A* search algorithm, Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Jump Point Search, Shortest path](https://harablog.wordpress.com/2011/09/07/jump-point-search/)
- [A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial, Youtube](https://www.youtube.com/watch?v=JtiK0DOeI4A)
- [Tirakirja, Antti Laaksonen](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
- [Min Heap in Python](https://www.geeksforgeeks.org/min-heap-in-python/)
- [Jump Point Search: Fast A* Pathfinding for Uniform Cost Grids](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)
- [2D Pathfinding Benchmarks](https://movingai.com/benchmarks/grids.html)
- [Bootstrap](https://getbootstrap.com/docs/5.0/examples/)