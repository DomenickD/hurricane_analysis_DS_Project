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

# write your update damages function here:
def convert_damages_data(damages):

  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)

print(updated_damages)
# write your construct hurricane dictionary function here:
def create_dictionary(key, names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricane_dictionary = {}
    num_hurricanes = len(names)

    for index in range(num_hurricanes):
        hurricane_dictionary[key[index]] = {
            "Name": names[index],
            "Month": months[index],
            "Year": years[index],
            "Max Sustained Wind": max_sustained_winds[index],
            "Areas Affected": areas_affected[index],
            "Damage": updated_damages[index],
            "Deaths": deaths[index]
            }
    return hurricane_dictionary 

hurricanes_by_name = create_dictionary(names, names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes_by_name)

# write your construct hurricane by year dictionary function here:

hurricanes_by_years = create_dictionary(years, names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes_by_years)

# write your count affected areas function here:

def count_affected_areas(hurricanes):
    affected_area_count={}
    for hurr in hurricanes:
        for area in hurricanes[hurr]["Areas Affected"]:
            if area not in affected_area_count:
                affected_area_count[area] =1
            else:
                affected_area_count[area]+=1
    return affected_area_count


affected_areas = count_affected_areas(hurricanes_by_name)
print(affected_areas)


# write your find most affected area function here:
def most_affected(dict):
    max_value = max(dict.values())
    max_key = max(dict, key=dict.get)
    most_affected_response = {max_key: max_value}
    return most_affected_response

max_affected_area = most_affected(affected_areas)
print(max_affected_area)
# write your greatest number of deaths function here:
def greatest_num_deaths(dict):
    max_death = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Death'] > max_death:
            max_death = dict[name]['Death']
            hurricane_name = name
    return hurricane_name, max_death

print(greatest_num_deaths(hurricanes_by_name))

# write your catgeorize by mortality function here:
hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

def categorize_by_mortality(dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    for name in dict:
        if dict[name]['Deaths'] == mortality_scale[0]:
            hurricane_mortality[0] = name
        elif mortality_scale[0] < dict[name]['Deaths'] <= mortality_scale[1]:
            hurricane_mortality[1].append(name)
        elif mortality_scale[1] < dict[name]['Deaths'] <= mortality_scale[2]:
            hurricane_mortality[2].append(name)
        elif mortality_scale[2] < dict[name]['Deaths'] <= mortality_scale[3]:
            hurricane_mortality[3].append(name)
        elif mortality_scale[3] < dict[name]['Deaths'] <= mortality_scale[4]:
            hurricane_mortality[4].append(name)
        else:
            hurricane_mortality[5].append(name)
    return hurricane_mortality


print(categorize_by_mortality(hurricanes_by_name))

# write your greatest damage function here:
def greatest_damage_done(dict):
    damages_dealt = []
    for name in dict:
        if dict[name]['Damage'] != 'Damages not recorded':
            damages_dealt.append(dict[name]['Damage'])

    greatest_damage = max(damages_dealt)

    for name in dict:
        if dict[name]['Damage'] == greatest_damage:
            return name, greatest_damage


print(greatest_damage_done(hurricanes_by_name))



# write your catgeorize by damage function here:
damage_scale_hurricane = {'No Damage': [], 1: [], 2: [], 3: [], 4: [], 5: []}

def catagory_damage(dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    for name in dict:
        if dict[name]['Damage'] == 'Damages not recorded':
            damage_scale_hurricane['No Damage'].append(name)
        elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
            damage_scale_hurricane[1].append(name)
        elif damage_scale[1] < dict[name]['Damage'] <= damage_scale[2]:
            damage_scale_hurricane[2].append(name)
        elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
            damage_scale_hurricane[3].append(name)
        elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
            damage_scale_hurricane[4].append(name)
        else:
            damage_scale_hurricane[5].append(name)
    return damage_scale_hurricane


print(catagory_damage(hurricanes_by_name))