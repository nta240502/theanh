import numpy as np

scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])

print("Bách phân vị thứ 50: ", np.percentile(scores, 50))
print("Median = ", np.median(scores))