#!/bin/sh

bmi=`expr $1 \* 100000 / \( $2 \* $2 \)`

if [ $bmi -lt 185 ] ; then
    echo "저체중입니다."
elif [ $bmi -ge 230 ] ; then
    echo "과체중입니다."
else 
    echo "정상체중입니다."
fi

exit 0