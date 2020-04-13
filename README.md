This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Taylor Kishinami

NearestNeighborClassification.py:

This code does not require user input to run. It will generate a graph of glucose plotted over hemoglobin. Both data sets are normalized. The data is color coded to indicate the diagnosis, as described in the legend. The test case (randomly generated) will also be plotted on the graph, represented by a star. It will be color coded depending on the outcome of the nearest neighbor test. The outcomes of both the nearest neighbor and k-nearest neighbor tests are printed and labelled below the graph.

KMeansClustering_functions.py:

This code does not need to run, as it simply contains the functions necessary to perform the k-means clustering simulation. 

KMeansClustering_driver.py:

This code can be manipulated by altering the variable k, which is the number of centroids generated at the beginning of the simulation. For 1-3 centroids, I set the simulation to go through 10 iterations, which allows the data to update until changes in the centroids in each iteration are numerically insignificant. This code graphs the data as assigned to initially random centroids, and prints "working..." each iteration until it graphs the final, mean-adjusted centroids and their clusters. It then prints the coordinates of the final centroids and the percentage of each component of the confusion matrix. In order to gather the data present in the results section of my project report, only the value of k must be altered for varying cluster amounts.  