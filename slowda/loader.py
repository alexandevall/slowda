import os
import sys
import ctypes


def load_lib():
    if sys.platform.startswith("darwin"):
        lib_name = "libslowda-zig.dylib"
    elif sys.platform.startswith("linux"):
        lib_name = "libslowda-zig.so"
    elif sys.platform.startswith("win32"):
        lib_name = "libslowda-zig.dll"
    else:
        raise RuntimeError("Unsupported platform")
    lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), lib_name))
    return lib


lib = load_lib()


class MyStruct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


lib.add_structs.argtypes = [MyStruct, MyStruct]
lib.add_structs.restype = ctypes.c_int


def add_structs(a: MyStruct, b: MyStruct) -> int:
    return lib.add_structs(a, b)
