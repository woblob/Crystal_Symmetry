"""Module for saving crystallographic data to text files.

This module provides functions for saving and formatting symmetry data
and vacancy configurations to text files.
"""

from typing import List, Tuple, Any
from datetime import datetime


def zapis_zredukowany() -> None:
    """Read symmetry data from a file, reduce it to unique entries, and save to a new file.

    Reads from "output of symmetries 2019_09_28_13_06_50.txt" and writes to "plik2.txt".
    """
    with open(
        "output of symmetries 2019_09_28_13_06_50.txt", "r", encoding="utf-8"
    ) as f:
        myset = set()
        for line in f:
            chs = line.split("\t")[-1]
            myset.add(chs)
    plik = list(myset)

    with open("plik2.txt", "w", encoding="utf-8") as f:
        # Sort by length in descending order
        for l in sorted(plik, key=len, reverse=True):
            # print(len(l), l )
            f.write(l)


def back2normal(output: List[Tuple[float, List[Any]]], size: float) -> List[str]:
    """Convert output data back to a normal format for saving.

    Args:
        output: List of tuples containing a float and a list of data
        size: Size parameter for scaling

    Returns:
        List of formatted strings ready for writing to a file
    """
    mylist = []
    for el0, el1 in sorted(output, key=lambda x: len(x[1]), reverse=True):
        # if el1 != []:
        vacs = ((el0 + 1) * (size / 2)).tolist()
        myvar = ""
        for vac in vacs:
            myvar += str(vac) + ";\t"
        mylist.append(myvar + str(el1) + "\n")
    # else:
    #   break
    return mylist


def saveOutput2(
    OUTPUT: List[Tuple[float, List[Any]]], size: float, filename: str
) -> None:
    """Save output data to a file with a timestamp in the filename.

    Args:
        OUTPUT: List of tuples containing a float and a list of data
        size: Size parameter for scaling
        filename: Base filename to use (will be appended with timestamp)
    """
    # Convert the output data to a formatted list of strings
    modOUTPUT = back2normal(OUTPUT, size)

    # Add timestamp to filename
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    full_filename = f"{filename} {timestamp}.txt"

    # Write the data to the file
    with open(full_filename, "w", encoding="utf-8") as f:
        for line in modOUTPUT:
            f.write(str(line))
