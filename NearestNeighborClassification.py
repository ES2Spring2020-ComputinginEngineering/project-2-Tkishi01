#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD Positive")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "CKD Negative")
    plt.plot(newhemoglobin,newglucose, "b.")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    return plt.show()

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

def createTestCase():
    newglucose = random.uniform(glucose[np.argmin(glucose)], glucose[np.argmax(glucose)])
    newhemoglobin = random.uniform(hemoglobin[np.argmin(hemoglobin)], hemoglobin[np.argmax(hemoglobin)])
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    a = (newglucose - glucose)
    b = (newhemoglobin - hemoglobin)
    distance = np.sqrt((a**2+b**2))
    return  distance

def nearestNeighborClassifier(newglucose, newhemoglobin,glucose, hemoglobin, classification):
    pointindex = np.argmin(calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin))
    return classification[pointindex]

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

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distance = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    k_sort = np.argsort(distance)
    k_indicies=k_sort[:k]
    k_class = classification[k_indicies]
    k_sortedclass = np.sort(k_class)
    return np.median(k_sortedclass)
    
    
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


