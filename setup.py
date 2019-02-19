import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="minima-test-test-schwdback",
    version="0.0.2",
    author="Lisback- Danlick",
    author_email="wasnice@uni-potsdam.de",
    description="A library to find function maxima",

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/pianobacki/testing.git",
    packages=['maxima'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
