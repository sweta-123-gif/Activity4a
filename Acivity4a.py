# Name: Sweta kc
# ISQA 3900 Web Application Development
# The Purpose of this program is create, modify and use the python list and also to create and use tuples.

# Names
names = ["maria", "maria", "will", "sam", "maria", "kahn", "sam", "barry", "george", "hank", "belinda", "maria",
         "karthik"]

# 2. Sorting the Name list
print("Initial List of Names:")
sort_list = names

sort_list.sort()
print(sort_list)


# 3. Calling the Name and return the value by removing the duplicates and afterwards again sorting the list.
def duplicatesRemover(sort_list):
    a = list(set(sort_list))
    return a


unique = duplicatesRemover(sort_list)
unique.sort()

# 4. Printing the output
print("\nList of Unique Names: ")
print(unique)
