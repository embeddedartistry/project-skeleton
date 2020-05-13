#!/bin/bash
#
# This script configures a new repository to use the project skeleton as defined
# within this repository.
#
#
# There is a required positional argument: the destination directory to use for installing files.

## Uncomment for debugging
set -ex
PS4='${LINENO}: '

USE_GIT=1
USE_SUBMODULES=1

while getopts "rhs" opt; do
  case $opt in
	r) USE_GIT=0
	   USE_SUBMODULES=0
	;;
	s) USE_SUBMODULES=0
	;;
	h) # Help
		echo "Usage: deploy_skeleton.sh [optional ags] dest_dir"
		echo "Optional args:"
		echo "	-r: Assume non-git environment and install submodule files directly."
		echo "	-s: Don't use submodules, and copy files directly"
		exit 0
	;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

# Shift off the getopts args, leaving us with positional args
shift $((OPTIND -1))

# First positional argument is the destination folder that skeleton files will be installed to
DEST_DIR=$1
STARTING_DIR=$PWD

# Check to see if we're in tools/ or the project-skeleton root
CHECK_DIR=subprojects
if [ ! -d "$CHECK_DIR" ]; then
	cd ..
	if [ ! -d "$CHECK_DIR" ]; then
		echo "This script must be run from the project skeleton root or the tools/ directory."
		exit 1
	fi
fi

# Adjust the destination directory for relative paths in case we changed directories
# This method still supports absolute directory paths for the destination
if [ ! -d "$DEST_DIR" ]; then
	if [ -d "$STARTING_DIR/$DEST_DIR" ]; then
		DEST_DIR=$STARTING_DIR/$DEST_DIR
	else
		echo "Destination directory cannot be found. Does it exist?"
		exit 1
	fi
fi

# Remove .DS_Store files
find . -name ".DS_Store" -exec rm {} \;

CORE_FILES="docs src test tools .clang-format .clang-tidy Makefile meson.build meson_options.txt README.md"
SUBMODULES="build"
GIT_FILES=".gitattributes .github .gitignore"
if [ $USE_SUBMODULES == 1 ]; then
	GIT_FILES+=" .gitmodules"
fi

# Copy core skeleton files to the destination
cp -r $CORE_FILES $DEST_DIR
mkdir -p $DEST_DIR/subprojects
cp subprojects/*.wrap $DEST_DIR/subprojects
cp -r $GIT_FILES $DEST_DIR

if [ $USE_SUBMODULES == 0 ]; then
	git submodule update --init
	cp -r $SUBMODULES $DEST_DIR
fi
