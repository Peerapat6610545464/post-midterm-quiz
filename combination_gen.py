import copy
import data_processing


def gen_comb_list(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list


# print("Test gen_comb_list")
# x = [1, 2, 3]
# y = [4, 5]
# z = [6, 7, 8]
# u = [9, 10]
# comb_list = gen_comb_list([x])
# print(comb_list, len(comb_list), [x])
# comb_list = gen_comb_list([x, y])
# print(comb_list, len(comb_list), [x, y])
# comb_list = gen_comb_list([x, y, z])
# print(comb_list, len(comb_list), [x, y, z])
my_table = data_processing.Table('movie', "fantasy")
my_DB = data_processing.DB()
my_DB.insert(my_table)
fantasy = my_DB.search("movie")
count = 0
for v in fantasy.value():
    if v == "fantasy":
        count += 1
print(count)
print(fantasy)
dict1 = {}
dict1['Film'] = 'The Shape of Water'
dict1['Genre'] = 'Fantasy'
dict1['Lead Studio'] = 'Fox'
dict1['Audience score %'] = '72'
dict1['Profitability'] = '9.765'
dict1['Rotten Tomatoes %'] = '92'
dict1['Worldwide Gross'] = '195.3'
dict1['Year'] = '2017'
print(dict1)
my_table.insert_row(my_DB, dict1)
count = 0
for v in fantasy.value():
    if v == "fantasy":
        count += 1
print(count)
fantasy = my_DB.search("movie")
my_table.update_row('Year', 'A Serious Man', 'Film', '2022')

#
# class Candidate():
#     def __init__(self, name, age, followers=0, genre="unknown",status=1):
#         if not isinstance(name, str):
#             raise TypeError
#         if name.isspace() or name == "":
#             raise ValueError
#         if not isinstance(age, int):
#             raise TypeError
#         if genre.isspace():
#             raise ValueError
#         if age < 0 and followers < 0:
#             raise ValueError
#         if status != "new" and status != "qualified" and status != status != "accepted" and status != "rejected":
#             raise ValueError
#         self.__name = name
#         self.__age = age
#         self.__followers = followers
#         self.__genre = genre
#         self.__status = status
#
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def followers(self):
#         return self.__followers
#     @property
#     def genre(self):
#         return self.__genre
#     @property
#     def status(self):
#         return self.__status
#
#
# candidate1 = Candidate("Kenny",18,2000,"dog game","new")
# print(f"Candidate {candidate1.name}, {candidate1.age}, {candidate1.followers}, {candidate1.genre}, ({candidate1.status})")
