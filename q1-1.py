def ic_hash(ic):
    # This function returns a hash value for a Malaysian IC number using the folding technique

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

    # return the final hash value
    return group_sum

def main():
    # prompt user to enter an IC number and store in ic_number variable
    ic_number = str(input("Enter your IC number: "))

    # call the hashing function
    hashed_ic = ic_hash(ic_number)

    # check if the hash was successfully computed and display the result
    if hashed_ic is not None:
        print("The hash value of the IC number is:", hashed_ic)
    else:
        print("Error in hashing the IC number")

# run the main function if the script is executed directly
if __name__ == "__main__":
    main()