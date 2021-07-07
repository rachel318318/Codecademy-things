# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

# Predictors of Heart Disease
sns.boxplot(x = heart.heart_disease, y = heart.thalach)
plt.show()

thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

mean_diff = np.mean(thalach_hd) - np.mean(thalach_no_hd)
median_diff = np.median(thalach_hd) - np.median(thalach_no_hd)
print('The mean difference of maximum heart rate between patients with heart disease and without heart disease is', mean_diff)
print('The median difference of maximum heart rate between patients with heart disease and without heart disease is', median_diff)

tstat, pval_two = ttest_ind(thalach_hd, thalach_no_hd)
print('From two-sample t-test, the pval for maximum heart rate between patients with heart disease and without heart disease is', pval_two, '. This indicates that the difference is significant, and the null hypothesis can be rejected, which is the average maxumum heart rate for a person with heart disease is equal to the one for a person without heart disease.')

# Chest Pain and Max Heart Rate
plt.clf()
sns.boxplot(x = heart.cp, y = heart.thalach)
plt.show()

thalach_typical = heart.thalach[heart.cp == 
'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

fstat, pval_anova = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)

print("From ANOVA test, the pval is', pval_anova, ', which shows that at least one pair of chest pain types has significantly different average max heart rates during excercise. To determine which of those pairs are significantly difference, Tukey's Range Test can be used.")

tukey_results = pairwise_tukeyhsd(heart.thalach, heart.cp, 0.05)
print(tukey_results)
print("The Tukey's Range Test result table shows that atypical angina has a significant difference from all other types of chest pain based on their p-values. However, the other pairs do now show any significant difference.")

# Heart Disease and Chest Pain
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
chi2, pval_chi2, dof, expected = chi2_contingency(Xtab)
print("Furthermore, the association between chest pain type and heart disease diagnosis has been investigated. With the type 1 error rate of 0.05, pval from the Chi-Square test is", pval_chi2, ", which concludes that there is a significant association between those variables.")
