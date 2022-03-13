travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
country_name=input("Type your visited country: ")
time=int(input("How many times you visited there? "))
city_name=input("Which city you visited there? Enter city name separated by coma: ").split(",")
def add_new_country(country_visited,time_visited,city_visited):
    new_country={}
    new_country['country']=country_visited
    new_country['visits']=time_visited
    city=[city for city in city_name]
    new_country['cities']=city
    travel_log.append(new_country)
add_new_country(country_name,time,city_name)
print(travel_log)