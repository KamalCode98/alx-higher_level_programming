#!/usr/bin/python3
"""
MODULE for 1-my_list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Print the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
