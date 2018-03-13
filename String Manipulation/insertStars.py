"""
Given a string, recursively compute a new string
where identical, adjacent characters
get separated with a "*".

Example:
insert_star_between_pairs("cac") ==> "cac"

insert_star_between_pairs("cc") ==> "c*c"
"""

def insert_star_between_pairs(a_string):
    if not a_string:
        return None
    chars_list = list(a_string)
    ret = str(chars_list[0])
    for i in range(1, len(chars_list)):
        if chars_list[i] == chars_list[i-1]:
            ret +=  "*" + chars_list[i]
        else:
            ret += chars_list[i]
    return ret