from setuptools import setup, find_packages

setup(
    name='TapEdu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tk',
        'Pillow',
        'pyinstaller',
        'pydot-ng',
        'opencv-python',
        'numpy',
        'pygubu-designer',
    ],
)
