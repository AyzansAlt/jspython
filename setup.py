import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyscript-pkg-vectr0", # Replace with your own username
    version="0.0.1",
    author="Vectr0 (Ayzan, VectorEngine)",
    author_email="ayzan@netriza.ml / ayzan@netriza.me",
    description="Python, but JavaScript",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netriza/pyscript",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)