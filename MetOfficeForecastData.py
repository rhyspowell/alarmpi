import json, urllib

def AllObservationData(url):
	observationData = json.load(urllib.urlopen(url))

	# Observation data key
	# G = Wind Gusts
	# T = Temperature
	# V = Visability
	# D = Wind Direction
	# S = Wind Speed
	# W = Weather Type
	# P = Pressure


	periods = observationData['SiteRep']['DV']['Location']['Period']
	observations = periods[len(periods)-1]['Rep']
	currentObservations = observations[len(observations)-1]
	try:
		observationGusts = currentObservations['G']
	except:
		observationGusts = 0
	try:
		observationTemperature = currentObservations['T']
	except:
		observationTemperature = "not reported"
	try:
		observationVisability = currentObservations['V']
	except:
		observationVisability = "not reported"
	try:
		observationWindDirection = currentObservations['D']
	except:
		observationWindDirection = "not reported"
	try:
		observationWindSpeed = currentObservations['S']
	except:
		observationWindSpeed = "not reported"
	try:
		observationWeatherType = currentObservations['W']
	except:
		observationWeatherType = "not reported"
	try:
		observationPressure = currentObservations['P']
	except:
		observationPressure = "not reported"

	return(observationGusts,observationTemperature,observationVisability,observationWindDirection,observationWindSpeed,observationWeatherType,observationPressure)