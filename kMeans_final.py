"""
CPSC-51100, SUMMER 2019
NAME: JASON HUGGY, JOHN KUAGBENU, COREY PAINTER
PROGRAMMING ASSIGNMENT #2
"""

# number of clusters is asked and stored
# use raw_input for Python 2
k = input('Enter the number of clusters: ')
k = int(k)

# retrieve the data and store it
data = [float(x.rstrip()) for x in open('prog2-input-data.txt')]

# initial centroid comes from data points
centroids = dict(zip(range(k),data[0:k]))

# inititially each cluster is blank
clusters = dict(zip(range(k),[[] for i in range(k)]))

# this is used to find the index of the centroid that is closest to each point.
# the index is essentially the cluster.
def find_closest_centroid(data, centroids):
    
    centr = [centroids.get(i) for i in centroids]
    cluster = []
    
    for i in data:
        temp_dist = []
        
        for j in centr:
            temp_dist.append(abs(i - j))
        
        cluster.append(temp_dist.index(min(temp_dist)))
        
    return cluster

# this assigns each point to the cluster that has the closest centroid
point_assignments = dict(zip(data, find_closest_centroid(data, centroids)))

old_point_assignments = dict([])

# assigns points as a list to each cluster

def assign_to_clusters (clusters, point_assignments):
    
    point_keys = list(point_assignments)
    point_enum = list(enumerate(point_assignments.values()))
    dict_enum = dict(point_enum)
    
    for i in clusters:
        cluster_list = []
        index_list = []
        
        for j,v in dict_enum.items():
            index = j
            
            if v == i:
                index_list.append(index)
                
        for m in index_list:
            cluster_list.append(point_keys[m])
        
        print (i , cluster_list)
        
        clusters.update({i : cluster_list})
        
# takes the average of the points in each cluster to determine the new centroid
# updates centroids
def update_centroids(clusters, centroids):
    
    for i, j in clusters.items():
        centroid = ((sum(j)/len(j)))
    
        centroids.update({i : centroid})
        
count = 1

while True:
    
    print("\n Iteration", count)
    
    count += 1
    
    old_point_assignments = point_assignments  # update old points if the points have changed
    
    assign_to_clusters(clusters, point_assignments) # apply function
    
    update_centroids(clusters, centroids)  # apply funciton
    
    clusters = dict(zip(range(k),[[] for i in range(k)]))  # reinitialize clusters to empty lists
    
    point_assignments = dict(zip(data, find_closest_centroid(data, centroids)))   #update point assignments
    
    if point_assignments == old_point_assignments:  # if points don't change, then end
        break
    

print("\n")
# prints the final results of what point belongs to each cluster 
# in console and text file
file = open('prog2-input-data.txt', 'w')

for i,j in point_assignments.items():  
    print ("Point", i , "in cluster", j)
    # the next four lines prints the output to text file
    list = ["Point", i , "in cluster", j, "\n"]
    list = map(str, list)
    line = " ".join(list)
    file.write(line)
    
file.close()