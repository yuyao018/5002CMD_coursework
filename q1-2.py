import random

# List of valid birth place (BP) codes for Malaysian ICs
valid_bp = [
    "01", "21", "22", "23", "24",     # Johor
    "02", "25", "26", "27",           # Kedah
    "03", "28", "29",                 # Kelantan
    "04", "30",                       # Malacca
    "05", "31",                       # Negeri Sembilan
    "06", "32", "33",                 # Pahang
    "07", "34", "35",                 # Penang
    "08", "36", "37", "38", "39",     # Perak
    "09", "40",                       # Perlis
    "10", "41", "42", "43", "44",     # Selangor
    "11", "45", "46",                 # Terengganu
    "12", "47", "48", "49",           # Sabah
    "13", "50", "51", "52", "53",     # Sarawak
    "14", "54", "55", "56", "57",     # WP Kuala Lumpur
    "15", "58",                       # WP Labuan
    "16",                             # WP Putrajaya
]

def generate_ic():
    # function to randomly generate a Malaysian IC number

    year = random.randint(1900, 2025) # Random year
    ic_year = str(year)[-2:]          # Get last two digits of the year
    month = random.randint(1, 12)     # Random month

    # Adjust day based on the month
    if month == 2:
        max_day_of_month = 29
    elif month in [4, 6, 9, 11]:
        max_day_of_month = 30
    else:
        max_day_of_month = 31

    day = random.randint(1, max_day_of_month) # Random day

    bp = random.choice(valid_bp) # Random valid birth place code
    serial = random.randint(0, 9999) # Random 4-digit serial number

    # Return 12-digit IC number in correct format
    return f"{ic_year}{str(month).zfill(2)}{str(day).zfill(2)}{bp}{str(serial).zfill(4)}"

def hash_function(ic, table_size):
    # Function to calculate hash value and return a hash index

    # Check if the IC number is 12 digits and contains only numeric characters
    if len(ic) != 12 or not ic.isdigit():
        print("Invalid Malaysian IC number")
        return None
    else:
        # folding technique
        # split the IC number into groups of 3 digits each
        groups = [ic[i:i+3] for i in range(0, 12, 3)]

        # initialize the group_sum to 0
        group_sum = 0

        # loop through the number to sum it up
        for group in groups:
            group_sum += int(group) # convert to integer and sum it up

    # return the hash index of the hash value by dividing the table size
    return group_sum % table_size

def insert_hash_table(ic, hash_table, table_size):
    # function to insert IC number into hash table with separate chaining

    # get the hash index by calling the hash function
    index = hash_function(ic, table_size)

    if index not in hash_table:
        hash_table[index] = [] # create a new list (chain) if not exists
    hash_table[index].append(ic) # append the IC number to chain at the hash index

def get_max_chain_length(hash_table):
    # function to get the length of the longest chain in the hash table

    # initialize the max_length to 0
    max_length = 0

    # loop through each hash index in the table to go through each chain
    for chain in hash_table.values():

        # if the length of the current chain is longer than the max length, store the value
        if len(chain) > max_length:
            max_length = len(chain)

    # return the value of max_length
    return max_length

def main():
    table_size_1 = 1009 # the first table size is initialize to 1009
    table_size_2 = 2003 # the second table size is initialize to 2003

    num_of_rounds = 10 # initialize the number of test rounds
    print(f"Running for {num_of_rounds} rounds")

    # perform hashing and collosion testing for each round
    for round in range(1, num_of_rounds + 1):
        print(f"----------------------Round {round}----------------------")
        hash_table_1 = {} # Initialize first hash table
        hash_table_2 = {} # Initialize second hash table

        # generate 1000 random IC numbers and insert into both hash tables
        for i in range(1000):
            ic_number = generate_ic()
            insert_hash_table(ic_number, hash_table_1, table_size_1)
            insert_hash_table(ic_number, hash_table_2, table_size_2)

        # get the maximum chain length of each table
        max_chain_length_1 = get_max_chain_length(hash_table_1)
        max_chain_length_2 = get_max_chain_length(hash_table_2)

        # Display the result
        print(f"Hash Table 1 (size {table_size_1}): Maximum chain length = {max_chain_length_1}")
        print(f"Hash Table 2 (size {table_size_2}): Maximum chain length = {max_chain_length_2}\n")

    print("---END---")

if __name__ == "__main__":
    main()