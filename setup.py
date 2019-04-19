import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="haip-jira",
    version="0.1.1",
    author="Reinhard Hainz",
    author_email="reinhard.hainz@gmail.com",
    description="A JIRA API client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haipdev/jira",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "haip-config",
        "haip-template"
    ]
)
