#!/usr/bin/python3
""" Convert Class object to JSON-like dictionary
"""


def class_to_json(obj):
    """ Convert Class object to JSON-like dictionary

    Args:
        obj: Instance of a Class

    Returns:
        dict: Dictionary representation of the object's attributes
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        # Exclude private attributes
        if not key.startswith('__'):
            json_dict[key] = value
    return json_dict
