from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import shutil
import subprocess
import sys


class ZigBuildExt(build_ext):
    def run(self):
        # Build the Zig project
        zig_dir = os.path.abspath("zig")
        subprocess.check_call(["zig", "build"], cwd=zig_dir)

        # Find the compiled shared library
        lib_dir = os.path.join(zig_dir, "zig-out", "lib")
        output_dir = os.path.join(os.path.dirname(__file__), "slowda")

        for f in os.listdir(lib_dir):
            if self.is_shared_lib(f):
                print(f"Copying {f} to {output_dir}")
                shutil.copy(os.path.join(lib_dir, f), output_dir)

        # Run the normal build_ext
        super().run()

    def is_shared_lib(self, filename):
        return filename.endswith((".so", ".dll", ".dylib"))


# Dummy extension to trigger build_ext (even though we don't use it directly)
ext_modules = [
    Extension("slowda.zig_stub", sources=[]),
]

setup(
    name="slowda",
    version="0.1.0",
    packages=["slowda"],
    include_package_data=True,
    package_data={"slowda": ["*.so", "*.dylib", "*.dll"]},
    zip_safe=False,
    cmdclass={"build_ext": ZigBuildExt},
    ext_modules=ext_modules,
)
