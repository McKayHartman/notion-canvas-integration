#!/bin/bash

# base url
BASE_URL="https://canvas.nau.com/api/v1"

# api key
API_KEY="19664~a67Un3MaRf2T7VCJ7hQDzr2uwP9rfPuzvFN6CCNaYxch4UuQf6rk4ZAYNTnuahk7"

#course codes
CODES=("35851" "35935" "35850" "35859" "35867" "34795" "36223")

#output
output_file="fetched_assignment_data.json"

#clear file
echo "[" > "$output_file"

#get assignement data
fetch_assignments(){
for code in "${CODES[@]}"
    do
	echo "$code info"
        RESPONSE=$(curl -s -X GET -H "Authorization: Bearer $API_KEY" "https://canvas.nau.edu/api/v1/courses/$code/assignments")
        echo "$RESPONSE" >> "$output_file"

	if [ "$course_id" != "${CODES[-1]}" ] && [ -n "$course_id" ]; then
	    echo "." >> "$output_file"
	fi
    done

echo "]" >> "$output_file"

echo "Data saved to $output_file"
}
fetch_assignments 
