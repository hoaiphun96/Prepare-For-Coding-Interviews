"""
We're sure you've used Microsoft Excel or Google Sheets at some point.
Given a column number of a spreadsheet, find it's corresponding column name.

Note: "1" denotes column Name "A"

Examples:
Input  : 2
Output : B

Input  : 27
Output : AA

Input  : 52
Output : AZ

Input  : 731
Output : ABC
"""
# Necessary modules have already been imported.
def excel_column_number_to_name(column_number):
    if column_number <= 26:
        return chr(column_number - 1 + ord('a')).upper()
    index = (column_number -1 ) % 26
    return excel_column_number_to_name(( column_number - index) / 26) + chr(index + ord('a')).upper()