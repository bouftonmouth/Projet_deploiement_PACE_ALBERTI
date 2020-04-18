import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithme bio-inspire", # Replace with your own username
    version="1.1",
    author="ALBERTI Baptiste PACE Tanguy",
    author_email="baptiste.alberti@insa-lyon.fr",
    description="Optimized genome creator",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bouftonmouth/Projet_sergio",
    packages=setuptools.find_packages(),
    intall_requires=[
    	'numpy'
    	'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)