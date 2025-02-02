# create a network() function that accepts a dictionary "servers" as a parameter
def network(servers):

    # initialize string variable to the "result"
    result = ""

    # iterate through "hostname" (key) and "IP address" (value) in the "servers" dictionaries.
    # use for loop with .items()
    for hostname, IP_address in servers.items():
        # A string identifying the hostname and IP address for each server is added to the "result" variable.
        # string .format() function is used to plug the hostnaem and IP_address variables into the designated {}
        # placeholders within the string
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"
    
    # return the "result" variable string
    return result

# Call the function with the dictionary
print(network({"<server-name1>":"<ip_address>", "<server-name2>":"<ip_address2>"}))

# to-do: make server dictionary a file input. 
# to-do: accept csv or txt