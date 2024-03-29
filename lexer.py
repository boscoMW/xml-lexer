"""
lexical analyzer for records of type car, of the following format

<car make="toyota" year="2009" model="corolla" transmission="automatic" >
<color body="red" rims="silver" interior="brown"/>
</car>

Note:remove newlines from input first
"""
import regex
import re

input_string = r'<car make="toyota" year="2009" model="corolla" transmission="automatic" ><color body="red" rims="silver" interior="brown"/></car>'

#extract cars
cars = re.findall(regex.car_entity_regex, input_string)
if len(cars):
    for car_entity in cars:
        opening_tag = re.search(regex.opening_tag, car_entity).group(1)# get opening tag
        print opening_tag
        car_attributes = re.findall(regex.car_attributes_regex, opening_tag)# extract attributes from opening tag
        if car_attributes:
            for attr in car_attributes:
                print [ attribute for attribute in attr if attribute][0].strip()
        #get color entity if it exists
        color_entity = re.search(regex.color_entity_regex, car_entity).group(1)# get color tag if it exists
        if color_entity:
            print color_entity
            color_attributes = re.findall(regex.color_attributes_regex, color_entity)# extract attributes from opening tag
            if color_attributes:
                for attr in color_attributes:
                    print [ attribute for attribute in attr if attribute][0].strip()
            

