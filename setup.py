from distutils.core import setup, Extension


setup(
    name='strrapidjson',
    version='0.1',
    description='Python 2 interface for rapidjson which does not use unicode objects',
    long_description=open('README.rst').read(),
    author='Levon Budagyan',
    url='https://github.com/aarki/strrapidjson',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='json rapidjson',
    ext_modules=[
        Extension('strrapidjson',
                  sources=['pyrapidjson/_pyrapidjson.cpp'],
                  include_dirs=['./pyrapidjson/rapidjson/include/'],
                  )]
)
