# Define sample data for each data type
sample_list = [1, 2, 3, 4, 5]
sample_tuple = (6, 7, 8, 9, 10)
sample_set = {11, 12, 13, 14, 15}
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Comparing List and Tuple
if len(sample_list) == len(sample_tuple):
    print("List and Tuple have the same length.")
else:
    print("List and Tuple have different lengths.")

if sample_list == list(sample_tuple):
    print("List and Tuple have the same elements.")
else:
    print("List and Tuple have different elements.")

# Comparing List and Set
if len(sample_list) == len(sample_set):
    print("List and Set have the same length.")
else:
    print("List and Set have different lengths.")

if set(sample_list) == sample_set:
    print("List and Set have the same elements.")
else:
    print("List and Set have different elements.")

# Comparing List and Dictionary
if len(sample_list) == len(sample_dict):
    print("List and Dictionary have the same length.")
else:
    print("List and Dictionary have different lengths.")

if set(sample_list) == set(sample_dict.values()):
    print("List and Dictionary have the same elements.")
else:
    print("List and Dictionary have different elements.")

# Comparing Tuple and Set
if len(sample_tuple) == len(sample_set):
    print("Tuple and Set have the same length.")
else:
    print("Tuple and Set have different lengths.")

if set(sample_tuple) == sample_set:
    print("Tuple and Set have the same elements.")
else:
    print("Tuple and Set have different elements.")

# Comparing Tuple and Dictionary
if len(sample_tuple) == len(sample_dict):
    print("Tuple and Dictionary have the same length.")
else:
    print("Tuple and Dictionary have different lengths.")

if set(sample_tuple) == set(sample_dict.values()):
    print("Tuple and Dictionary have the same elements.")
else:
    print("Tuple and Dictionary have different elements.")

# Comparing Set and Dictionary
if len(sample_set) == len(sample_dict):
    print("Set and Dictionary have the same length.")
else:
    print("Set and Dictionary have different lengths.")

if set(sample_set) == set(sample_dict.values()):
    print("Set and Dictionary have the same elements.")
else:
    print("Set and Dictionary have different elements.")