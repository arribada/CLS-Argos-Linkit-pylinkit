from setuptools import setup, find_packages

setup(
    name='pygentracker',
    version='0.3.0',
    description='Python GenTracker BLE configuration tool',
    author='Liam Wickins',
    author_email='liam@icoteq.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=3.0',
    install_requires=[
        'service_identity',
        'pyasn1',
        'bleak'
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            'pygentracker = pygentracker.__main__:main'
        ]
    },
)
