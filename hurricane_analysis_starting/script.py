# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def updating_damage(lst):
  updated_lst = []
  for i in lst:
    if i == 'Damages not recorded':
      updated_lst.append(i)
    else:
      if i[-1] == 'M':
        updated_lst.append(float(i[:len(i)-1]) * conversion.get("M"))
      else:
        updated_lst.append(float(i[:len(i)-1]) * conversion.get("B"))
  return updated_lst

# test function by updating damages
updated_damages = updating_damage(damages)
#print(updated_damages)

# 2 
# Create a Table
def hurr_table(name,month,year,msw,aa,damage,death):
  dic_overall = {}
  for i in range(len(name)):
    dic = {}
    dic['Name'] = name[i]
    dic['Month'] = month[i]
    dic['Year'] = year[i]
    dic['Max Sustained Wind'] = msw[i]
    dic['Areas Affected'] = aa[i]
    dic['Damage'] = damage[i]
    dic['Deaths'] = death[i]
    dic_overall[name[i]] = dic
  return dic_overall

# Create and view the hurricanes dictionary
hurr_dic = hurr_table(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
#print(hurr_dic)

# 3
# Organizing by Year
def dic_by_year(dic):
  dic_year = {}
  for i in dic:
    year = dic[i]["Year"]
    data = dic[i]
    if year not in dic_year:
      dic_year[year] = [data]
    else:
      dic_year[year].append(data)
  return dic_year

# create a new dictionary of hurricanes with year and key
#print(dic_by_year(hurr_dic))

# 4
# Counting Damaged Areas
def damage_count(dic):
  dic_count = {}
  for i in dic:
    affected = dic[i]['Areas Affected']
    for x in affected:
      if x not in dic_count:
        dic_count[x] = 1
      else:
        dic_count[x] += 1
  return dic_count

# create dictionary of areas to store the number of hurricanes involved in
aa_count = damage_count(hurr_dic)
#print(aa_count)

# 5 
# Calculating Maximum Hurricane Count
def max_hurr_count(dic):
  max_num = 0
  for i in dic:
    if dic[i] > max_num:
      max_num = dic[i]
      area = [i]
    elif dic[i] == max_num:
      area.append(i)
  if len(area) == 1:
    area = area[0]
  return area, max_num

# find most frequently affected area and the number of hurricanes involved in
area, num = max_hurr_count(aa_count)
#print(area, num)

# 6
# Calculating the Deadliest Hurricane
def most_death(dic):
  max_num = 0
  name = []
  for i in dic:
    if dic[i]["Deaths"] > max_num:
      max_num = dic[i]["Deaths"]
      name = [i]
    elif dic[i]["Deaths"] == max_num:
      name.append(i)
  if len(name) == 1:
    name = name[0]
  return name, max_num

# find highest mortality hurricane and the number of deaths
hurr, num_death = most_death(hurr_dic)
#print(hurr, num_death)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
def mortal_scale(dic):
  new = {0:[],1:[],2:[],3:[],4:[]}
  for i in dic:
    if dic[i]['Deaths'] >= mortality_scale[0] and dic[i]['Deaths'] < mortality_scale[1]:
      new[0].append(dic[i])
    elif dic[i]['Deaths'] >= mortality_scale[1] and dic[i]['Deaths'] < mortality_scale[2]:
      new[1].append(dic[i])
    elif dic[i]['Deaths'] >= mortality_scale[2] and dic[i]['Deaths'] < mortality_scale[3]:
      new[2].append(dic[i])
    elif dic[i]['Deaths'] >= mortality_scale[3] and dic[i]['Deaths'] < mortality_scale[4]:
      new[3].append(dic[i])
    else:
      new[4].append(dic[i])
  return new

# categorize hurricanes in new dictionary with mortality severity as key
mortal_rate = mortal_scale(hurr_dic)
#print(mortal_rate)

# 8 Calculating Hurricane Maximum Damage
def most_damage_cost(dic):
  max_num = 0
  name = []
  for i in dic:
    if dic[i]["Damage"] == 'Damages not recorded':
      continue
    elif dic[i]["Damage"] > max_num:
      max_num = dic[i]["Damage"]
      name = [i]
    elif dic[i]["Damage"] == max_num:
      name.append(i)
  if len(name) == 1:
    name = name[0]
  return name, max_num

# find highest damage inducing hurricane and its total cost
most_damage_hurr, cost = most_damage_cost(hurr_dic)
#print(most_damage_hurr, cost)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_scale_dic(dic):
  new = {0:[],1:[],2:[],3:[],4:[]}
  for i in dic:
    if dic[i]['Damage'] == 'Damages not recorded':
      new[0].append(dic[i])
    elif dic[i]['Damage'] >= damage_scale[0] and dic[i]['Damage'] < damage_scale[1]:
      new[0].append(dic[i])
    elif dic[i]['Damage'] >= damage_scale[1] and dic[i]['Damage'] < damage_scale[2]:
      new[1].append(dic[i])
    elif dic[i]['Damage'] >= damage_scale[2] and dic[i]['Damage'] < damage_scale[3]:
      new[2].append(dic[i])
    elif dic[i]['Damage'] >= damage_scale[3] and dic[i]['Damage'] < damage_scale[4]:
      new[3].append(dic[i])
    else:
      new[4].append(dic[i])
  return new

damage_dic = damage_scale_dic(hurr_dic)
#print(damage_dic)
