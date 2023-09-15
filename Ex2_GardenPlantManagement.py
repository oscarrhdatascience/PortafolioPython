"""
Description:
A system designed to manage plants in a botanical garden. Users can add plants, specify their species, common name, and area within the garden. Additionally, it allows tracking the age of the plant, the date it was added to the garden, and transferring plants between different areas.

Integrated Concepts:

    OOP
    Lists/ArrayList
    Search Functions
    Flow Control
    Date Manipulation
"""
from datetime import datetime

class Plant:
    def __init__(self, common_name, species, area, age):
        self.common_name = common_name
        self.species = species
        self.area = area
        self.date_added = datetime.now()
        self.age = age

    def set_area(self, area):
        self.area = area

class BotanicalGarden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def search_by_common_name(self, common_name):
        for plant in self.plants:
            if plant.common_name.lower() == common_name.lower():
                return plant
        return None

    def search_by_species(self, species):
        return [plant for plant in self.plants if plant.species.lower() == species.lower()]

    def plants_in_area(self, area):
        return [plant for plant in self.plants if plant.area.lower() == area.lower()]

    def transfer_plant(self, common_name, new_area):
        plant = self.search_by_common_name(common_name)
        if plant:
            plant.set_area(new_area)

# Testing the system can be done here
