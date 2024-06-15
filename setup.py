from setuptools import find_packages,setup
from typing import List


hypen_e="-e."
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements    



setup(

    author="aswinprabu1999",
    version="0.0.1",
    name="ras project",
    author_email="aswinprabuaswin@gmail.com",
    packages=find_packages(),
    install_required=get_requirements("requirements.txt")

)



