from setuptools import setup

setup(
    name="slowda",
    version="0.1.0",
    packages=["slowda"],
    include_package_data=True,
    package_data={"slowda": ["*.so", "*.dylib", "*.dll"]},
    zip_safe=False,
)
