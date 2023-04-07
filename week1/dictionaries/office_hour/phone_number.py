# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # returns "(123) 456-7890"

# Don't forget the space after the closing parentheses! 


def convert_to_phone_format( num_list,foo=None):
    print(foo)
    area_code_list = list(map(str, num_list[:3]))
    area_code = "".join(area_code_list)
    print(area_code)
    mid = num_list[3:6]
    end = num_list[6:]
    # area_code_string = ""
    # mid_string = ""
    # end_string = ""
    
    # for num in area_code:
    #     area_code_string += str(num)
    # for num in mid:
    #     mid_string += str(num)
    # for num in end:
    #     end_string += str(num)
    
    # print(area_code_string)
    # print(mid_string)
    # print(end_string)
    # result = f"({area_code_string}) {mid_string} {end_string}"
    # print(result)
    # return result

convert_to_phone_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
convert_to_phone_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
convert_to_phone_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "Bar")