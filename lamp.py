import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

# read in data
Sm_duplex = pd.read_csv('/Users/tjv/LAMP/lamp/dil10.csv')
Sm_duplex_df = pd.DataFrame(Sm_duplex)

# create a figure and axis object
fig, ax1 = plt.subplots()

# plotting the first y axis
ax1.plot(Sm_duplex_df['Concn'], Sm_duplex_df['Sm_copies'], color='blue', label='Y1')
ax1.set_xlabel('Concentration of template DNA Sm&Pf')
# ax1.set_ylabel('Sm_copies', color='blue')
ax1.tick_params(axis="y", labelcolor='blue', labelright=True)

#create a second y-axis on the ax1 so that it is plotted on the left y axis
#ax2 = ax1.twinx()

# plot second y axis
ax1.plot(Sm_duplex_df['Concn'], Sm_duplex_df['Pf_copies'], color='red', label='Y2')
# ax1.set_ylabel('Pf_copies', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# create third plot
ax3 = ax1.twinx()

# third y axis
ax3.plot(Sm_duplex_df['Concn'], Sm_duplex_df['Pf_ct'], color='orange', label='Y3', linewidth=5)
ax3.set_ylabel('Pf_ct', color='orange', rotation=60)
ax3.tick_params(axis='y', labelcolor='orange')

# moving third axis y label and scale to the left using spines
ax3.yaxis.set_label_position('left')
ax3.tick_params(axis='y', direction='in')


# create fourth plot
ax4 = ax3.twinx()

# adding the fourth y axis
ax4.plot(Sm_duplex_df['Concn'], Sm_duplex_df['Sm_ct'], color="green", label='Y4')
ax4.set_ylabel('Sm_ct', color='green', rotation=60)
ax4.tick_params(axis='y', labelcolor='green')

# set the limits of the sm to match limits of the sm
ax4.set_ylim(ax3.get_ylim())

# adding a legend
lines = ax1.get_lines() + ax3.get_lines() + ax4.get_lines()# exclude ax2
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper right')

# show plot
plt.title("Comparison of simplex lamp assays for schistosomiasis and malaria")
plt.show()
