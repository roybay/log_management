!#/bin/bash

#grep -o "error" *.txt | wc -l


input="./log.txt"
lineNumber=1
count=0
while IFS= read -r line
do
  if [[ $line == *"error"* ]]; then
  	count=$((count+1))
  	echo "$int-------------------------------"
	echo  "FIND  $line"
  fi 
  lineNumber=$((lineNumber+1))
done < "$input"
echo "========================="
echo "Total Error: $count"
echo "========================="