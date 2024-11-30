def clook(arm_position, lrequests, tracks, debug=False):
    """
    CLOOK Disk Scheduling Algorithm implementation.

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

    # Move to the right first (this is the default direction)
    if debug: print(f"Initial position: {current_pos}")

    # Process the right requests
    for a_request in right:
        distance += abs(a_request - current_pos)
        current_pos = a_request
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    # Now move to the left requests (without going to the end, just "jumping" to the first request)
    if left:
        distance += abs(current_pos - left[0])  # Jump to the first left request
        current_pos = left[0]
        if debug: print(f"> Jumped to {current_pos}, Total distance: {distance}")

        for a_request in left[1:]:
            distance += abs(a_request - current_pos)
            current_pos = a_request
            if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    # Calculate the average distance
    average = distance / n
    return {
        "sequence": [arm_position] + right + left,  # Return the order of tracks visited
        "average": average,
        "distance": distance,
    }
