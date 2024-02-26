
def calculate_wrapping_paper(l, w, h):
    """
    Calculate the total surface area of a box (a perfect right rectangular prism) with dimensions l x w x h.

    Parameters:
        l (int): length of the box
        w (int): width of the box
        h (int): height of the box

    Returns:
        int: the total surface area of the box
    """
    return 2 * l * w + 2 * w * h + 2 * h * l

def calculate_slack(side):
    """
    Calculate the area of the smallest side of a box (a perfect right rectangular prism) with dimensions l x w x h.

    Parameters:
        side (int): length or width or height of the box

    Returns:
        int: the area of the smallest side
    """
    return side ** 2

def order_wrapping_paper(present_dimensions):
    """
    Calculate the total amount of wrapping paper needed for a list of presents with dimensions given in feet.

    Parameters:
        present_dimensions (list of ints): each element is a list containing the length, width, and height of a present

    Returns:
        int: the total number of square feet of wrapping paper needed
    """
    total_area = 0
    for present in present_dimensions:
        surface_area = calculate_wrapping_paper(present[0], present[1], present[2])
        slack = calculate_slack(min(present))
        total_area += surface_area + slack
    return total_area

# Test case 1:
print(order_wrapping_paper([[2, 3, 4], [1, 1, 10]])) # Should be 58
# Test case 2:
print(order_wrapping_paper([[2, 3, 4], [1, 1, 10], [3, 4, 5]])) # Should be 61
