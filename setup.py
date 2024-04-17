import os

from setuptools import setup, find_packages


_PATH_ROOT = os.path.dirname(__file__)

with open(os.path.join(_PATH_ROOT, "README.md"), encoding="utf-8") as fo:
    readme = fo.read()

setup(
    name='lightllm',
    version='0.1.0',
    description='Implementation of the LLaMA language model',
    author='Big-Scale',
    url='https://github.com/Big-Scale/LightLLM.git',
    install_requires=[
        "torch>=2.0.0",
        "lightllm @ git+https://github.com/Big-Scale/LightLLM.git",
        "sentencepiece",
        "bitsandbytes",
    ],
    packages=find_packages(),
    long_description=readme,
    long_description_content_type="text/markdown",
)
