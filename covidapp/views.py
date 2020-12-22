from django.shortcuts import render
import requests
import json



url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "105c7d62bdmsh954f200b73bdf9ep14bfc1jsnbbfa0d64ea7d",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def home(request):
	noofresults = int(response['results'])
	countrylist = []
	for x in range(noofresults):
		countrylist.append(response['response'][x]['country'])
	if request.method == "POST":
		selectedcountry = request.POST['selectedcountry']
		for x in range(0, noofresults):
			if selectedcountry == response['response'][x]['country']:
				new = response['response'][x]['cases']['new']
				active = response['response'][x]['cases']['active']
				critical = response['response'][x]['cases']['critical']
				recovered = response['response'][x]['cases']['recovered']
				total = response['response'][x]['cases']['total']
				deaths = int(total) - int(active) - int(recovered)
		context = {'selectedcountry' : selectedcountry, 'countrylist' : sorted(countrylist), 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'deaths' : deaths, 'total' : total}
		return render(request, 'home.html', context)
	
	context = {'countrylist' : sorted(countrylist)}
	return render(request, 'home.html', context)