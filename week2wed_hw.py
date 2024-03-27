# Problem One

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destinations = our_routes.intersection(competitor_routes)
print(same_destinations)

our_routes_special = our_routes.difference(competitor_routes) 
print(our_routes_special)

routes_differences = our_routes.symmetric_difference(competitor_routes)
print(routes_differences)


# Problem Two

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
customer_ids_no_duplicates = set(customer_ids)

print(customer_ids_no_duplicates)