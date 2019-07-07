!#/bin/bash

#grep -o "error" *.txt | wc -l


input="./log2.txt"
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








filepath = 'log2.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   tmp = []
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       print("---------------")
       tmp=line.strip().split(" ", 1)
       print("Arry : {}".format(tmp))
       print("Date : {}".format(tmp[0]))
       print("Rest : {}".format(tmp[1]))     
       print("===============")
       cnt += 1



with open(filepath, "r") as logs:
for log in logs:
	print("Line : {}".format(log))
    print("---------------")
    str = log.split(" ", 1)
    print("Arry : {}".format(str))
    print("Date : {}".format(str[0]))
    print("Rest : {}".format(str[1]))     
    print("===============")

    str = log.split("", 1)
    print(str)
