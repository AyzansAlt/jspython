import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jspython", # Replace with your own username
    version="1.0.1",
    author="Vectr0",
    author_email="ayzan@netriza.ml",
    description="Python, but JavaScript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netriza/jspython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)