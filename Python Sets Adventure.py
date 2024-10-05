#Task 1: Flight Route Comparison
# Define the sets of flight destinations for both airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# 2. Destinations unique to our airline
unique_our_routes = our_routes.difference(competitor_routes)

# 3. Destinations unique to the competitor
unique_competitor_routes = competitor_routes.difference(our_routes)

# 4. Destinations that neither airline shares
all_destinations = our_routes.union(competitor_routes)
shared_destinations = common_destinations
unshared_destinations = all_destinations.difference(shared_destinations)

# Display the results
print("1. Destinations that both airlines fly to:", common_destinations)
print("2. Destinations unique to our airline:", unique_our_routes)
print("3. Destinations unique to competitor:", unique_competitor_routes)
print("4. Destinations that neither airline shares:", unshared_destinations)
