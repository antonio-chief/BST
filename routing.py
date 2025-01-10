class Location:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

def binary_search(locations, target_distance):
    left, right = 0, len(locations) - 1

    while left <= right:
        mid = (left + right) // 2

        if locations[mid].distance == target_distance:
            return locations[mid]
        elif locations[mid].distance < target_distance:
            left = mid + 1
        else:
            right = mid - 1

    # If exact match not found, return the closest location
    if right < 0:
        return locations[0]  # Closest location if target is less than the first
    if left >= len(locations):
        return locations[-1]  # Closest location if target is greater than the last

    # Return the closest of the two surrounding distances
    if (locations[left].distance - target_distance) < (target_distance - locations[right].distance):
        return locations[left]
    else:
        return locations[right]

def main():
    # Sample sorted locations (sorted by distance)
    locations = [
        Location("Location A", 5),
        Location("Location B", 10),
        Location("Location C", 15),
        Location("Location D", 20),
        Location("Location E", 25)
    ]

    # Example: Finding the nearest location to a given distance
    target_distance = 12
    nearest_location = binary_search(locations, target_distance)

    # Output the result
    print(f"The nearest location to distance {target_distance} is {nearest_location.name} at distance {nearest_location.distance}.")

if __name__ == "__main__":
    main()