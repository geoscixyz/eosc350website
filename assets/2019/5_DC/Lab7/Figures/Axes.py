import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(111)
ax.set_xlim(-40,40)
ax.set_ylim(-40,0)
ax.xaxis.set_label_position('top') 
ax.xaxis.tick_top()