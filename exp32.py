import matplotlib.pyplot as plt

heights = [160, 165, 170, 172, 168, 175, 163,
           180, 169, 174, 177, 166, 171, 173, 178]

plt.hist(heights, bins=5, edgecolor="black")

plt.title("Distribution of Classmates' Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")

plt.show()