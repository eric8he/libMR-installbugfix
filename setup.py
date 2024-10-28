from setuptools import setup
from setuptools.extension import Extension
import sys
import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import numpy
except ImportError:
    install_package("numpy")
    import numpy

try:
    from Cython.Build import cythonize
except ImportError:
    install_package("cython")
    from Cython.Build import cythonize

setup(name='libmr',
      ext_modules = __import__("Cython").Build.cythonize(Extension('libmr',[
                            "python/libmr.pyx",
                            "libMR/MetaRecognition.cpp",
                            "libMR/weibull.c"
                      ],
                      include_dirs = ["libMR/", numpy.get_include()],
                      language="c++",
                  )),
      data_files = [('libMR', ['libMR/MetaRecognition.h', 'libMR/weibull.h'])],
      version = "0.1.9",
      description="LibMR, the MetaRecognition library",
      long_description=open("README.rst").read(),
      url="https://github.com/Vastlab/libMR",
      license="http://www.metarecognition.com/libmr-license/",
      author='Terry Boult, Ethan Rudd, and Manuel Gunther',
      install_requires=['cython','numpy']
)
