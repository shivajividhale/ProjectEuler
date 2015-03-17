import logging
import sys

__author__ = 'Shivaji'

try:
    content=23
    #content=content.strip()
    flag=True
    for char in content:
        if char.isdigit() == False:
            flag=False
            break
    if flag==False:
        content=content
    elif content.find(" ") == -1:
            content = "define "+content

    print(content)
except:
    logging.warning("Error", sys.exc_info()[0])

print("Hello")