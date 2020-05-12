# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-CurdtMillion3",  # the name that you will install via pip
    version="1.4",
    author="Curdt Million",
    author_email="curtcecil@gmail.com",
    description="My first attempt",
    long_description=long_description,
    long_description_content_type="text/markdown",  # required if using md file
    #license="MIT",
    url="https://github.com/CurdtMillion/lambdata-curdtmillion",
    #keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
