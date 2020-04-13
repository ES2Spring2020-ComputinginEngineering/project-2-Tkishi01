##################
#ES2 Project 2
#NearestNeighborClassification.py
#NAME: Taylor Kishinami
#HOURS NEEDED: 3
#I worked alone on this part.
#################
import numpy as np
import matplotlib.pyplot as plt
import random

# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification
#openckdfile takes no arguments.
#It reads the data from ckd.csv and formats it into arrays.
#It returns three arrays, glucose, hemoglobin, and classification.

def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD Positive")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "CKD Negative")
    plt.plot(newhemoglobin,newglucose, "b.")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()
#graphData takes three arguments: glucose, hemoglobin, and classification. All are data arrays.
#It plots the each patients' hemoglobin (x axis) and glucose (y axis). It colors and labels them accordingly.
#It returns a graph of colored points representing each patient and their respective diagnosis.
    
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
    
def createTestCase():
    newglucose = random.uniform(glucose[np.argmin(glucose)], glucose[np.argmax(glucose)])
    newhemoglobin = random.uniform(hemoglobin[np.argmin(hemoglobin)], hemoglobin[np.argmax(hemoglobin)])
    return newglucose, newhemoglobin
#createTestCase takes no arguments.
#It generates random new values for glucose and hemoglobin within their respective ranges.
#It returns these values. 

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    a = (newglucose - glucose)
    b = (newhemoglobin - hemoglobin)
    distance = np.sqrt((a**2+b**2))
    return  distance
#calculateDistanceArray takes four arguments: the randomly generated point and the arrays of glucose and hemoglobin.
#It calculates the distance from the generated point to every point in the data set.
#It returns an array containing these distances. 

def nearestNeighborClassifier(newglucose, newhemoglobin,glucose, hemoglobin, classification):
    pointindex = np.argmin(calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin))
    return classification[pointindex]
#nearestNeighborClassifier takes 5 arguments: the generated point, and all three data arrays.
#It finds index of point closest to the generated point using the minimum value of the distance array calculated by the arguments. 
#It then returns the classification of the closest point

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, nearestNeighborClass):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD Positive")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "CKD Negative")
    if nearestNeighborClass.any() == 0.0:
        plt.plot(newhemoglobin,newglucose, marker="*", markersize =10, color ="red", label = "Test Case")
    if nearestNeighborClass.any() == 1.0:
        plt.plot(newhemoglobin,newglucose, marker="*", markersize =10, color ="black", label = "Test Case")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()
#graphTestCase takes 5 arguments: the glucose and hemoglobin data arrays, the generated point, and the classification of the generated point
#It graphs the two data arrays and the generated point with color coding based on diagnosis. 
#It returns the graph.

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    k_sort = np.argsort(distance)
    k_indicies=k_sort[:k]
    k_class = classification[k_indicies]
    k_sortedclass = np.sort(k_class)
    return np.median(k_sortedclass)
#knearestNeighborClassifier takes 6 arguments: the number of neighbors, the generated point, and all 3 data arrays.
#It creates a distance array and gathers the classifications of k nearest points.
#It sorts the classifications and returns the median of k nearest points.
    
# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin = normalizeData(glucose, hemoglobin)
newglucose, newhemoglobin = createTestCase()
distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
nearestNeighborClass = nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, nearestNeighborClass)
kNearestNeighborClass = kNearestNeighborClassifier(5, newglucose, newhemoglobin, glucose, hemoglobin, classification)
poi = (np.argmin(calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)))
print("Nearest Neighbor Class =" + str(nearestNeighborClass))
print("k Nearest Neighbor Class =" + str(kNearestNeighborClass))



