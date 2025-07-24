"""Setup module."""

from pathlib import Path

from setuptools import find_packages, setup

with Path("README.md").open() as file:
    readme = file.read()

with Path("LICENSE").open() as file:
    lcns = file.read()

with Path("requirements.txt").open() as file:
    requirements = file.read()
    requirements = requirements.splitlines()

setup(
    name="gen1-terminal-pokedex",
    version="1.0.0",
    description="A little gen1 cli pokedex built in python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="PericarpoQ",
    author_email="jonathagh@gmail.com",
    url="https://github.com/PericarpoQ/gen1-terminal-pokedex",
    packages=find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license=lcns,
    package_dir={"": "src"},
    package_data={"gen1_terminal_pokedex": ["assets/*"]},
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["gen1-terminal-pokedex=gen1_terminal_pokedex.cli.cli:cli"]
    },
)
