from setuptools import setup
import os
import subprocess



# class ZigBuildExt(build_ext):
#     def run(self):
#         # se where we are
#         here = os.path.abspath(os.path.dirname(__file__))
#         print("-> here", here)
#         zig_dir = os.path.join(here, "zig")
#         print("-> zig_dir", zig_dir)
#         output_lib_dir = os.path.join(zig_dir, "zig-out", "lib")
#         print("-> output_lib_dir", output_lib_dir)

#         # Build the Zig project
#         print("-> build zig project")
#         zig_dir = os.path.abspath("zig")
#         print("-> zig dir", zig_dir)

#         print("-> ls")
#         subprocess.check_call(["ls"])

#         print("-> ls done")

#         # subprocess.check_call(["zig", "build"], cwd=zig_dir)
#         subprocess.check_call(["zig", "build"], cwd="zig")
#         print("-> did build")
#         # Find the compiled shared library
#         lib_dir = os.path.join(zig_dir, "zig-out", "lib")
#         print("-> lib_dir", lib_dir)
#         output_dir = os.path.join(os.path.dirname(__file__), "slowda")
#         print("-> output_dir", output_dir)

#         for f in os.listdir(lib_dir):
#             print("-> f", f)
#             if self.is_shared_lib(f):
#                 print(f"Copying {f} to {output_dir}")
#                 shutil.copy(os.path.join(lib_dir, f), output_dir)

#         # Run the normal build_ext
#         super().run()

#     def is_shared_lib(self, filename):
#         return filename.endswith((".so", ".dll", ".dylib"))


# # Dummy extension to trigger build_ext (even though we don't use it directly)
# # ext_modules = [
# #     Extension("slowda.zig_stub", sources=[]),
# # ]

print("-> set ups")

here = os.path.abspath(os.path.dirname(__file__))
print("-> here", here)
zig_dir = os.path.join(here, "zig")
print("-> zig_dir", zig_dir)
output_lib_dir = os.path.join(zig_dir, "zig-out", "lib")
print("-> output_lib_dir", output_lib_dir)

print("-> ls")
subprocess.check_call(["ls"])

print("-> ls done")

setup(
    name="slowda",
    version="0.1.0",
    packages=["slowda"],
    include_package_data=True,
    package_data={"slowda": ["*.so", "*.dylib", "*.dll"]},
    zip_safe=False,
    # cmdclass={"build_ext": ZigBuildExt},
    # ext_modules=ext_modules,
)
