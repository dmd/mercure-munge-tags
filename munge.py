"""
munge.py
=============
The 9.4T Bruker doesn't populate (0008,0050) AccessionNumber, and
our workflows want that. 
"""

import os
import sys
import json
from pathlib import Path

# Imports for loading DICOMs
import pydicom
from pydicom.uid import generate_uid


def process_image(file, in_folder, out_folder):
    dcm_file_in = Path(in_folder) / file
    dcm_file_out = Path(out_folder) / file

    ds = pydicom.dcmread(dcm_file_in)
    ds.AccessionNumber = f"9T{ds.StudyDate[2:]}{ds.StudyTime}"
    ds.save_as(dcm_file_out)


def main(args=sys.argv[1:]):
    """
    The module is called with two arguments from the function docker-entrypoint.sh:
    'munge.py [input-folder] [output-folder]'. The exact paths of the input-folder
    and output-folder are provided by mercure via environment variables
    """
    print(f"Running munge.py")

    # Check if the input and output folders are provided as arguments
    if len(sys.argv) < 3:
        print("Error: Missing arguments!")
        print("Usage: testmodule [input-folder] [output-folder]")
        sys.exit(1)

    # Check if the input and output folders actually exist
    in_folder = sys.argv[1]
    out_folder = sys.argv[2]
    if not Path(in_folder).exists() or not Path(out_folder).exists():
        print("IN/OUT paths do not exist")
        sys.exit(1)

    for entry in os.scandir(in_folder):
        if entry.name.endswith(".dcm") and not entry.is_dir():
            process_image(entry.name, in_folder, out_folder)


if __name__ == "__main__":
    main()
