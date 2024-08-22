import requests

# Check if directory exists
def check_dir(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError: 
        pass

dirs_file = open("dirs.txt", "r")
# Change the IP to own Meta2 IP as necessary here!
target = 'http://10.0.2.6/mutillidae'

for line in dirs_file:
    word=line.strip() 
    url = target+"/"+word
    
    if check_dir(url):
        print(url)

print("\n============= END =============")