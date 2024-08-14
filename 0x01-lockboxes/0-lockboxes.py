#!/usr/bin/python3
'''A module for determining if all lockboxes can be unlocked.
'''


def canUnlockAll(boxes):
    '''Determines if all the boxes in a list can be unlocked.
    
    Given a list of boxes where each box contains keys to other boxes,
    this function checks if it's possible to unlock all boxes starting 
    from the first box (box 0).
    
    Args:
        boxes (list of list of int): A list where each element is a list
                                     of integers representing keys to other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx < 0 or boxIdx >= n:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes.update(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return len(seen_boxes) == n
