#!/bin/bash
# This script forwards all arguments to the deploy_skeleton.sh script
# The directory supplied to the script *must* be an absolute path!
#
# Note that public updates must be made to https://gist.github.com/phillipjohnston/bb95f19d156007f99be4c10c1efdf694

INITIAL_DIR=$(pwd)
cd /tmp
git clone git@github.com:embeddedartistry/project-skeleton.git --recursive --depth 1
cd project-skeleton
bash tools/deploy_skeleton.sh $@
cd ../
rm -rf project-skeleton
cd $INITIAL_DIR
