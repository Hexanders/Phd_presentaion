import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "http://physikmdb.uni-graz.at:5001/default/row/213"

# Send a GET request to the page
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Function to find energy values based on label
def find_energy(label):
    tag = soup.find('td', string=label)
    if tag:
        return tag.find_next_sibling('td').string.strip()
    return None

# Extract HOMO and LUMO energies
homo_energy = find_energy('HOMO')
lumo_energy = find_energy('LUMO')

print(f"HOMO Energy: {homo_energy}")
print(f"LUMO Energy: {lumo_energy}")
