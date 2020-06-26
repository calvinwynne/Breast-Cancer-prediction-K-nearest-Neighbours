import numpy as np
import pandas as pd
import warnings 
import matplotlib.pyplot as plt
from math import sqrt
from collections import Counter as counter
plt.style.use('fivethirtyeight')


dataset = {'k': [[1,2], [2,3], [3,1]], 'r': [[6,5], [7,7], [8,6]]}
new_feature = [5, 7]


[[plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
[[print(i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_feature[0], new_feature[1], s=100)
plt.show()



def knearest_neighbors(data, predict, k):
    if len(data) >= k:
        warnings.warn('K is set to value less than total votings groups!')
    distances = []
    for group in data:
        for features in data[group]:
            #euclidean_distance = np.sqrt(np.sum(np.array(feature) - np.array(predict) **2 ))
            eculidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([eculidean_distance, group, features])
    print("Distances")
    for i in distances:
        print(i)
    print()
    votes = [i[1] for i in sorted(distances)[:k]]
    print("votes")
    for i in votes:
        print(i)
    print()
    vote_result = counter (votes).most_common(1)[0][0]
    return vote_result
            
result = knearest_neighbors(dataset, new_feature, k=3)
print(result)
