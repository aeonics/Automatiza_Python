#Create an "If-Else" condition in the "For"-Loop of the "Exercise Script" that prints you the number of characters of the 35th generated value of the variable "var". Submit the number 
#!/bin/bash
# Count number of characters in a variable:
#     echo $variable | wc -c

# Variable to encode
var="nef892na9s1p9asn2aJs71nIsm"

for counter in {1..40}
do
        var=$(echo $var | base64)
        echo $counter
        if [ $counter -eq 35 ]; 
        then
            echo $var | wc -c
            break
        fi

done
# of characters in the 35th value of the variable "var".   
