
"""
We're sure you've used Microsoft Excel or Google Sheets at some point. Given a column name of the spreadsheet, return the corresponding column number.

Note: Column name "A" corresponds to column number 1

Examples:
Input  : A
Output : 1

Input  : AA
Output : 27

"""

#approach 1
def excel_column_name_to_number(column_title):
    output = 0
    for index in range(len(column_title)):
        output = output * 26
        output = output + ord(column_title[index]) - ord('A') + 1
    return output

#approach 2
def excel_column_name_to_number(column_title):
    column_title = list(column_title)
    ret = 0
    for i, char in enumerate(column_title):
        char_ind = ord(column_title[i]) - ord('A') + 1
        x = 26**(len(column_title)-1-i)
        ret += char_ind*x
    return ret