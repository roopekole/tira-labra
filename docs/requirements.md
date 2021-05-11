# Requirement specifications
This documents specifies the high level requirements of the implemented program and the algorithms contained in that program.

- Study program: Bachelor programme in computer science (tietojenk‰sittelytieteen kandidaattiohjelma) Helsingin yliopisto
- Project language: English (mutta tekij‰ ymm‰rt‰‰ kyll‰ suomeakin)

### Algorithms
The purpose of the program is to compare two (or more) path finding algorithms. I will implement Jump Point Search (JPS) and IDA* and potentially one of the traditional algorithms (such as A*). I will compare the performance and space complexity.

### Inputs
The program will utilize the maps available in the Moving AI lab. The program will scrape the website and provide full list of (smaller scale) maps for user to select. The initial scope will cover city maps. Extended coverage could potentially cover any char based maps as long as there are no conflicts between the encoding of paths and barriers.

The purpose is that user may select any of the available maps. The program will unzip the file and parse the map. For the parsed map, the program will perform the algorithmic comparison.

*It is not determined yet, how the user will select start and end nodes.*

### Time and space complexity
**IDA**
- Time complexity: O(b^d)
- Space complexity: O(d)
where b is the branching factor and d is the depth of the first solution (source: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search#Time_complexity)

**JPS**
- Time complexity: ?
- Space complexity: ?

Will be appended as additional algorithms are added

### Data structures
Will be appended later

### User interface
The program will be used through a browser based graphical user interface. The user interface allows the user to determine the required input parameters (map and coordinates) intuitively.




