''' Write a Python class to convert an integer to a Roman numeral '''
class IntToRoman:
  def __init__(self):
      self.roman_map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 1: 'I'}

  def convert(self, num):
    roman_numeral = ""
    for value, symbol in self.roman_map.items():
      roman_numeral += symbol * (num // value)  # Use integer division for repetitions
      num %= value  # Update remaining value after division
    return roman_numeral

converter = IntToRoman()
print(converter.convert(3549))  # Output: MMMDXLIX