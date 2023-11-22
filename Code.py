# Define the routes, passengers, and rickshaw capacity
routes = [2, 3, 4, 2.5, 5, 4.2]
passengers = [4, 2, 5, 6, 3, 1]
rickshaw_capacity = 5

# Create a list of tuples (distance, passengers, route number, score)
# If passengers on a route are more than rickshaw capacity, consider
# only the rickshaw capacity
route_info = [(dist, 
               min(pax, rickshaw_capacity), 
               route+1, 
               min(pax, rickshaw_capacity)/dist) 
              for route, 
              (dist,pax) in enumerate(zip(routes, passengers))]

# Sort the list by score (descending) and passengers (descending)
route_info.sort(key=lambda x: (-x[3], -x[1]))

# The first route in the sorted list is the one with 
# the highest score and maximum passengers
selected_route = route_info[0]

print(f"The selected route is Route {selected_route[2]} with a distance of {selected_route[0]} km and {selected_route[1]} passengers.")