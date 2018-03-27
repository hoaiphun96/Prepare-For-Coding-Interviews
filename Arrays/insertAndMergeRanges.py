"""
Given a sorted list of integer ranges (see Range in Use Me) and a new range as inputs, insert the new range at the correct position and merge all overlapping ranges.

Note: Check out the Use Me section to get the structure of the Range class.

Example:
Input  : [[1,10], [5,8], [8,15]]
New range : [9,20]
Output : [[1,20]]
"""
#Approach 1:
def insert_and_merge(input_range_list, new_range):
   position = find_insert_position(input_range_list, new_range)
   if position == len(input_range_list):
       input_range_list.append(new_range)
   else:
       input_range_list = input_range_list[:position] + [new_range] + input_range_list[position:]
   return merge_ranges(input_range_list)


def find_insert_position(input_range_list, new_range):
   left, right = 0, len(input_range_list) - 1

   while left <= right:
       middle = (left + right) // 2
       if input_range_list[middle].lower_bound > new_range.lower_bound:
           right = middle - 1
       elif input_range_list[middle].lower_bound < new_range.lower_bound:
           left = middle + 1
       else:
           return middle + 1
   return left


def merge_ranges(input_range_list):
   ret = [input_range_list[0]]
   for index in range(1, len(input_range_list)):
       if input_range_list[index].lower_bound <= ret[-1].upper_bound:
           ret[-1].upper_bound = max(ret[-1].upper_bound, input_range_list[index].upper_bound)
       else:
           ret.append(input_range_list[index])
   return ret

#Approach 2
def insert_and_merge(input_range_list, new_range):
   # Insert Range
   insert_list = []
   for range in input_range_list:
       if range.upper_bound < new_range.lower_bound:
           insert_list.append(range)
       else:
           if range.lower_bound > new_range.upper_bound:
               insert_list.append(new_range)
               new_range = range
           else:
               if range.upper_bound >= new_range.lower_bound or range.lower_bound <= newRange.upper_bound:
                   new_range = Range(min(range.lower_bound, new_range.lower_bound),
                                     max(new_range.upper_bound, range.upper_bound))

   insert_list.append(new_range)

   # Merge ranges
   output_list = []
   previous = insert_list[0]
   i = 1
   while i < len(insert_list):
       current = insert_list[i]
       if (previous.upper_bound >= current.lower_bound):
           merged = Range(previous.lower_bound, max(previous.upper_bound, current.upper_bound));
           previous = merged
       else:
           output_list.append(previous)
           previous = current
       i = i + 1

   output_list.append(previous)
   return output_list
