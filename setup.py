from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirement=[]

    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[i.replace('\n',"") for i in requirement]

    return requirement

setup(
name='Mlproject',
version='0.0.1',
author='Suhas Pawar',
author_email='suhaspawar23@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)