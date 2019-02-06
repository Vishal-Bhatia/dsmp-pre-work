# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
##Using read.csv() to load the data onto a dataframe variable
df = pd.read_csv(path)

##Computing the probability that the FICO score is above 700
df1 = df[df.fico > 700]
p_a = len(df1)/len(df)

##Computing the probability that the purpose of the loan is debt consolidation
df2 = df[df.purpose == 'debt_consolidation']
p_b = len(df2)/len(df)

##Computing the probability that the purpose of the loan is debt consolidation given a FICO score of above 700
df3 = df1[df1.purpose == 'debt_consolidation']
p_a_b = len(df3)/len(df1)

##Checking for independency
result = bool(p_a_b == p_b)

##Outputting the independency result
print(result)

# code ends here


# --------------
# code starts here
##Computing the probability that the loan has been paid back
df4 = df[df["paid.back.loan"] == "Yes"]
prob_lp = len(df4)/len(df)

##Computing the probability that the underwriting criteria of LendingClub.com are met
df5 = df[df["credit.policy"] == "Yes"]
prob_cs = len(df5)/len(df)

##Subsetting a new database comprising only those entries where the loan has been paid back [recreating the first subset to meet GreyAtom checks on the code]
new_df = df[df["paid.back.loan"] == "Yes"]

##Computing the probability that the the loan has been paid back given the underwriting criteria of LendingClub.com are met
df6 = df4[df4["credit.policy"] == "Yes"]
prob_pd_cs = len(df6)/len(df4)

##Applying Bayes theorem
bayes = prob_pd_cs*prob_lp/prob_cs

##Outputting the conditional probability
print(bayes)

# code ends here


# --------------
# code starts here
##Subsetting a new database comprising only those entries where the loan has not been paid back
df1 = df[df["paid.back.loan"] == "No"]

##Using value_counts() on purpose in the subsetted dataframe, and outputting the same
purpose_vc = df1["purpose"].value_counts()

##Plotting the bar chart for purpose
purpose_vc.plot.bar()

# code ends here


# --------------
# code starts here
##Computing the median and mean for installment
inst_median = df.installment.median()
inst_mean = df.installment.mean()

##Plotting the histogram for installment
df_inst = df.installment
hist_inst = df_inst.plot.hist(bins = 30)
print(hist_inst)

##Plotting the histogram for log of annual income
df_loginc = df["log.annual.inc"]
hist_loginc = df_loginc.plot.hist(bins = 30)
print(hist_loginc)

# code ends here


