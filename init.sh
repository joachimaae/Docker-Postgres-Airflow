# Folder structure, taken from https://stackoverflow.com/questions/5374382/bash-script-that-creates-a-directory-structure
sed '/^$/d;s/ /\//g' environment/struct.txt | xargs mkdir -p
cp ./environment/examples/example-* ./environment/
cd environment
for i in  "example-"*;do mv "$i" "${i#example-}";done
