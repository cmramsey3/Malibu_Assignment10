# dataProcessing.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant
# to-do in this module
# Create a class that intakes a dictionary that is created by API_load class in API.py and extract some interesting 
# data and print a friendly message with it to the console.

class dataProcessing:
    """
    Processes JSON data returned from the API and prepares it for use or CSV export.
    """

    def __init__(self, json_data):
        self.data = json_data

    def extract_bracket_data(self):
        """
        Extracts income tax brackets from the JSON into a list of dictionaries.

        @return list[dict]: Each dict contains 'income' and 'rate' keys.
        """
        bracket_data = []

        brackets = self.data["federal"]["married"]["brackets"]
        for bracket in brackets:
            bracket_data.append({
                "min": bracket.get("min", "N/A"),
                "max": bracket.get("max", "N/A"),
                "rate": bracket.get("rate", "N/A")
            })

        return bracket_data
