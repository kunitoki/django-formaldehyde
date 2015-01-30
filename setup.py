from setuptools import setup, find_packages

from formaldehyde import __author__, __version__, __license__, __email__

setup(
    name='django-formaldehyde',
    version=__version__,
    license=__license__,
    url='https://github.com/kunitoki/django-formaldehyde',
    author=__author__,
    author_email=__email__,
    description='Django forms at warp speed.',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django >= 1.6",
    ],
    keywords=[
        'django',
        'form',
        'forms',
        'formset'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Web Environment',
        'Topic :: Software Development',
    ]
)
