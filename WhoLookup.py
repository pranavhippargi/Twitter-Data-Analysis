import webbrowser
from bs4 import BeautifulSoup
import requests
import qt 


# Input name
enterName = input("Enter the name or alias of the individual: ")

#Get full link with alias
whoLink = "http://who/is/" + str(enterName)

#Open the link
webbrowser.open(whoLink)





# print(printF)

#TO-DO: 
# 1) Get HTML Attribute of the class: mainPerson2 and the subscripts, tags, ect 
# 2) Display in terminal. If successfull, create GUI with Tkinter
# 3) Display webscraped data into the GUI.

# # Unit Test to see if the BS4 displays HTML tags. 
#     source_code = requests.get('http://who/is/prhippar').text
#     soup = BeautifulSoup(source_code, "html.parser")
#     findTables = soup.find_all('div')
#     findTablesString = str(findTables)
#     print(findTablesString)

