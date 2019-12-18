# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# #### L1-1: Unzipping datasets.zip

# +
import zipfile
from pathlib import Path #NGL

path_to_zip_file = "datasets.zip"
directory_to_extract_to = Path().absolute()
# print(f"Path to zip file: {path_to_zip_file}") # Check file path
# print(f"Directory to extract to: {directory_to_extract_to}") # Check directory for extraction


# +
def extract_file(z_file, extraction_dest):
    zip_ref = zipfile.ZipFile(z_file, 'r')
    zip_ref.extractall(extraction_dest)
    zip_ref.close()
    
# extract_file(path_to_zip_file, directory_to_extract_to) # -> Run this only once!

# -


