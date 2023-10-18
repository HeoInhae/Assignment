#!/bin/sh

echo "리눅스가 재미있나요? (yes / no)"
read answer

case $answer in
    yes | y | Y | Yes | YES)
        echo "yes";;
    no | n | N | No | NO | noooo | nono)
        echo "no";;
    *)
        echo "yes 또는 no로 입력해 주세요."
        exit 1;;
esac
exit 0