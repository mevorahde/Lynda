# 
# Example file for parsing and processing JSON
#
import urllib.request
import json


def print_results(data):
    # Use the json module to load the string data into a dictionary
    the_json = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    count = the_json["metadata"]["count"];
    print("{} events recorded\n".format(count))

    # for each event, print the place where it occurred
    # print("--------------")
    # for i in the_json["features"]:
    #     print(i["properties"]["place"])
    # print("--------------\n")

    # print the events that only have a magnitude greater than 4
    # print("--------------")
    # print("Events that were greater than 4: \n")
    # for i in the_json["features"]:
    #     if i["properties"]["mag"] >= 4.0:
    #         print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    # print("--------------\n")

    # print only the events where at least 1 person reported feeling something
    print("--------------")
    print("Events that were felt: \n")
    for i in the_json["features"]:
        felt_reports = i["properties"]["felt"]
        if felt_reports is not None:
            if felt_reports > 0:
                print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported "
                       + str(felt_reports) + "times")
    print("--------------\n")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    url_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    web_url = urllib.request.urlopen(url_data)
    print("result code: " + str(web_url.getcode()))
    if web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print_results("Received error, cannot parse results")


if __name__ == "__main__":
    main()
