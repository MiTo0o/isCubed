from setuptools import setup

setup(
  name="isCubed",
  version="0.01",
  description="Check if number is perfect cube",
  url="https://github.com/MiTo0o",
  author="MiTo",
  author_email="derzanchiang1800@gmail.com",
  license="MIT",
  packages=["isCubed"],
  zip_safe=False,
  long_description="""
# isCubed
________

Check if a number is a perfect cube

## install
    pip install isCubed

If that doesnt work try:

    pip3 install isCubed

## usage

```py
from isCubed import isCubed

print(isCubed(5))
#prints False

print(isCubed(27))
#prints True

```
  """,
  long_description_content_type='text/markdown'
)