from setuptools import setup, find_packages


setup(
      name='barbarian',
      version='0.1',
      description='Progress Bars',
      url='',
      author='Idin',
      author_email='d@idin.net',
      license='GNU AGPLv3',
      packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
      install_requires=[],
      python_requires='~=3.6',
      zip_safe=False
)