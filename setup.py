try:
    import numpy
except ImportError:
    import subprocess
    subprocess.call("pip install numpy", shell=True)

from numpy.distutils.core import setup, Extension
ext = Extension(
    name='linextra',
    sources=['pdpack/linextra.F', 'pdpack/linpack.F'],
    include_dirs=['pdpack/include'],
    libraries=['blas']
)

setup(
    name='linextra',
    ext_modules=[ext]
)
