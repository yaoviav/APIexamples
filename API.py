import requests
#pip3 install requests 
import openpyxl


URL = " https://jsonplaceholder.typicode.com/users"

#code to search by Username based on username element in JSON file 
print("Search by Username: ")
user = input("> ")
queryURL = URL + f"?username={user}"
response = requests.get(queryURL)


print(response.text) 
#To run the code you need to to do python3 API.py



#install Flask 
#pip3 installFlask

Brew Documentation
#https://docs.brew.sh

List all directory things 
#ls -l




# # Read content from the text file
# text_file_path = response.text
# with open(text_file_path, "r") as file:
#     text_content = file.read()

# # Create a new Excel workbook
# workbook = openpyxl.Workbook()
# sheet = workbook.active

# # Write text content to the Excel sheet
# sheet.cell(row=1, column=1, value=text_content)

# # Save the Excel workbook
# excel_file_path = "example1.xlsx"
# workbook.save(excel_file_path)

# print("Text file content successfully converted to Excel.")
