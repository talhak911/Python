from typing import Union
key = Union[str,int]
value = Union[str,int,set,list, dict, tuple]
data: dict[key,value] = {"name":"Talha"
                         , "fname":"sadiq",
                         "Hobby":{1:"cricket",2:"gardening"}
                         }

print(data["Hobby"][2])