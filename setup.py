from setuptools import find_packages, setup
from typing import List

DESRCIPTION="This is a sample project for laptop price prediction"

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name="laptopRegressorProject",
    version="0.0.1",
    author="jiya",
    author_email="jiyamaryjosepha@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
