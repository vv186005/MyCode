import requests

def validate_and_standardize_address(address, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK' and len(data['results']) > 0:
        standardized_address = data['results'][0]['formatted_address']
        return standardized_address
    else:
        return None

# Example usage
#address = '1600 Amphitheatre Parkway, Mountain View, CA'
#address = '8190 N STONY PK RD , JACKSON MI, 49201'
address = '1701 LAKE LANSING RDSTE 100, LANSING, MI, 48912'
api_key = 'AIzaSyDx1NN9h6uTx1VSm1sKAUJ5lMf7ggthtuM'
standardized_address = validate_and_standardize_address(address, api_key)

if standardized_address:
    print(f"Standardized Address: {standardized_address}")
else:
    print("Address validation failed or no standardized address found.")