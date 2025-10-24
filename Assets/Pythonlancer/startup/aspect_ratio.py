import math


def get_aspect_ratio(width: int, height: int) -> tuple[int, int]:
    """
    Calculates the aspect ratio of given width and height in the format "x:y".

    Args:
        width: The width dimension.
        height: The height dimension.

    Returns:
        A string representing the aspect ratio in "x:y" format.
    """
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")

    # Calculate the greatest common divisor
    gcd_val = math.gcd(width, height)

    # Divide width and height by the GCD to get the simplified ratio
    simplified_width = width // gcd_val
    simplified_height = height // gcd_val

    return simplified_width, simplified_height


def get_aspect_ratio_str(width: int, height: int) -> str:
     simplified_width, simplified_height = get_aspect_ratio(width, height)
     return f"{simplified_width}:{simplified_height}"
