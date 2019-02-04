# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file - path
#Code starts here 
##Loading the dataframe and saving the same as a variable
data = pd.read_csv(path)

##Replacing '-' with 'Agender' using the replace() function in column Gender and saving it as variable gender_count
data["Gender"].replace('-', 'Agender', inplace = True)
gender_count = data["Gender"].value_counts()

##Plotting a bar graph of gender_count
gender_count.plot.bar()

#Code ends here


# --------------
#Code starts here 
##Creating a value-count variable for Alignment, named alignment
alignment = data["Alignment"].value_counts()

##Plotting a pie-chart of alignment and adding a label to it
alignment.plot.pie()
plt.title('Character Alignment')

#Code ends here


# --------------
#Code starts here
##Creating a new dataframe sc_df comprising only Strength and Combat
sc_df = data[["Strength", "Combat"]]

##Computing the covariance between the above two variables and the std.dev. of both and saving all three as variables
sc_covariance = sc_df["Strength"].cov(sc_df["Combat"])
sc_strength, sc_combat = sc_df.std()[0], sc_df.std()[1]

##Computing the Pearson's correlation coefficient between the above two variablesand saving it as a variable
sc_pearson = sc_covariance/(sc_strength*sc_combat)

##Repeating the same process for Intelligence and Combat
ic_df = data[["Intelligence", "Combat"]]
ic_covariance = ic_df["Intelligence"].cov(ic_df["Combat"])
ic_intelligence, ic_combat = ic_df.std()[0], ic_df.std()[1]
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

##Outputing the Pearson's correlation coefficient between Strength and Combat, and that between Intelligence and Combat
print("Strength--Combat Perason's Corr.: ", sc_pearson)
print("Intelligence--Combat Perason's Corr.: ", ic_pearson)

##Things to ponder upon:
#Q: Based on the above calculations, which attribute is more correlated to combat? Strength or Intelligence?
#A: Intelligence is more correlated with combat.
#Q: Why did we use Pearson's correlation instead of Spearman?
#A: We use Pearson's as we are dealing with quantitative data.


# --------------
#Code starts here
##Calculating the 99th percentile of Total and saving it as a variable
total_high = data["Total"].quantile(0.99)

##Subseting the dataframe for only those entries where the Total score is in the top-1%
super_best = data[data.Total > total_high]

##Outputing the top-1% Total score Names as a list
super_best_names = [super_best.Name]
print(super_best_names)

#Code ends here


# --------------
#Code starts here
##
ax_1, ax_2, ax_3 = super_best.Intelligence, super_best.Speed, super_best.Power

axes_list = [ax_1, ax_2, ax_3]

plt.boxplot(axes_list)



