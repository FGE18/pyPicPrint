"""
Picture module
This module contains functions to manage picture.
"""
# APP Import


class Picture:

    def __init__(self, height=1, width=1):
        self.height = height
        self.width = width

    def get_optimal_print_height(self, definition, unit):
        """This function compute optimal height print for image using definition value entered as parameter.
        Parameter: definition -- Integer definition for print in DPI.
        Parameter: unit -- String CM / IN for centimeters or inches
        Returns: float Optimal height for print in defined unit rounded with 2 decimals.
        """
        ret_val = int(self.height) / int(definition)
        ret_val = ret_val if unit == "IN" else ret_val * 2.54
        return round(ret_val, 2)

    def get_optimal_print_width(self, definition, unit):
        """This function compute optimal width print for image using definition value entered as parameter.
        Parameter: definition -- Integer definition for print in DPI.
        Parameter: unit -- String CM / IN for centimeters or inches
        Returns: float Optimal width for print in defined unit rounded with 2 decimals.
        """
        ret_val = int(self.width) / int(definition)
        ret_val = ret_val if unit == "IN" else ret_val * 2.54
        return round(ret_val, 2)

    def get_resolution(self):
        """Not used"""
        return self.width * self.height

    def set_height(self, height):
        # Use property to ensure verification
        if isinstance(height, int) & height > 0:
            self.height = height

    def set_width(self, width):
        # Use property to ensure verification
        if isinstance(width, int) & width > 0:
            self.width = width
