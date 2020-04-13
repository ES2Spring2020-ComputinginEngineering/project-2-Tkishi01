##################
#ES2 Project 2
#NearestNeighborClassification.py
#NAME: Taylor Kishinami
#HOURS NEEDED: 5
#I worked alone on this part.
#################
import numpy as np
import matplotlib.pyplot as plt
import random

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification
#openckdfile takes no arguments.
#It reads the data from ckd.csv and formats it into arrays.
#It returns three arrays, glucose, hemoglobin, and classification.
    
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
#normalizeData takes two arguments: glucose and hemoglobin. Both are data arrays.
#It normalizes the glucose and hemoglobin values so that all data values are on a scale of 0 to 1. 
#It returns the two normalized glucose and hemoglobin arrays

def selectCentroids(k):
    centroidPoints= []
    for i in range(k):
        glucose = (random.uniform(0,1))
        hemoglobin = (random.uniform(0,1))
        centroidPoints.append([glucose,hemoglobin])
    return  np.array(centroidPoints)
#selectCentroids takes one argument, k number of clusters.
#It generates k amount of random values for glucose and hemoglobin to create k centroid points. 
#It returns an array of the centroid values.

def calculateDistanceArray(centroidHemoglobin,centroidGlucose, glucose, hemoglobin):
    a = (centroidGlucose - glucose)
    b = (centroidHemoglobin - hemoglobin)
    distance = np.sqrt((a**2+b**2))
    return  distance
#calculateDistanceArray takes four arguments: the randomly generated point and the arrays of glucose and hemoglobin.
#It calculates the distance from the generated point to every point in the data set.
#It returns an array containing these distances. 

def createDistanceArray(k, centroidPoints, glucose, hemoglobin):
    distanceList=calculateDistanceArray(centroidPoints[0][0], centroidPoints[0][1],glucose,hemoglobin)
    for i in range(1,k):
        distance = calculateDistanceArray(centroidPoints[i][0], centroidPoints[i][1],glucose,hemoglobin)
        distanceList = np.column_stack((distanceList,distance))
    return distanceList
#createDistanceArray takes 4 arguments: k centroids, centroidPoints, and the glucose and hemoglobin data arrays.
#It uses calculateDistanceArray to create an array for each centroid and stacks them together.
#It returns the 2D array of distances arranged by centroid per column.

def assignClusters(k, centroidPoints, glucose, hemoglobin):
    classificationList = []
    distanceList = createDistanceArray(k,centroidPoints, glucose, hemoglobin)
    for i in distanceList:
        clusterClass=np.argmin(i)
        classificationList.append(clusterClass)
    return np.array(classificationList)
#assignClusters takes 4 arguments: k centroids, centroidPoints, and the glucose and hemoglobin data arrays.
#It finds the minimum distance centroid for each point and appends the class of the centroid into a list.
#It returns an array of the classifications(aka nearest centroids) of each point.

def updateCentroids(glucose, hemoglobin, classificationList, k):
    updatedCentroids = np.empty((k,2))
    for i in range(0,k):
        glucoseCentroid = np.mean(glucose[classificationList==i])
        hemoglobinCentroid = np.mean(hemoglobin[classificationList==i]) 
        updatedCentroids[i]= np.append(hemoglobinCentroid,glucoseCentroid)
    return updatedCentroids
#updateCentroids takes 4 arguments: the data arrays glucose and hemoglobin, the classificationList, and k centroids.
#It creates new centroids by taking the mean coordinates of each cluster, making them closer to the center of the cluster.
#It returns the new centroids.
    
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
#graphingKMeans takes 4 arguments: the glucose and hemoglobin data arrays, centroidPoints, and classificationList.
#It plots the normalized data points and their assignment to each centroid (diamond-shaped) by color coding.
#It returns the cluster plot.



        