#!/usr/bin/sh

# NEVER install OF as root
if [ "$(id -u)" -eq 0 ] || [ -n "$SUDO_USER" ]; then
    echo "Do not install OpenFortress as root"
    exit
fi

# allow the user to set their own svn binary e.g. git svn
DEFAULT_SVN=svn
if [ -z "$SVN" ]; then
    SVN="$DEFAULT_SVN"
fi

# some variables to simplify changes in the future
NAME=open_fortress
OF_REPO="https://svn.openfortress.fun/svn/open_fortress/"
STEAMDIR="$HOME/.local/share/steam"


# try fetching the Distro we are on
if [ -f "/etc/os-release" ]; then
    . /etc/os-release
fi


if [ -z "$SKIP_DEPENDENCIES" ]; then
    echo "  Installing dependencies"

    case $id in

      fedora)
        sudo dnf install subversion -y
        ;;

      ubuntu | debian)
        sudo apt-get install subversion -y
        ;;

      *)
        echo "  Couldn't install dependencies."
        echo "  Install the following dependencies yourself:"
        echo "   - subversion"
        ;;
    esac
fi
echo

$SVN checkout $OF_REPO $STEAMDIR/steamapps/sourcemods/$NAME

echo
echo "  The install should now be completed."
echo "  Restart Steam to see OpenFortress in your library."
echo "  If you have any issues, join this discord server:"
echo "  https://discord.gg/Jk3NUb7"
echo "  And ping @VoxelTek#7809 in #linux-troubleshooting"
echo