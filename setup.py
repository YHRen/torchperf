from pathlib import Path
import codecs, re

from setuptools import find_namespace_packages, setup


def find_version(file_path: str) -> str:
    with open(file_path, "r") as fp:
        version_file = fp.read()
    ptn = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(ptn, version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="pytorch-perf",
        version=find_version(Path("./torchperf/__init__.py")),
        author="Yihui Ren",
        author_email="yren@bnl.gov",
        description="A pytorch perf decorator",
        license="MIT",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/yhren/torchperf",
        keywords="decorator cuda performance perf pytorch",
        packages=find_namespace_packages(include=["torchperf", "torchperf.*"]),
        include_package_data=True,
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Operating System :: POSIX :: Linux",
        ],
        # install_requires=install_requires,
        # Install development dependencies with
        # pip install -r requirements/dev.txt -e .
    )