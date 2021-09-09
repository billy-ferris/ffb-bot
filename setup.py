from setuptools import setup

setup(
    name='ffb-bot',

    packages=['ffb_bot'],

    include_package_data=True,

    version='0.3.0',

    install_requires=['requests>=2.0.0,<3.0.0', 'espn_api>=0.17.0', 'apscheduler>3.0.0'],

    test_suite='nose.collector',

    tests_require=['nose', 'requests_mock'],

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
