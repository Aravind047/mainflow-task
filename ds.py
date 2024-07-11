def list_operations():
    fruits = ["apple", "banana", "cherry", "date"]
    print("Original list:", fruits)
    
   
    fruits.append("elderberry")
    print("List after adding an element:", fruits)
    
    
    fruits.remove("banana")
    print("List after removing an element:", fruits)
    
    
    print("Element at index 2:", fruits[2])
    
    
    print("Sliced list (first 3 elements):", fruits[:3])


def dictionary_operations():
    student = {
        "name": "John Doe",
        "age": 21,
        "major": "Computer Science"
    }
    print("Original dictionary:", student)
    
   
    student["grade"] = "A"
    print("Dictionary after adding a key-value pair:", student)
    
   
    student.pop("age")
    print("Dictionary after removing a key-value pair:", student)
    
   
    print("Value for key 'name':", student["name"])
    
    
    print("Iterating over dictionary:")
    for key, value in student.items():
        print(key, ":", value)


def tuple_operations():
    colors = ("red", "green", "blue", "yellow")
    print("Original tuple:", colors)
    
   
    print("Element at index 1:", colors[1])
    
    
    print("Sliced tuple (last 2 elements):", colors[-2:])
    
    
    more_colors = ("purple", "orange")
    combined_colors = colors + more_colors
    print("Combined tuple:", combined_colors)


if __name__ == "__main__":
    print("List Operations")
    list_operations()
    
    print("\nDictionary Operations")
    dictionary_operations()
    
    print("\nTuple Operations")
    tuple_operations()