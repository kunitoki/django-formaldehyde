from setuptools import setup

from formaldehyde import __version__

setup(
    name='django-formaldehyde',
    version=__version__,
    license='MIT',
    url='https://github.com/kunitoki/django-formaldehyde',
    author='Lucio Asnaghi (aka kunitoki)',
    author_email='kunitoki@gmail.com',
    description='Django forms at warp speed.',
    long_description=open('README.rst').read(),
    packages=[
        'formaldehyde',
        'formaldehyde.tests',
    ],
    package_data={
        'formaldehyde': ['templates/formaldehyde/admin/*.html'],
    },
    install_requires=[
        "Django >= 1.6",
    ],
    keywords=[
        'django',
        'form',
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
