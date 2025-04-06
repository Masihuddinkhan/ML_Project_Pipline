from setuptools import setup, find_packages
from typing import List


HYPHOP_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]
        
        if HYPHOP_E_DOT in requirements:
            requirements.remove(HYPHOP_E_DOT)


setup(name='ML_Pipeline',
      version='0.0.1',
      author='Masihuddin',
      description='Machine Learning Pipeline',
      author_email='masihuddinkhan025@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
)