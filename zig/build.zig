const std = @import("std");

pub fn build(b: *std.Build) void {
    std.debug.print("hello from build\n", .{});
    const optimize = b.standardOptimizeOption(.{});
    const target = b.standardTargetOptions(.{});

    const module = b.createModule(.{
        .root_source_file = b.path("src/root.zig"),
        .target = target,
        .optimize = optimize,
    });

    const lib = b.addLibrary(.{
        .linkage = .dynamic,
        .name = "slowda-zig",
        .root_module = module,
    });

    lib.linkLibC();
    b.installArtifact(lib);
}
