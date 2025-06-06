const MyStruct = extern struct { x: c_int, y: c_int };

export fn add_structs(a: MyStruct, b: MyStruct) c_int {
    return a.x + a.y + b.x + b.y;
}
