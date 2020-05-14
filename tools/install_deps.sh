#!/bin/bash
#
# This script takes one optional argument. If "update" is supplied, dependencies will be
# updated instead of installed.

UPDATE=0
PIP_UPDATE=
BREW_COMMAND="install"
APT_COMMAND="install"
BREW_PACKAGES=("python3" "ninja" "wget" "gcc@7" "gcc@8" "gcc@9" "llvm" "adr-tools" "cmocka" "pkg-config")
BREW_PACKAGES+=("vale" "doxygen" "cppcheck" "clang-format" "gcovr" "lcov" "sloccount")
# TODO: test app - do I need to add anything for versions?
APT_PACKAGES=("python3" "python3-pip" "ninja-build" "wget" "build-essential" "clang" "lld" "llvm")
APT_PACKAGES+=("clang-tools" "libcmocka0" "libcmocka-dev" "pkg-config" "vale" "sloccount")
APT_PACKAGES+=("doxygen" "cppcheck" "gcovr" "lcov" "clang-format" "clang-tidy" "clang-tools")
APT_PACKAGES+=("gcc-7" "g++-7" "gcc-8" "g++-8" "gcc-9" "g++-9")
PIP3_PACKAGES=("meson" "lizard")

if [ "$1" == "update" ]; then
	UPDATE=1
	PIP_UPDATE="--upgrade"
	BREW_COMMAND="upgrade"
	APT_COMMAND="upgrade"
fi

if [ "$(uname)" == "Darwin" ]; then
	if [ $UPDATE == 1 ]; then
		# update homebrew
		brew update
	else
		#install brew if unavailable
		if [ -z "$(command -v brew)" ]; then
			/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
		fi
		# Needed for GCC compiler versions
		brew tap homebrew/cask-versions
	fi

	brew ${BREW_COMMAND} ${BREW_PACKAGES[@]}
	pip3 install ${PIP3_PACKAGES[@]} $(PIP_UPDATE)
else
	# WSL/Linux Case
	if [ $UPDATE == 0 ]; then
		# Needed for GCC versions
		sudo add-apt-repository ppa:ubuntu-toolchain-r/test
	fi

	sudo apt-get update
	sudo apt ${APT_COMMAND} ${APT_PACKAGES[@]}
	# Install pip3 dependencies globally, not just for the current user
	sudo -H pip3 install ${PIP3_PACKAGES[@]} ${PIP_UPDATE}
fi
