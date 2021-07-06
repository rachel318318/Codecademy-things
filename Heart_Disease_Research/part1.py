# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']


#Cholesterol Analysis
chol_hd = yes_hd.chol

tstat1, pval1 = ttest_1samp(chol_hd, 240)

pval1 /= 2

chol_nohd = no_hd.chol
tstat2, pval2 = ttest_1samp(chol_nohd, 240)

pval2 /= 2

print(pval1, pval2)

"""
The heart disease patients have an average of 251 mg/dl of cholesterol level. By doing the one-sample t-test and having a threshold of 0.05, the p-value is 0.0035 which shows that the cholesterol level is significanly higher than the population mean of 240 mg/dl. On the other hand, the patients with no heart disease has the p-value of 0.26, which indicates that their cholesterol level is not significantly higher.
"""

#Fasting Bolld Sugar Analysis
num_patients = len(heart)
num_highfbs_patients = len(heart[heart.fbs == 1])

pval = binom_test(num_highfbs_patients,n=num_patients,p=0.08,alternative='greater')
print(pval)

"""
As the fact that about 8% of the US population had diabetes by some estimates and fasting blood sugar levels greater than 120 mg/dl can be indicative of diabetes was given, the null hypothesis has been established saying the sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl. With the binomial test using the sample size of num_patients (which is 303) and the number of patients with fasting blood sugar > 120 mg/dl, p-val was calculated to be 4.69e-05, which shows that the sample was drawn from a population where the fasting blood sugar > 120 mg/dl is significantly greater than 8%
""" 


