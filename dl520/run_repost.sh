#!/bin/bash
#TOP=$(dirname `readlink -n $0`)
TOP=$(cd `dirname $0`; pwd)
logfile=$TOP/logfile
i=0
while read line
do
i=$[i+1]
echo "伦哥：这个第${i}个账号哦"
echo $line
line1=`echo ${line%%-*}`
line2=`echo ${line##*-}`
echo $line1
echo $line2
python3 -u my_repost.py $line1 $line2 > $logfile/${line1} 2>&1 & 
#python3 test_comment.py $i > log.file 2>&1 &
sleep 30
done < $1
echo "邓伦：开始运行了！君君君好棒！" 
