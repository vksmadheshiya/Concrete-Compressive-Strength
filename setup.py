from setuptools import setup, find_packages
from typing import List


REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements_list() -> List[str]:
    """
    Description: This Function will return list of requirements mentioned in requirements.txt file
    
    return This function is going to return a list which contains name of librabries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

# Declaring Variable For setup function
NAME = "Conpressive strength check"
VERSION="0.0.2"
AUTHOR="Vikas"
DESCRIPTION="Project to predict the compressive strength of concrete"
PACKAGES = ["compressive_strength"]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    # packages=PACKAGES,
    packages = find_packages(),
    install_requires=get_requirements_list()

    

)


if __name__=="__main__":
    print(get_requirements_list)