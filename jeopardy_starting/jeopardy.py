import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')

####### Renaming the Columns #######
lst = []
for i in df.columns.values:
  lst.append(i.strip())

df.columns = lst
print(df)

####### Finding Questions Containing Given List of Words #######
def find_questions(lst):
  mylambda = lambda x: all(i.lower() in x.lower() for i in lst)
  return df.loc[df.Question.apply(mylambda)]

#print(find_questions(['King','England']))

####### Converting Value to float(Value) #######
lst2 = []
for i in df.Value.values:
  k = i.replace(',','')
  if k == 'None':
    lst2.append(None)
    continue
  lst2.append(float(k.strip('$')))

df['Value_float'] = lst2

####### Finding Average Value for Questions with 'King' #######
df2 = find_questions(['King'])
print(df2['Value_float'].mean())

####### Finding Unique Values for Answer #######
def unique_ans(data):
  return data.Answer.nunique()

print(unique_ans(df2))