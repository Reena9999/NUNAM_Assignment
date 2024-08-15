from setuptools import setup, find_packages

setup(
    name='NUNAM_API',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'mysql-connector-python'
    ],
    entry_points={
        'console_scripts': [
            'run_api=api.api:app.run'
        ]
    },
)
