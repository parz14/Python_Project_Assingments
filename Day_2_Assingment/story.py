import re

File = open("story.txt")  # Open a text file
file_text = File.read()  # Read the content in the text file
if re.search("middle", file_text):  # search a pattern in the text file
    print("Pattern found in the text file")
else:
    print("Pattern not found in the text file")
x = re.findall(r'middle', file_text)  # Find pattern in the text file
print("findall --> ", x)
x = re.search(r'Rikk', file_text, re.M | re.I)  # Search a pattern ignoring multiline and case
print("search --> ", x)
x = re.match(r'middle', file_text)  # match a pattern with text file
print("match --> ", x)
File.close()  # Close the text file
