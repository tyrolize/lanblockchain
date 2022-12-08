import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lanblockchain",
    version="0.1",
    description="LAN Blockchain with the bros.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tyrolize/lanblockchain",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)