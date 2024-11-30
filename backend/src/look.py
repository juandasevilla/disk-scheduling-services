def look(arm_position, lrequests, tracks, debug=False):
    """
    LOOK Disk Scheduling Algorithm implementation.

    Args:
        arm_position (int): The initial position of the disk arm.
        lrequests (list[int]): The list of requested tracks.
        tracks (int): Total number of tracks (cylinders).
        debug (bool): If True, prints debug information.

    Returns:
        dict: Result containing the sequence, average seek distance, and total distance.
    """
    distance = 0
    n = len(lrequests)
    current_pos = arm_position

    # Sort the request list
    lrequests.sort()

    # Split requests into two lists: one for tracks to the left, one for tracks to the right
    left = [req for req in lrequests if req < arm_position]
    right = [req for req in lrequests if req >= arm_position]

    # Process the right requests (move towards the right first)
    if debug: print(f"Initial position: {current_pos}")

    # Process the right requests
    for a_request in right:
        distance += abs(a_request - current_pos)
        current_pos = a_request
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    closest_left = None

    if left:
        # Find the closest left request to the last right request
        closest_left = min(left, key=lambda x: abs(x - current_pos))
        distance += abs(closest_left - current_pos)
        current_pos = closest_left
        left.remove(closest_left)
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

        # Process remaining left requests
    for a_request in sorted(left, key=lambda x: abs(x - current_pos)):
        distance += abs(a_request - current_pos)
        current_pos = a_request
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

        # Calculate the average distance
    average = distance / n

    if closest_left is not None:
        return {
            "sequence": [arm_position] + right + [closest_left] + sorted(left),
            "average": average,
            "distance": distance,
        }
    else:
        return {
            "sequence": [arm_position] + right + sorted(left),
            "average": average,
            "distance": distance,
        }