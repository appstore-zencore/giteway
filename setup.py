import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
]

setup(
    name="giteway",
    version="0.1.0",
    description="Git repos manage.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/giteway",
    author="zencore",
    author_email="appstore@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['giteway'],
    packages=find_packages("src", exclude=["src", "manage.py"]),
    package_dir={"": "src"},
    requires=requires,
    install_requires=requires,
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.*"],
    },
)