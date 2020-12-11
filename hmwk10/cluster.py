from point import *

#Cluster class
class Cluster :
    
    def __init__(self, center = Point([0, 0])) :
        self.center = center
        self.points = set()
    
    @property    
    def coords(self) :
        return self.center.coords
        
    @property
    def dim(self) :
        return self.center.dim
        
    def addPoint(self, p) :
        self.points.add(p)
        
    def removePoint(self, p) :
        self.points.remove(p)
    
    #Returns the average distance from all of the points in self.points to
    #the current center
    @property
    def avgDistance(self) :
        sumAllDist = 0
        for x in self.points:
            sumAllDist += self.center.distFrom(x)

        agvDist = 0
        avgDist = sumAllDist / len(self.points)
        return avgDist
        
    #Updates the Points that is self.center to be the average position of all
    #the points in self.points
    #Note: if there are no points in the cluster, return without updating
    def updateCenter(self) :
        if (len(self.points) == 0):
            return
        else:
            # getting the dimensions of the point
            dimensions = len((list(self.points)[0]).coords)

            # initializing the summation of all the points
            sumOfAllDims = []
            # summing all the components of each point
            for dimInd in range(dimensions):
                holder = 0
                for x in self.points:
                    holder+= x.coords[dimInd]
                sumOfAllDims.append(holder)

            # getting the average for each component
            for ind, val in enumerate(sumOfAllDims):
                sumOfAllDims[ind] = val / len(self.points)

            self.center = Point(sumOfAllDims)
            return
            
    def printAllPoints(self) :
        print (str(self))
        for p in self.points :
            print ("   {}".format(p))
        
    def __str__(self) :
        return "Cluster: {} points and center = {}".format(len(self.points), self.center)
        
    def __repr__(self) :
        return self.__str__()

#create a list of clusters with centers initialized using data
#input: data: a k-by-d numpy array
#output: a list of k Clusters, with each cluster having a d-dimensional
#        initial center, each center coming from a row
#hint: you may find makePointList useful for this
def createClusters(data) :
    centers = makePointList(data)
    return [Cluster(c) for c in centers]

if __name__ == '__main__' :
    
    p1 = Point([1.5, 2.5])
    p2 = Point([2.0, 3.0])
    c = Cluster(Point([0.5, 3.5]))
    print(c)
    
    c.addPoint(p1)
    c.addPoint(p2)
    print(c)
    print(c.avgDistance)
    c.updateCenter()
    print(c)
    print(c.avgDistance)