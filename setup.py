from setuptools import setup, find_packages

setup(
    name='boxcar',
    version=__import__('boxcar').__version__,
    description='The service for Boxcar',
    author='TualatriX',
    author_email='tualatrix@gmail.com',
    license='BSD',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
)
