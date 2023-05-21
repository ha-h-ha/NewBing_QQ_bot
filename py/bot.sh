#!/bin/bash
./run.sh &
echo start
while true
do
if [ -e 1.log ]
then
  echo reboot
    rm 1.log
    ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9
    sleep 2
    ./run.sh &
fi
sleep 2
done