import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='livecpi',  
     version='0.1',
     scripts=['livecpi'] ,
     author="Christian Matthy",
     author_email="cjmatthy200@gmail.com",
     description="Calculates Pi using different methods",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/MatthyPlayz/LiveCPi",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
