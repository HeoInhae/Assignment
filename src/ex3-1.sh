#!/bin/sh

n=$1
if [ -z $n ] ; then
    while [ 1 ]
    do
        echo "hello world"
    done
else
    while [ $n -gt 0 ]
    do
        echo "hello world"
        n=$(($n-1))
    done
fi

exit 0