#  dictionary  {}
# key-value pair
# key -> unique
# value -> can be duplicate
# heterogenonus
# indexing not allowed

# data = {}
# data = dict()
# print(type(data))

# data ={
#     "name":"raj",
#     "rollno":10101,
#     1012 : 200,
#     "course":["python","numpy","pandas"]
# }

# print(data.get("age","value does not exist"))
# print(data["age"])

# print(data.keys())
# print(data.values())
# print(data.items())

# print(len(data))
# print(max(data))
# print(min(data))

# to remove element from a dictionary
# data.pop("name")
# data.popitem()
# data.clear()
# del data



# to add key-value pair in dictionary
# data.setdefault("age",24)
# data.update({"age":12,"fees":50000})

# print(data["name"])
# print(data["course"])


# to add key-value pair in dictionary
# variable_name[key] = value
# data["age"]=24        # new key value pair add    
# data[1012] += 300     # update value
# data["name"] = "rahul"   #  override value



# count the frequency of an element in a list
# li = [1,2,1,2,1,2,2]
# 1:3   2:4

li = [1,1,2,1]
data = {}
print(data)

data[li[0]] = data.get(li[0],0)+1
print(data)

data[li[1]] = data.get(li[1],0)+1
print(data)

data[li[2]] = data.get(li[2],0)+1
print(data)

data[li[3]] = data.get(li[3],0)+1
print(data)