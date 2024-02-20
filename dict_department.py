def get_person_info(persons_dict, key):
    """
    Function to fetch information of a person based on a key.
    
    Args:
    persons_dict (dict): Dictionary containing person information.
    key (str): Key to fetch a particular person's information.

    Returns:
    dict: Information of the person.
    """
    return persons_dict.get(key, "No person found with this key")

persons = {
    "person1": {"name": "Aakansh","sapID": "500123456", "department": "CSE"},
    "person2": {"name": "Rohit","sapID": "500543210", "department": "ECE"},
    "person3": {"name": "Charlie","sapID": "500221110", "department": "Business"},
    "person4": {"name": "David","sapID": "50056789", "department": "IT"},
    "person5": {"name": "Eve","sapID": "50045678", "department": "Finance"},
}

key = "person1"
print(get_person_info(persons, key))
