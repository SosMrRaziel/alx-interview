#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize a variable to keep track of the number of
    # continuation bytes expected
    num_continuation_bytes = 0

    # Iterate through each integer in the data
    for byte in data:
        # Check if it's a continuation byte
        if num_continuation_bytes > 0:
            # If it's not in the form 10xxxxxx, it's invalid
            if not (128 <= byte < 192):
                return False
            num_continuation_bytes -= 1
        else:
            # Determine the number of continuation bytes based on the
            # first byte
            if byte < 128:
                # Single-byte character
                continue
            elif 192 <= byte < 224:
                # Two-byte character
                num_continuation_bytes = 1
            elif 224 <= byte < 240:
                # Three-byte character
                num_continuation_bytes = 2
            elif 240 <= byte < 248:
                # Four-byte character
                num_continuation_bytes = 3
            else:
                # Invalid starting byte
                return False

    # If there are remaining continuation bytes, it's invalid
    return num_continuation_bytes == 0
