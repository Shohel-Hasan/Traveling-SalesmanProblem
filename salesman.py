"""To solve the Traveling Salesman Problem (TSP) and find the best optimized traffic route for visiting all the City Bank branches, 
we can use a heuristic algorithm called the Nearest Neighbor Algorithm. This algorithm chooses the nearest unvisited city at each step, resulting in a reasonably good solution.

Here's a Python program that implements the Nearest Neighbor Algorithm to solve the TSP for the given City Bank branch locations:
"""
import math

branch_locations = [
    (23.8728568, 90.3984184, 'Uttara Branch'),
    (23.8513998, 90.3944536, 'City Bank Airport'),
    (23.8330429, 90.4092871, 'City Bank Nikunja'),
    (23.8679743, 90.3840879, 'City Bank Beside Uttara Diagnostic'),
    (23.8248293, 90.3551134, 'City Bank Mirpur 12'),
    (23.827149, 90.4106238, 'City Bank Le Meridien'),
    (23.8629078, 90.3816318, 'City Bank Shaheed Sarani'),
    (23.8673789, 90.429412, 'City Bank Narayanganj'),
    (23.8248938, 90.3549467, 'City Bank Pallabi'),
    (23.813316, 90.4147498, 'City Bank JFP')
]

def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

def tsp_nearest_neighbor(locations):
    visited = [False] * len(locations)
    route = [0]  # Start from the first location (Uttara Branch)
    total_distance = 0


    current_location_index = 0
    visited[current_location_index] = True

    while len(route) < len(locations):
        nearest_location_index = None
        nearest_distance = float('inf')

        for i, location in enumerate(locations):
            if not visited[i]:
                distance = calculate_distance(
                    locations[current_location_index][0],
                    locations[current_location_index][1],
                    location[0],
                    location[1]
                )
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_location_index = i

        
        route.append(nearest_location_index)
        total_distance += nearest_distance
        visited[nearest_location_index] = True
        current_location_index = nearest_location_index

   
    total_distance += calculate_distance(
        locations[current_location_index][0],
        locations[current_location_index][1],
        locations[0][0],
        locations[0][1]
    )
    route.append(0)

    return route, total_distance


optimized_route, total_distance = tsp_nearest_neighbor(branch_locations)


print("Optimized Route:")
for index in optimized_route:
    print(branch_locations[index][2])

print("\nTotal Distance (in kilometers):", total_distance)
