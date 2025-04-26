#!/bin/bash
scanPorts() {
    echo "Enter the IP address to verify:"
    read ipAddress
    echo "Enter range of ports to be scanned: e.g. (20-80) : "
    read portsRange
    if [ -z "$ipAddress" ]|| [ -z "$portsRange" ]; then
       echo "You must enter an IP address and port ranges to be scanned"
       return
    fi
 #Performing port scanning using nmap
    echo "Checking the ports $portsRange in the IP network $ipAddress"
    nmap -p "$portsRange" "$ipAddress"
 #Conditional opens to check if the nmap scan was successful
    if [ $? -ne 0 ]; then #If it is different from 0, it means that it was not successfully executed
       echo "An error occurred during scanning"
    else
       echo "Successful verification"
    fi
}
echo "Please choose one of the 2 options: "
echo "1.- General port scanning."
echo "2.- Exit the program.."
read -p "(1 o 2)" option
	case $option in
		1)
			scanPorts
		;;
		2)
			echo "Exiting the program...."
			break
		;;
		*)
			echo "Invalid option"
		;;
	esac





