from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import os

class CMakeBuildExt(build_ext):
    def build_extensions(self):
        # Call CMake to build the extensions
        for ext in self.extensions:
            self.build_cmake(ext)
        super().build_extensions()

    def build_cmake(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cfg = 'Debug' if self.debug else 'Release'
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DCMAKE_BUILD_TYPE={cfg}',
        ]
        build_args = []

        os.makedirs(self.build_temp, exist_ok=True)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

extensions = [
    Extension(
        'schp.modules.src',
        sources=[
            'schp/modules/src/inplace_abn_cpu.cpp',
            'schp/modules/src/inplace_abn_cuda.cu',
            'schp/modules/src/inplace_abn_cuda_half.cu',
        ],
        include_dirs=['schp/modules/src'],
        extra_compile_args={'cxx': ['-O2'], 'nvcc': ['-O2']},
    ),
]


install_requires = [
    'pillow', 
    'tqdm', 
    'Ninja', 
    'opencv-python', 
    'torch', 
    'torchvision', 
    'torchaudio', 
    'gdown', 
]


setup(
    name='schp', 
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    ext_modules=extensions,
    cmdclass={'build_ext': CMakeBuildExt},
    entry_points={
        'console_scripts': [
        ],
    },
    author='BbChip0103',
    author_email='bbchip13@gmail.com',
    description='Package of Self Correction for Human Parsing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BbChip0103/Self-Correction-Human-Parsing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords="human, parser, clothes, segmentation",
)
