import matplotlib.pyplot as plt
from random_walk import RandomWalk


"""x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

# plot the points and set a gradient of blue to the graph
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label the axis
ax.set_title("Square Number", fontsize=18)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Square of Value", fontsize=10)
# set axis ranges
ax.axis([0, 1100, 0, 1100000])

# turn off the exponent representation of the axis
ax.get_xaxis().get_major_formatter().set_scientific(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)

# set size of tick
ax.tick_params(axis='both', labelsize=14)

plt.show()
"""

    # Make a random walk
rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10,6), dpi=128)
point_numbers = range(rw.num_points)
#plot values while using a blue gradient
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=2)

# emphasize first and last points
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()





