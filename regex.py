import re

car_attributes_regex = re.compile(r'(\s?transmission="\w+"\s?)|(\s?make="\w+"\s?)|(\s?model="\w+"\s?)|(\s?year="\d{4}"\s?)|(\s?horsepower="\d{1,3}"\s?)|(\s?top_speed="\d{1-5}\w+"\s?)')
color_attributes_regex = re.compile(r'(\s?body="\w+"\s?)|(\s?rims="\w+"\s?)|(\s?interior="\w+"\s?)')
car_entity_regex = re.compile(r'<car.*</car>')
color_entity_regex = re.compile(r'(<color\s?(\s?\w+="\w+"\s?)*/>)')
opening_tag = re.compile(r'(<car\s?(\s?\w+="\w+"\s?)*>)')
closing_tag = re.compile(r'</car>')
