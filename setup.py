import os
from setuptools import find_packages, setup

# determining the directory containing setup.py
setup_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_path, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    # package information
    name="sendtelegram",
    packages=find_packages(),
    version="0.2.0",
    description="A telegram replacement for sendmail.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    url="https://github.com/gstracquadanio/sendtelegram",
    keywords="",
    #  author information
    author="Giovanni Stracquadanio",
    author_email="giovanni.stracquadanio@ed.ac.uk",
    # installation info and requirements
    install_requires=["requests>=2.22", "argh>=0.26"],
    setup_requires=[],
    # test info and requirements
    test_suite="tests",
    tests_require=[],
    # package deployment info
    include_package_data=True,
    zip_safe=False,
    # all tools have cli interface
    entry_points={"console_scripts": ["sendtelegram=sendtelegram.cli:main"]},
)
