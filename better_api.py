def sting_len(input_string):
    #
    return len(input_string)
#end

def string_type(input_string):
    if type(input_string) == int:
        type_string = "int"
    elif type(input_string) == float:
        type_string = "float"
    elif type(input_string) == str:
        type_string = "string"
    elif type(input_string) == bool:
        type_string = "bool"
    #end
    return type_string
#end

def string_type_lower(input_string):
    #
    return input_string.lower()
#end

def string_type_up(input_string):
    #
    return input_string.upper()
#end

def string_delete_choosen(input_string, str_to_delete):
    return input_string.strip(str_to_delete)
#end

def string_index_number(input_string):
    #
    return ord(input_string)
#end

def number_index_string(input_int):
    #
    return chr(input_int)
#end

def string_first_letter_big(input_string):
    #
    return input_string.capitalize()
#end

def string_place_center(input_string, input_int):
    #
    return input_string.center(input_int)
#end

def int_hezka(input_int, input_hezka):
    #
    return pow(input_int, input_hezka)
#end

def string_count(input_string, string_count_str):
    return input_string.count(string_count_str)
#end
def string_count_custom(input_string, string_count_str, str_start, str_end):
    #
    return input_string.count(string_count_str, str_start, str_end)
#end
def int_round(input_int, round_start):
    if round_start == 0:
        #
        rounded_int = round(input_int)
    else:
        #
        rounded_int = round(input_int, round_start)
    #end
    return rounded_int
#end

def string_find(input_string, string_to_find):
    #
    return input_string.find(string_to_find)
    #return in error "-1"
#end

def string_index(input_string, string_to_find):
    #
    return input_string.index(string_to_find)
    #return in error "valueError"
#end

def string_replace(input_string, string_to_replace):
    return input_string.replace(string_to_replace)
#end

def string_calc(input_string):
    #
    return eval(input_string)
#end

def table_inset(insert_type, table_to_inset):
    #
    return table_to_inset.insert(sting_len(table_to_inset), insert_type)
#end

def table_extand(insert_type, table_to_inset):  #inset no metter what next to already values in the table
    return table_to_inset.extend(insert_type)
#end

def table_remove(remove_type, table_to_remove):
    #
    return table_to_remove.remove(remove_type)
#end

def table_sort(table_to_sort):
    #
    return table_to_sort.sort()
#end

def math_round_positive(intput_int):
    return abs(intput_int)
#end

def math_min(table_to_min):
    return min(table_to_min)
#end

def math_max(table_to_max):
    return max(table_to_max)
#end

def table_sum(table_to_sum):
    return sum(table_to_sum)
#end

def to_string(input_tostring):
    #
    if string_type(input_tostring) != "string":
        return "invalid input"
    else:
        return str(input_tostring)
    #end
#end

def to_int(input_toint):
    if string_type(input_toint) != "int":
        return "invalid input"
    else:
        return int(input_toint)
    #end
#end

def to_float(input_tofloat):
    #
    if string_type(input_tofloat) != "float":
        return "invalid input"
    else:
        return float(input_tofloat)
    #end
#end

def user_input(string_to_show, typemode):
    #
    typemode(input(string_to_show))
#end
