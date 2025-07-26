from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "AMAZON Recommender",
    version = "0.1",
    author = "Abde Ali",
    packages = find_packages(),
    install_requires = requirements,
)