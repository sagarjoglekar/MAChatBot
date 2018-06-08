import gdelt
import json
import platform
import multiprocessing


print (platform.platform())

print (multiprocessing.cpu_count())

# Version 2 queries
gd2 = gdelt.gdelt(version=2)

# Single 15 minute interval pull, output to json format with mentions table
results = gd2.Search('2018 June 1',table='mentions',output='json')
print(len(results))
print results
results.json()
