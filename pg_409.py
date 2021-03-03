import matplotlib.pyplot as mb

xv = range(1, 5001)
yv = [x**3 for x in xv]

mb.style.use('seaborn')
fig, ax = mb.subplots()
ax.scatter(xv, yv, c=yv, cmap= mb.cm.flag, s=15)

#titles
ax.set_title("Cubic numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

mb.show()