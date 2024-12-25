"""
Setup configuration for the aiagentaz package.

This file contains all the necessary configuration for installing and
distributing the package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README.md safely with UTF-8 encoding
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="aiagentaz",
    version="0.1.0",
    description="A Python package for easily interacting with various AI services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Md Tahseen Anam",
    author_email="tahseen.adit@gmail.com",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)