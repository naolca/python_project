# This code is intended to manage our contacts. It can save, search and also delete a contact. To make the implemetation efficient we used a hashmap data structure. Which makes the code execute the save, search operations in constant time.
class contactManager:

    # Create empty container list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_containers()

    def create_containers(self):
        return [[] for _ in range(self.size)]

    # Insert a number into contacts
    def saveContact(self, name, contactNumber):

        # Get the index from the name
        # using hash function
        hashed_key = hash(name) % self.size

        # Get the container corresponding to index
        container = self.hash_table[hashed_key]

        found_name = False
        for index, record in enumerate(container):
            record_name, record_val = record

            # check if the container has same name as
            # the name to be inserted
            if record_name == name:
                found_name = True
                break

        # If the container has same name as the name to be inserted,
        # Update the name and  phone number
        # Otherwise append the new name and contact number pair to the bucket
        if found_name:
            container[index] = (name, contactNumber)
        else:
            container.append((name, contactNumber))

    # Return contactnumber with specific name
    def SearchNumber(self, name):

        # Get the index from the name using
        # hash function
        hashed_key = hash(name) % self.size

        # Get the container corresponding to index
        container = self.hash_table[hashed_key]

        found_name = False
        for index, record in enumerate(container):
            name, contactNumber = record

            # check if the container has same key as
            # the key being searched
            if name == name:
                found_name = True
                break

        # If the container has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no contact found
        if found_name:
            return contactNumber
        else:
            return "No contact  found"

    # Remove a contact using the name
    def removeContact(self, name):

        # Get the index from the name using
        # hash function
        hashed_key = hash(name) % self.size

        # Get the container corresponding to index
        container = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(container):
            name, contactNumber = record

            # check if the bucket has same key as
            # the key to be deleted
            if name == name:
                found_key = True
                break
        if found_key:
            container.pop(index)
        return
        
    def displayContacts(self):
         """
        Retrieve all the contacts and their contact numbers stored in the contact manager.
        
        Returns:
        List: A list of tuples containing the contact name and their respective contact number.
        """
        contacts = []
        for container in self.hash_table:
            for record in container:
                name, contactNumber = record
                contacts.append((name, contactNumber))
        return contacts
