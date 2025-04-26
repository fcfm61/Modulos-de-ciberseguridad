#!/bin/bash

is_alive_ping()
{
  ping -c 1 $1 > /dev/null
  [ $? -eq 0 ] && echo Node with IP: $i is up.
}
echo "Welcome to the network monitoring, please choose one of the following options"
echo "1.- General network monitoring"
echo "2.- Exit the program"
read -p "(1 o 2)" option
case $option in
	1)
for i in 192.168.0.{1..255}
do
is_alive_ping $i & disown
done

for i in {1..255}; do
  timeout i bash -c "ping -c 1 192.168.0.$i" > /dev/null 2>&1
  if [ $? -eq 0 ]; then
        echo "The host 192.168.0.$1 is active"
  fi
done

# Check System Uptime
tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $tecreset $tecuptime
        ;;
	2)
echo "Coming out of the program...."
break
	;;
	*)
echo "Invalid option"
	;;
esac

