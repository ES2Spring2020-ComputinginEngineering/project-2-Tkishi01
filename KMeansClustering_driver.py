##################
#ES2 Project 2
#NearestNeighborClassification.py
#NAME: Taylor Kishinami
#HOURS NEEDED: 1
#I worked alone on this part.
#################
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

k=2
glucose, hemoglobin, classification = kmc.openckdfile()
glucose, hemoglobin = kmc.normalizeData(glucose, hemoglobin)  
centroidPoints = kmc.selectCentroids(k) 
classificationList = kmc.assignClusters(k, centroidPoints,glucose,hemoglobin)
updatedCentroids = kmc.updateCentroids(glucose,hemoglobin,classificationList,k)
#The code above sets variables used later, including the number of centroids. 

kmc.graphingKMeans(glucose,hemoglobin,centroidPoints,classificationList)
#This graphs the initial assignment of the data using the initial random centroids.

iterations = 0
while iterations < 10:
    #The simulation iterates 10 times.
    classificationList = kmc.assignClusters(k, centroidPoints, glucose, hemoglobin)
    centroidPoints = kmc.updateCentroids(glucose, hemoglobin, classificationList, k)
    print("working...")
    iterations = iterations +1
kmc.graphingKMeans(glucose, hemoglobin, centroidPoints, classificationList)
#This is the final cluster assignment. Next, the code prints the final centroid points.
print("Final Centroid Points:")
print(centroidPoints)
tP = 0
fP = 0
tN = 0
fN = 0
ckdCluster = 0
nonckdCluster = 0
if np.mean(classificationList) >0.5:
    hasckd = 1
    nockd = 0
else: 
    hasckd = 0
    nockd = 1
    #This determines which centroid represents CKD patients and which does not.
for i in range(0,len(classification)):
    if classification[i] == 0:
        nonckdCluster = nonckdCluster+1
        if classificationList[i] == nockd:
            fN = fN+1
        if classificationList[i] == hasckd:
            tN = tN+1
    if classification[i] == 1:
        ckdCluster = ckdCluster+1
        if classificationList[i] == nockd:
            tP=tP+1
        if classificationList[i] == hasckd:
            fP = fP+1
            #This calculates how many points fall into each category.
truePositives = tP/ckdCluster*100
falsePositives = fP/ckdCluster*100
trueNegatives = tN/nonckdCluster*100
falseNegatives = fN/nonckdCluster*100
print("True Positives:" + str(truePositives))
print("False Positives:" + str(falsePositives))
print("True Negatives:" + str(trueNegatives))
print("False Negatives:" + str(falseNegatives))