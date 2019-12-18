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

#path_to_zip_file = Path("datasets.zip").absolute()
path_to_zip_file = "datasets.zip"
directory_to_extract_to = Path().absolute()
print(f"Path to zip file: {path_to_zip_file}")
print(f"Directory to extract to: {directory_to_extract_to}")

# -

zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()
"""
print(20*"*")
#import pathlib
#current_dir = pathlib.Path(__file__).parent
#current_file = pathlib.Path(__file__)
#print(f"Current Directory: {current_dir}")
#print(f"Current File: {current_file}")

#print(os.path.abspath(__file__))

from pathlib import Path
print("File      Path:", Path(path_to_zip_file).absolute())
print("Directory Path:", Path().absolute()) 

"""


