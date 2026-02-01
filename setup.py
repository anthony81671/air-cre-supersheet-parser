"""Setup script for AIR CRE SuperSheet Parser."""

from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="air-cre-supersheet-parser",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Production-ready parser for AIR CRE SuperSheet PDF files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anthony81671/air-cre-supersheet-parser",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "air-cre-parse=src.main:cli",
        ],
    },
)
