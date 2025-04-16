"""Setup configuration for the krysztalki package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="krysztalki",
    version="0.1.0",
    author="Crystal Symmetry Team",
    author_email="author@example.com",
    description="A package for crystal symmetry analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/krysztalki",
    packages=find_packages(include=["krysztalki", "krysztalki.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        line.strip()
        for line in open("requirements.txt", encoding="utf-8")
        if line.strip() and not line.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "krysztalki=krysztalki.cli.main:main",
        ],
    },
)
