from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        headers = {'X-Api-Key': 'API-Key'}
        
        # Make the API request
        try:
            api_request = requests.get(api_url + query, headers=headers)
            if api_request.status_code == 200:  # Check if request was successful
                api = json.loads(api_request.content)
                if not api:  # Handle if the response is empty
                    api = "No data found for this query."
            else:
                api = f"Error: Received status code {api_request.status_code}"
        except requests.exceptions.RequestException as e:
            api = f"Error: {str(e)}"

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
