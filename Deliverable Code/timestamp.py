from scipy.signal import find_peaks
import numpy as np

def timestamp(t, psd):
    """ This function takes in a numpy array of filtered audio, as well as a list of times and frequencies evaluated at
    and outputs the number of fish heard in a length of time
    f: numpy array
    t: numpy array
    psd: numpy array
    """
    max_val = max(psd)

    # Using Scipy's find_peaks method
    timestamps, _ = find_peaks(psd, height=[1000000, 0.75 * max_val], distance=50)

    # Snapping shrimp can reach up to 218 decibels and are basically always snapping, so they make a stable marker
    # This means that the loudest peaks on the PSD are always going to be snapping shrimp
    shrimp_stamps, _ = find_peaks(psd, height=0.75 * max_val, distance=50)

    # Find the start of the very first group
    timestamps_groups = np.array([])
    init_time_index = None
    for init_time_index in range(0, timestamps.size - 1):
        # Look for the first peak that has a closely clustered peak right after that, which indicates it's part of a group
        if t[timestamps[init_time_index + 1]] - t[timestamps[init_time_index]] < 3:
            break
    # Look fo rhte rest of the groups:
    if init_time_index != None:
        start_time_index = init_time_index
        # Find the endpoints of every other group of glupping
        for time_index in range(init_time_index + 1, timestamps.size - 1):
            prev_time = t[timestamps[time_index - 1]]
            next_time = t[timestamps[time_index + 1]]
            current_time = t[timestamps[time_index]]
            # Find endpoints
            if next_time - current_time > 3 and current_time - prev_time < 3:  # Make sure the previous peaks are clustered close and the next peaks are far
                timestamps_groups = np.append(timestamps_groups, timestamps[start_time_index:time_index + 1])
            # Find startpoints
            if next_time - current_time < 3 and current_time - prev_time > 3:  # Make sure the next peaks are clustered close and the previous peaks are far
                # timestamps_groups = np.append(timestamps_groups, timestamps[time_index])
                start_time_index = time_index
    shrimp_stamps_result = t[shrimp_stamps[:]]
    fish_stamps_result = t[timestamps_groups[:]]
    return shrimp_stamps_result, fish_stamps_result
