#!/bin/bash
# Update Script
# Script created by @WHITEDH4CKER


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mUpdating \e[1;94mWHITEDH4CKER\e[1;92m directory ...\n\n"
sleep 1.5
cd ..
rm -rf IG-BRUTEFORCE
git clone https://github.com/WHITEDH4CKER/IG-BRUTEFORCE
cd IG-BRUTEFORCE
ls
printf "\n\e[1;92m Update Complete ...\n\e[0m"

}

dependencies
script
