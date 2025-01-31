#!/bin/bash

# base url
BASE_URL="https://nau.instructure.com/api/v1"

# api key
API_KEY="19664~a67Un3MaRf2T7VCJ7hQDzr2uwP9rfPuzvFN6CCNaYxch4UuQf6rk4ZAYNTnuahk7"

#course codes
course_codes=("35851" "35935" "35850" "35859" "35867" "34795" "36223")

#fetch assignment data
fetch_assignments(){
for code in course_code;
do
    RESPONSE=$(curl -s -H "Authorization: Bearer $API_KEY" "$BASE_URL/$course")
    echo "$RESPONSE"
done 
