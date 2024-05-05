#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/capstone/UCSB_GANER_Capstone_2023-2024/src/camera"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/capstone/UCSB_GANER_Capstone_2023-2024/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/capstone/UCSB_GANER_Capstone_2023-2024/install/lib/python3/dist-packages:/home/capstone/UCSB_GANER_Capstone_2023-2024/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/capstone/UCSB_GANER_Capstone_2023-2024/build" \
    "/usr/bin/python3" \
    "/home/capstone/UCSB_GANER_Capstone_2023-2024/src/camera/setup.py" \
     \
    build --build-base "/home/capstone/UCSB_GANER_Capstone_2023-2024/build/camera" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/capstone/UCSB_GANER_Capstone_2023-2024/install" --install-scripts="/home/capstone/UCSB_GANER_Capstone_2023-2024/install/bin"