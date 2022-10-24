
from invoke import task
import os
import sys

buildresults = "buildresults"
q = ""
meson="meson" 
internal_option = ""
options = ""
lto=1
debug = 1
santizier=""



if (lto==1):
    internal_option=internal_option +"-Db_lto=true -Ddisable-builtins=true"

if (debug==1):
    internal_option=internal_option+"-Ddebug=true -Doptimization=g"

if (santizier !=None):
    internal_option=internal_option+"-Db_sanitize={} -Db_lundef=false".format(santizier)




configured_build_dep="{} {} {} {} {}".format(q,meson,buildresults,internal_option,options)

@task 
def build(r):
    a = os.getcwd()
    for root, subdirs, files in os.walk(a):
         i=0
         for d in subdirs:
                if d == "{}".format(buildresults):
                    i=i+1
                    r.run("ninja -C {}".format(buildresults))

    if i == 0:            
        r.run("meson {}".format(buildresults))


@task 
def test(c):
    c.run("ninja -C {} test ".format(buildresults))

@task 
def docs(d):
    d.run("ninja -C {} docs ".format(buildresults))
@task 
def package(p):
    p.run("inv build ")
    p.run("inv docs ")
    p.run("ninja -C {} package".format(buildresults))
    p.run("ninja -C {} package-native".format(buildresults))


@task 
def reconfig(d):
    d.run("{} {} {} --reconfigure {} {}  ".format(q,meson,buildresults,internal_option,options))


@task 
def cppcheck(c):
    c.run("ninja -C {} cppcheck ".format(buildresults))

@task 
def cppcheckXml(c):
    c.run("ninja -C {} cppcheck-xml".format(buildresults))


@task 
def complexity(c):
    c.run("ninja -C {} complexity".format(buildresults))


@task 
def complexityFull(c):
    c.run("ninja -C {} complexity-full ".format(buildresults))


@task 
def scanBuild(c):
    c.run("ninja -C {} scan-build ".format(buildresults))

@task 
def tidy(c):
    c.run("ninja -C {} scan-tidy ".format(buildresults))


@task 
def sloccount(c):
    c.run("ninja -C {} sloccount ".format(buildresults))


@task 
def sloccountFull(c):
    c.run("ninja -C {} sloccount-full".format(buildresults))


@task 
def sloccountReport(c):
    c.run("ninja -C {} sloccount-report ".format(buildresults))
    

@task 
def sloccountFullReport(c):
    c.run("ninja -C {} sloccount-full-report ".format(buildresults))


@task 
def vale(c):
    c.run("ninja -C {} vale ".format(buildresults))


@task 
def coverage(c):
     a = os.getcwd()
     print(a)
     for root, subdirs, files in os.walk(a+"/coverage"):
         i=0
         for d in subdirs:
                if d == "build.ninja":
                    i=i+1
         if i ==0 :
            c.run("meson {}/coverage {} {} -Db_coverage=true ".format(buildresults,internal_option,options))

     c.run("ninja -C {} coverage test ".format(buildresults))
     c.run("ninja -C {} coverage coverage".format(buildresults))

     
@task 
def format(c):
    c.run("ninja -C {} format ".format(buildresults))

     
@task 
def formatpatch(c):
    c.run("ninja -C {} format-patch ".format(buildresults))

     
@task 
def clean (c):
    c.run("ninja -C {} clean ".format(buildresults))

     
@task 
def distclean (c):
    c.run(" rm -rf {}".format(buildresults))

     
@task 
def help (c):
    print("usage: make [OPTIONS] <target>")
    print(" Options:")
    print("   > MESON Override meson tool - useful for testing meson prereleases and forks.")
    print( " VERBOSE Show verbose output for Make rules. Default 0. Enable with 1.")
    print("     > BUILDRESULTS Directory for build results. Default buildresults.")
    print("     > OPTIONS Configuration options to pass to a build. Default empty.")
    print("     > LTO Enable LTO builds. Default 0. Enable with 1.")
    print("     > DEBUG Enable a debug build. Default 0 (release). Enable with 1.")
    print("     > CROSS Enable a Cross-compilation build. Default format is arch:chip.")
    print("         - Example: make CROSS=arm:cortex-m3")
    print("         - For supported chips, see build/cross/")
    print("         - Additional files can be layered by adding additional")
    print("           args separated by ':'")
    print("			  NOTE: cross files in this project will use Embedded Artistry libc/libcpp")
    print("			  NOTE: cross files in this project will use Embedded Artistry libc/libcpp")
    print("         > NATIVE Supply an alternative native toolchain by name.")
    print("         - Example: make NATIVE=gcc-9")
    print("         - Additional files can be layered by adding additional")
    print("           args separated by ':'")
    print("         - Example: make NATIVE=gcc-9:gcc-gold")
    print("    > SANITIZER Compile with support for a Clang/GCC Sanitizer.")
    print("         Options are: none (default), address, thread, undefined, memory,")
    print("         and address,undefined' as a combined option")
    print("Targets:")
    print("  default: Builds all default targets ninja knows about")
    print("  test: Build and run unit test programs")
    print("  docs: Generate documentation")
    print("  package: Build the project, generates docs, and create a release package")
    print("  clean: cleans build artifacts, keeping build files in place")
    print("  distclean: removes the configured build output directory")
    print("  reconfig: Reconfigure an existing build output folder with new settings")
    print("  Code Formating:")
    print("    format: runs clang-format on codebase")
    print("    format-patch: generates a patch file with formatting changes")
    print("    Static Analysis:")
    print("    cppcheck: runs cppcheck")
    print("    cppcheck-xml: runs cppcheck and generates an XML report (for build servers)")
    print("    scan-build: runs clang static analysis")
    print("    complexity: runs complexity analysis with lizard, only prints violations")
    print("    complexity-full: runs complexity analysis with lizard, prints full report")
    print("    complexity-xml: runs complexity analysis with lizard, generates XML report")
    print("        (for build servers)")
    print("	   sloccount: Run line of code and effort analysis")
    print("	   sloccount-full: Run line of code and effort analysis, with results for every file")
    print("	   sloccount-report: Run line of code and effort analysis + save to file for Jenkins")
    print("	   sloccount-full-report: Run line of code and effort analysis, with results for every file.")
    print("        Save output to a file for Jenkins")
    print("    coverage: runs code coverage analysis and generates an HTML & XML reports")
    print("    tidy: runs clang-tidy linter")
    print("    vale: lints project documentation against configured style guide")