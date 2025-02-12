# libraries
import requests
import json

# Constants
API = "https://api.notion.com/v1"
TOKEN = "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"
DATABASE = "17a2cfc01df7809b9c5eebf3bce0f965"

# Headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    # ** If you dont update this, the
    # ** program will stop working when the
    # ** version changes.
    "Notion-Version": "2022-06-28"
}

# Delete any data currently in the databse
response = requests.post(
    f"{API}/databases/{DATABASE}/query", headers=headers)

# check the status code successful
if response.status_code == 200:
    pages = response.json()["results"]
else:
    print(f"Error 1: {response.status_code}, {response.text}")

# send delete request
for page in pages:
    page_id = page['id']
    delete_response = requests.patch(
    f"{API}/pages/{page_id}", headers=headers,
    json={"archived": True}
    )

    if delete_response.status_code == 200:
        print(f"Deleted page with ID: {page_id}")
    else:
        print(f"Failed tp delete page {page_id}: {delete_response.status_code} - ")

# Write the new data
with open('updated_assignment_data.json', 'r') as file:
    updated_data = json.load(file)
    for assignment in updated_data:
        new_page_data = {
            "parent": {"database_id": DATABASE},
            "properties": {
                "Assignment Name": {
                    "rich_text": [
                        {"text": {"content": assignment['name'] if assignment['name'] else "Untitled Assignment"}}
                    ]
                },
                "Course ID": {
                    "number": int(assignment['course_id']) if assignment['course_id'] else 0
                },
                "Due Date": {
                    "date": {"start": assignment['due_at']} if assignment['due_at'] else {"start": "2025-01-01"}
                },
                "Score": {
                    "number": assignment['score'] if assignment['score'] is not None else 0
                },
                "Points Possible": {
                    "number": assignment['points_possible'] if assignment['points_possible'] is not None else 0
                },
                "URL": {"url": assignment['url']} if assignment['url'] else {}
                
            }
        }
        print(json.dumps(new_page_data, indent=4))	
	# send the request via api POST
        #response = requests.get(f"{API}/databases/{DATABASE}", headers=headers)
        #print(response.json())
        response = requests.post(f"{API}/pages", headers=headers, json=new_page_data)

        print(f"Response: {response.status_code}, {response.text}")

	# check if it was added
        if response.status_code == 200:
             print(f"Successfully added assignment: {assignment['name']}")
        else:
             print(f"Failed to add assignment {assignment['name']} - {response.status_code}")
