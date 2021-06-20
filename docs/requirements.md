# Requirement specifications
This documents specifies the high level requirements of the implemented program and the algorithms contained in that program.

- Study program: Bachelor programme in computer science (tietojenkäsittelytieteen kandidaattiohjelma) Helsingin yliopisto
- Project language: English (mutta tekijä ymmärtää kyllä suomeakin)

### Algorithms
The purpose of the program is to compare different path finding algorithms on two dimensional map. The project assumes that maps are uniform cost maps (no down or uphills etc.) with travelable surface and walls. The program will compare *Dijkstra's*, *A** and Jump Point Search algortihms. 

### Inputs
The program will utilize the maps available in the Moving AI lab. The program will scrape the website and provide full list of (256x256 px) maps for user to select. This project scope does not allow configurability of the input (i.e. changing the scrapable web endpoint). However, it's relatively easy to adjust the parts in the source code that refer to the maps and algorithms may be run with any two dimensional map that does not violate the uniform cost assumption.

User may select any of the available maps. The program will unzip the file and parse the map. For the parsed map, the program will perform the algorithmic comparison.

### User interface
Algorithm comparison is performed through a browser-based graphical user interface which allows user to select the input map, start and end coordinates and the algoriths for comparison.

The user interface, after running the algorithms, then displays the user the found path and the performance results of the selected algorithms.

### Time and space complexity of the algorithms
**Dijkstra**
- Time complexity: O((V + E log (V))
- Space complexity: O(V)

**A***
- Time complexity: O(E)
- Space complexity: O(V)

**JPS**
- Time complexity: O(E)
- Space complexity: O(V)

### Data structures
The selected algorithms are implemented using priority queue. The project implements a custom minimum heap data structure that allows the required features of the priority queue. This will replace python standard library module `heapq`.

The project will not replace any other data structures offered by python standard libraries. Of those the most noteworthy are `dict` and `set` structures. Also, the modules offering front end features and utilities use several external features (such as web scraping). 




