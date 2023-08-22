import requests
import openpyxl
import Flask

URL = "https://jsonplaceholder.typicode.com/users"

# Get user input for username
print("Search by Username: ")
user = input("> ")
queryURL = URL + f"?username={user}"
response = requests.get(queryURL)

# Parse the JSON response
user_data = response.json()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write header row
header = ["ID", "Name", "Username", "Email", "Phone", "Website"]
sheet.append(header)

# Write user data to the Excel sheet
for user in user_data:
    row = [user["id"], user["name"], user["username"], user["email"], user["phone"], user["website"]]
    sheet.append(row)

# Save the Excel workbook
excel_file_path = "sampleuset.xlsx"
workbook.save(excel_file_path)

print(f"User information for user successfully saved to thing")
