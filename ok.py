# Hashing Program

hash_table = {}
elements = []

def hash_function(element):
  return element[0].lower(),element[0].upper()
  # hash function that returns the first character of the element in lowercase and uppercase....

def add(element):
  try:
    index = hash_function(element)
    if index in hash_table:
      hash_table[index].append(element)
    else:
      hash_table[index] = [element]
    elements.append(element)
  except Exception as e:
    print(f"Error adding element: {e}")

def retrieve(element):
  try:
    index = hash_function(element)
    if index in hash_table:
      return hash_table[index]
    else:
      return None
  except Exception as e:
    print(f"Error retrieving element: {e}")
def update(element, new_element):
  try:
    index = hash_function(element)
    if index in hash_table:
      for i, e in enumerate(hash_table[index]):
        if e == element:
          hash_table[index][i] = new_element
          elements[elements.index(element)] = new_element
          return
    print(f"Element {element} not found")
  except Exception as e:
    print(f"Error updating element: {e}")

def delete(element):
  try:
    index = hash_function(element)
    if index in hash_table:
      hash_table[index].remove(element)
      elements.remove(element)
    else:
      print(f"Element {element} not found")
  except Exception as e:
    print(f"Error deleting element: {e}")

def display():
  print("Hash Table:")
  for index, elements in hash_table.items():
    print(f"Index {index}: {elements}")

while True:
  print("\nOptions:")
  print("1. Add element")
  print("2. Retrieve element")
  print("3. Update element")
  print("4. Delete element")
  print("5. Display hash table")
  print("6. Exit")

  choice = input("Choose an option: ")

  if choice == "1":
    element = input("Enter element to add: ")
    add(element)
  elif choice == "2":
    element = input("Enter element to retrieve: ")
    retrieved_element = retrieve(element)
    if retrieved_element:
      print(f"Element {element} found at index {hash_table[hash_function(element)][0]}")
    else:
      print(f"Element {element} not found")
  elif choice == "3":
    element = input("Enter element to update: ")
    new_element = input("Enter new element: ")
    update(element, new_element)
  elif choice == "4":
    element = input("Enter element to delete: ")
    delete(element)
  elif choice == "5":
    display()
  elif choice == "6":
    print("Goodbye!")
    break
  else:
    print("Invalid option")
