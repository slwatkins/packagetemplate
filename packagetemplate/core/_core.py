import numpy as np
from scipy import constants


__all__ = [
    "helloworld",
    "hover2pi",
]


def helloworld():
    """
    Returns the classic hello world message.

    Parameters
    ----------
    None

    Returns
    -------
    helloworld: str
        A string containing `"Hello world!"`.

    """

    return "Hello world!"


def hover2pi():
    """
    Returns the reduced Planck constant.

    Parameters
    ----------
    None

    Returns
    -------
    hover2pi: float
        The reduced Planck constant.

    Notes
    -----
    Using a mix of scipy and numpy to use the package requirements.

    """

    return constants.h / (2 * np.pi)

