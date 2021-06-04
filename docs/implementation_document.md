# Implementation document

### Purpose
The purpose of the application is to compare different pathfinding algorithms on different map and coordinate inputs. Inputs can be controlled by the user via the graphical user interface

### Architecture
The application conforms to a three layered architecture. Front end is based on Jinja 2 framework with custom JavaScript event triggers and canvas rendering and is contained in `templates` module. 

The controller is based on Flask framework and contains `views.py` to control the user inputs and `forms.py` to control the input forms on front end templates. 

The the application logic is divided in three modules `utilities` to provide generic web scraping and file processing utilities, `algorithms` which contain the implemented algorithms, and `data_structures` which contain the self-implemented data structures.

### Time and space complexity

* Time complexity
Dijkstra = O((E+V)log(V)) ??
A* = O((E+V)log(V)) ??
JPS = O((E+V)log(V)) ??

* Space complexity
Dijkstra = O(E) ??
A* = O(E) ??
JPS = O(E) ??

### Performance analysis

### Sources
- [A* search algorithm, Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Jump Point Search, Shortest path](https://harablog.wordpress.com/2011/09/07/jump-point-search/)
- [A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial, Youtube](https://www.youtube.com/watch?v=JtiK0DOeI4A)
- [Tirakirja, Antti Laaksonen](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
- [Min Heap in Python](https://www.geeksforgeeks.org/min-heap-in-python/)
- [Jump Point Search: Fast A* Pathfinding for Uniform Cost Grids](https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/)
- [2D Pathfinding Benchmarks](https://movingai.com/benchmarks/grids.html)
- [Bootstrap](https://getbootstrap.com/docs/5.0/examples/)