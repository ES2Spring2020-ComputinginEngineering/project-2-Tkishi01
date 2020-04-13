#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose,hemoglobin):
    normglucose = []
    normhemoglobin = []
    for i in glucose:
        norm = (i-70)/(490-70)
        normglucose.append(norm)
    for i in hemoglobin:
        norm = (i-3.1)/(17.8-3.1)
        normhemoglobin.append(norm)
    return np.array(normglucose), np.array(normhemoglobin)

def selectCentroids(k):
    centroidPoints= []
    for i in range(k):
        glucose = (random.uniform(0,1))
        hemoglobin = (random.uniform(0,1))
        centroidPoints.append([glucose,hemoglobin])
    return  np.array(centroidPoints)

def calculateDistanceArray(centroidGlucose,centroidHemoglobin, glucose, hemoglobin):
    a = (centroidHemoglobin - glucose)
    b = (centroidGlucose - hemoglobin)
    distance = np.sqrt((a**2+b**2))
    return  distance

def createDistanceArray(k, centroidPoints, glucose, hemoglobin):
    distanceList=calculateDistanceArray(centroidPoints[0][0], centroidPoints[0][1],glucose,hemoglobin)
    for i in range(1,k):
        distance = calculateDistanceArray(centroidPoints[i][0], centroidPoints[i][1],glucose,hemoglobin)
        distanceList = np.column_stack((distanceList,distance))
    return distanceList

def assignClusters(k, centroidPoints, glucose, hemoglobin):
    classificationList = []
    distanceList = createDistanceArray(k,centroidPoints, glucose, hemoglobin)
    for i in distanceList:
        clusterClass=np.argmin(i)
        classificationList.append(clusterClass)
    return np.array(classificationList)

def updateCentroids(glucose, hemoglobin, classificationList, k):
    updatedCentroids = np.empty((k,2))
    for i in range(0,k):
        glucoseCentroid = np.mean(glucose[classificationList==i])
        hemoglobinCentroid = np.mean(hemoglobin[classificationList==i]) 
        #print(glucoseCentroid,hemoglobinCentroid)
        updatedCentroids[i]= np.append(hemoglobinCentroid,glucoseCentroid)
    return updatedCentroids

def graphingKMeans(glucose, hemoglobin, centroidPoints, classificationList):
    plt.figure()
    for i in range(classificationList.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[classificationList==i],glucose[classificationList==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroidPoints[i, 0], centroidPoints[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend(loc='upper center', bbox_to_anchor=(1.2, 0.8), shadow=True, ncol=1)
    plt.show()

######


        