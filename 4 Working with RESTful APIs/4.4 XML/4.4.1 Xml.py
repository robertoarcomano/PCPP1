"""
1 First line with version and format: <?xml version = "1.0" encoding = "utf-8"?>
2 Comment: <!-- cars.xml - List of cars ready to sell -->
3 Attributes: <price currency="USD">35900</price>
4 Document data type: <!DOCTYPE cars_for_sale SYSTEM "cars.dtd">
    4.1 FPI (Formal Public Identifier
    4.2 SYSTEM
    4.3 PUBLIC
5 Opening: <Name>, closing </Name> or short form for null objects <Name/>
6 You can repeat all objects but the first one
7 No datatypes
"""
import xml.etree.ElementTree
tree = xml.etree.ElementTree.parse('cars.xml')
cars_for_sale = tree.getroot()
def print_cars(xml):
    print(xml.tag)
    for car in xml.findall('car'):
        print('\t', car.tag)
        for prop in car:
            print('\t\t', prop.tag, end='')
            if prop.tag == 'price':
                print(prop.attrib, end='')
            print(' =', prop.text)

print_cars(cars_for_sale)
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')
print_cars(cars_for_sale)

