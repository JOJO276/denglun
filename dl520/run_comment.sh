#!/bin/bash
while read line
do
echo $line
line1=`echo ${line%%-*}`
line2=`echo ${line##*-}`
echo $line1
echo $line2
#python3 test_repost_new.py $line1 $line2 > $line1 2>&1 & 
python3 test_comment.py $line1 $line2 > log.file 2>&1 &
sleep 30 
done < $1 
