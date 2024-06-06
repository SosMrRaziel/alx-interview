#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """ Determine if all the boxes can be opened """
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while True:
        any_box_unlocked = False
        for i, box in enumerate(boxes):
            if unlocked[i]:
                continue  # Skip already unlocked boxes
            if i in keys:
                unlocked[i] = True  # Unlock the box
                keys.update(box)  # Add new keys to the set
                any_box_unlocked = True
        if not any_box_unlocked:
            break  # Exit if no new boxes were unlocked in this iteration

    return all(unlocked)  # Check if all boxes are unlocked