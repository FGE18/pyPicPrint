"""
Picture module
This module contains class to manage picture.
"""
# APP Import


class Picture:

    def __init__(self, i_height:int=1, i_width:int=1):
        self.height = i_height
        self.width = i_width

    def get_optimal_print_height(self, f_definition:int, f_unit:str)->float:
        """This function compute optimal height print for image using definition value entered as parameter.
        :Parameter: f_definition -- Integer definition for print in DPI.
        :Parameter: f_unit -- String CM / IN for centimeters or inches
        :Returns: float Optimal height for print in defined unit rounded with 2 decimals.
        """
        ret_val = int(self.height) / int(f_definition)
        ret_val = ret_val if f_unit == "IN" else ret_val * 2.54
        return round(ret_val, 2)

    def get_optimal_print_width(self, f_definition:int, f_unit:int)->float:
        """This function compute optimal width print for image using definition value entered as parameter.
        :Parameter: f_definition -- Integer definition for print in DPI.
        :Parameter: f_unit -- String CM / IN for centimeters or inches
        :Returns: float Optimal width for print in defined unit rounded with 2 decimals.
        """
        ret_val = int(self.width) / int(f_definition)
        ret_val = ret_val if f_unit == "IN" else ret_val * 2.54
        return round(ret_val, 2)

    def get_resolution(self):
        """Not used"""
        return self._width * self._height
    #
    # @property
    # def height(self):
    #     return self._height
    #
    # @height.setter
    # def height(self, value):
    #     # tester try conversion int (ValueError)
    #     if isinstance(value, int) and value > 0:
    #         self._height = value
    #     else:
    #         self._height = 1
    #
    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     # tester try conversion int (ValueError)
    #     if isinstance(value, int) and value > 0:
    #         self._width = value
    #     else:
    #         self._width = 1

# Debug
# if __name__ == '__main__':
#     img_ok = Picture(1024, 768)
#     img_nok = Picture("o", "o")
#     print(img_ok.height, img_nok.height)