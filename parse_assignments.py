# Libraries
import json

# set the base url
BASE_URL = "https://canvas.nau.edu/courses"
# open fetched asignment data json file
with open('fetched_assignment_data.json', 'r') as file:
    new_data = json.load(file)

# Initalize an array to hold the updated data
updated_data = []

# Iterate over the raw data from the fetched json file 

for assignment in new_data:
	# put into object "extracted data"
	extracted_data = {
	    'assignment_id': assignment.get('id'),
	    'course_id': assignment.get('course_id'),
	    'name': assignment.get('name'),
	    'due_at': assignment.get('due_at'),
	    'points_possible': assignment.get('points_possible'),
	    'score': assignment.get('submission', {}).get('score', None),
	    'url': f"{BASE_URL}/{assignment.get('course_id')}/assignments/{assignment.get('id')}" if assignment.get('course_id') and assignment.get('id') else None

	}
	
	# append it to the updated data
	updated_data.append(extracted_data)
# write it to a file
with open('updated_assignment_data.json', 'w') as output:
    json.dump(updated_data, output, indent=4)

# print message
print("Data written to 'updated_assignment_data.json'")
