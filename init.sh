if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# Folder structure, taken from https://stackoverflow.com/questions/5374382/bash-script-that-creates-a-directory-structure
sed '/^$/d;s/ /\//g' environment/struct.txt | xargs mkdir -p
chown <ADMINUSER>:<ADMINUSER> DataStorage -R
