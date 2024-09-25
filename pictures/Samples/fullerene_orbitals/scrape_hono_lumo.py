import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "http://physikmdb.uni-graz.at:5001/default/row/213"
def find_energy(label, element):
    tag = element.find('td', string=label)
    if tag:
        return tag.find_next_sibling('td').string.strip()
    return None
try:
    # Send a GET request to the page
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    fff = soup.find_all("table", {"class": "table-striped"})
    # # Extract the energies for HOMO and LUMO
    # homo_energy = soup.find(string='HOMO').find_next().text
    # lumo_energy = soup.find(string='LUMO').find_next().text

    # print(f"HOMO Energy: {homo_energy}")
    # print(f"LUMO Energy: {lumo_energy}")
    #print(fff)
    for i in fff:
        pup = i.find_all('td')
        for k in range(len(pup)): 
            if 'HOMO' in pup[k].text.strip():
                print(pup[k].text.strip(), pup[k+1].text.strip(), pup[k+2].text.strip())
            if 'LUMO' in pup[k].text.strip():
                print(pup[k].text.strip(), pup[k+1].text.strip(), pup[k+2].text.strip())

except requests.exceptions.RequestException as e:
    print(f"Error accessing the page: {e}")
except AttributeError:
    print("Error finding the required information on the page.")
