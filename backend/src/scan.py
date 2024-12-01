def scan(arm_position, lrequests, tracks, debug=False):
    """
    SCAN Disk Scheduling Algorithm implementation.

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

    sequence = [current_pos]

    # Process the right requests
    for a_request in right:
        distance += abs(a_request - current_pos)
        current_pos = a_request
        sequence.append(current_pos)
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    # Move to the end of the track
    if current_pos != tracks - 1:
        distance += abs((tracks - 1) - current_pos)
        current_pos = tracks - 1
        sequence.append(current_pos)
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    # Process the left requests (move towards the left)
    for a_request in reversed(left):
        distance += abs(a_request - current_pos)
        current_pos = a_request
        sequence.append(current_pos)
        if debug: print(f"> Moved to {current_pos}, Total distance: {distance}")

    # Calculate the average distance
    average = distance / n

    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# Example usage:
# print(scan(50, [82, 170, 43, 140, 24, 16, 190], 200, debug=True))