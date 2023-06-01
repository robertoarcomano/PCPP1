"""
1 Modules
    1.1 xml.etree.ElementTree
    1.2 xml.dom.minidom
    1.3 xml.sax
2 Xml Elements:
    2.1 prolog <?xml version="1.0" encoding="ISO-8859-2"?>
    2.2 root element <data>
    2.3 elements <book>
    2.4 attributes title
3 ElementTree class
    3.1 parse to loads xml from a file
    3.2 fromstring loads xml from a string
    3.3 tag shows its tag name
    3.4 attrib shows all attributes (dictionary)
    3.5 objects contains arrays of their children
    3.6 iter to look for a specific tag
    3.7 findall to look for a specific tag at the 1st level
    3.8 find to look for the first child of the findall
    3.9 edit: tag=new_value
    3.10 remove: specify the object
    3.11 set a tag
    3.12 remove attribute: del attrib[attr_name] or attrib.pop(attr_name)
    3.13 write(FILE_NAME, FORMAT, HEADER)
    3.15 New document:
        3.15.1 ET.Element to create a new element
        3.15.2 ET.dump to show all the document
        3.15.3 ET.SubElement to create children
"""
import xml.etree.ElementTree as ET


def show_xml(xml):
    for i in range(0, len(xml)):
        print(xml[i].tag, xml[i].attrib)
        for j in range(0, len(xml[i])):
            print(" ", xml[i][j].tag)
            print("   ", xml[i][j].text)
    print()


tree = ET.parse("example.xml")
root = tree.getroot()
show_xml(root)

# Look for a tag
print("iter looks for a specific tag, i.e. year")
for year in root.iter("year"):
    print(year.text)
print()

# Look for a tag at the first level
print("iter looks for a specific tag at the first level, i.e. book")
for book in root.findall("book"):
    print(book.tag + ": title: " + book.get("title"))
print()

# Look for the first tag at the first level
print("iter looks for the first specific tag at the first level, i.e. book")
print("title:", root.find("book").get("title"))

print()
print("Editing")
for book in root:
    book.tag = "movie"
show_xml(root)

print("Removing")
for book in root:
    book.remove(book.find("author"))
show_xml(root)

print("Set")
for book in root:
    book.set("name", book.get("title"))
    book.set("title", "my_title")
    book.set("title1", "my_title")
    del book.attrib["title"]
    book.attrib.pop("title1")
show_xml(root)

# Saving
tree.write("example1.xml", "UTF-8", True)

# New document
print("New document")
element = ET.Element("Laptop")
ET.SubElement(element, "component", {'name': 'video_card', 'value': "ATI"})
ET.dump(element)

# Save the new document
new_root = ET.ElementTree(element)
new_root.write("example2.xml", "UTF-8", True)

