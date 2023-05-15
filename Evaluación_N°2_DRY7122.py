import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
clave = "ZxriPEOhM5qXGQzpjoHt92aevmj4Vwwn"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": clave, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        distance_km = round(json_data["route"]["distance"] * 1.61, 2)
        print("Kilometers: " + str(distance_km))
        distance_miles = round(json_data["route"]["distance"], 2)
        print("Miles: " + str(distance_miles))

        if "fuelUsed" in json_data["route"]:
            fuel_used_gal = json_data["route"]["fuelUsed"]
            fuel_used_ltr = round(fuel_used_gal * 3.78, 2)
            print("Fuel Used (Gal): " + str(fuel_used_gal))
            print("Fuel Used (Ltr): " + str(fuel_used_ltr))
        else:
            print("Fuel Used: Not Available")

        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_km = round(each["distance"] * 1.61, 2)
            print(((each["narrative"]) + " (" + str(distance_km) + " km)"))

        print("=====================================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
