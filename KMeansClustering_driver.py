#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np

glucose, hemoglobin, classification = kmc.openckdfile()
glucose, hemoglobin = kmc.normalizeData(glucose, hemoglobin)  
k=2
centroidPoints = kmc.selectCentroids(k) 
classificationList = kmc.assignClusters(k, centroidPoints,glucose,hemoglobin)
updatedCentroids = kmc.updateCentroids(glucose,hemoglobin,classificationList,k)
kmc.graphingKMeans(glucose,hemoglobin,centroidPoints,classificationList)
iterations = 0
while iterations < 10:
    classificationList = kmc.assignClusters(k, centroidPoints, glucose, hemoglobin)
    centroidPoints = kmc.updateCentroids(glucose, hemoglobin, classificationList, k)
    print("working...")
    iterations = iterations +1
kmc.graphingKMeans(glucose, hemoglobin, centroidPoints, classificationList)
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
truePositives = tP/ckdCluster*100
falsePositives = fP/ckdCluster*100
trueNegatives = tN/nonckdCluster*100
falseNegatives = fN/nonckdCluster*100
print("True Positives:" + str(truePositives))
print("False Positives:" + str(falsePositives))
print("True Negatives:" + str(trueNegatives))
print("False Negatives:" + str(falseNegatives))