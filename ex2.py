import numpy as np
import pandas as pd
# Data from fitness tracker (10 days)
Tracker = pd.DataFrame({'Day': [1,2,3,4,5,6,7,8,9,10],
'Steps': [7079, 8576, 6586, 4508, 5564, 6971, 7733, 8520, 9753, 9569]})
# i) Represent data in 10x2 array
print("i) 10x2 Array (Day, Steps):\n", Tracker)
# ii) Add 2000 steps (after 7 pm) to all observations
Tracker['Updated_Steps'] = Tracker['Steps'] + 1000
print("\nii) Updated Array (after adding 2000 steps):\n", Tracker[['Day','Updated_Steps']])
# iii) Steps walked more than 9000
above_7000 = Tracker[Tracker['Updated_Steps']> 7000]
print("\niii) Steps walked more than 7000:\n", above_7000[['Day','Updated_Steps']])
# iv) Steps walked in sorted order
sorted_steps = np.sort(Tracker['Updated_Steps'])
print("\niv) Steps walked in sorted order:\n", sorted_steps)