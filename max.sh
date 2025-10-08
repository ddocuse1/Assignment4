#!/bin/bash
read -p 'Input 1:' a
read -p 'Input 2:' b
if [ $a -gt $b ]; then
    echo $a
fi
if [ $b -gt $a ]; then
    echo $b
fi
