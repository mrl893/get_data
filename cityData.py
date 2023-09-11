from math import sqrt
from construct_check import check
from lab04.lab04 import LAB_SOURCE_FILE

def distance(city_a, city_b):
    city_a = make_city("city_a", 0, 1)
    city_b = make_city("city_b", 0, 2)
    distance(city_b, city_a)
    
    city_c = make_city("city_c", 6.5, 12)
    city_d = make_city("city_d",2.5, 15)
    distance(city_c, city_d)
    
def closer_city(lat, lon, city_a, city_b):
    berkeley = make_city("Berkeley", 34.87, 112.26) 
    stanford = make_city('Stanford', 34.05, 118.25)
    bucharest = make_city('Bucharest', 44.43, 26.10)
    vienna = make_city('Vienna', 48.20, 16.37)
    closer_city(41.29, 174.78, bucharest, vienna)

def check_abstraction():
    change_abstraction(True)
    
    city_a = make_city("city_a", 0, 1)
    city_b = make_city("city_b", 0, 2)

    
    city_c = make_city("city_c", 6.5, 12)
    city_d = make_city("city_d",2.5, 15)
    
    berkeley = make_city("Berkeley", 34.87, 112.26) 
    stanford = make_city('Stanford', 34.05, 118.25)
    bucharest = make_city('Bucharest', 44.43, 26.10)
    vienna = make_city('Vienna', 48.20, 16.37)
    
    check_abstraction()
    
def make_city(name, lat, lon):
    """Makes a new City object with the given name and location."""
    city = make_city("Berkeley", 0, 1)
    get_name(city)
    get_lat(city)
    get_lon(city)
    
    if check_abstraction.changed:
        return {"name": name, "lat": lat, "lon": lon}
    else:
        return [name, lat, lon]
   
def get_name(city):
    """Returns this city's name as a string."""
    """ city = make_city('Berkeley', 0, 1) get_name(city) 'Berkeley' """
    if check_abstraction.changed:
        return city["name"]
    else:
        return city[0]
    
def get_lat(city):
    """city = make_city('Berkeley', 0, 1) get_lat(city) 0 """
    if check_abstraction.changed:
        return city["lat"]
    else:
        return city[1]
        

def get_lon(city):
     """city = make_city('Berkeley', 0, 1) get_lon(city) 1 """
     if check_abstraction.changed:
         return city["lon"]
     else:
         return city[2]
def change_abstraction(change):
    change.changed = change
check_abstraction.changed = False

def add_chars(w1, w2):
    add_chars("owl", "howl")
    add_chars("want", "wanton")
    add_chars("rat", "radiate")
    add_chars("resin", "recursion")
    add_chars("fin", "effusion")
    add_chars("coy", "cacophony")
print(check(LAB_SOURCE_FILE, 'add_chars', ['For', 'While', 'Set', 'SetComp'])) # Must use recursion
