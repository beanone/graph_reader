from setuptools import setup, find_packages

setup(
    name="graph-reader",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="Graph exploration library for fast retrieval from file-based graph storage with adjacency caching.",
    url="https://github.com/yourname/graph-reader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)