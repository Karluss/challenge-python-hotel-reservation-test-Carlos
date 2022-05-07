
class Lakewood:
    name = "Lakewood"
    classification = 3
    weekRegular= 110
    weekReward = 80
    weekendRegular= 90
    weekendReward = 80

class Bridgewood:
    name = "Bridgewood"
    classification = 4
    weekRegular= 160
    weekReward = 110
    weekendRegular = 60
    weekendReward = 50

class Ridgewood:
    name = "Ridgewood"
    classification = 5
    weekRegular = 220
    weekReward = 100
    weekendRegular = 150
    weekendReward  = 40

hotelLakewood = Lakewood()
hotelBridgewood = Bridgewood()
hotelRidgewood = Ridgewood()

def isReward(client):
    if client == "Regular:":
        return "Regular"
    elif client == "Reward:":
        return "Reward"

def getDay(date):
    day = date[date.find("(")+1:date.find(")")]
    return day

def getHighestClassification(hotel1,hotel2):
    if hotel1.classification > hotel2.classification:
        return hotel1
    else:
        return hotel2

def isWeekDay(day):
    if (day == "mon") or (day == "tues") or (day == "wed") or (day == "thur") or (day == "fri"):
        return True
    else:
        return False
        
def getHotel(client, dates):
    lowestPriceHotel = " "
    for i in range(len(dates)):
        if client == "Regular":
            if (isWeekDay(dates[i])):
                lowestPriceHotel = hotelLakewood
                if (lowestPriceHotel.weekRegular >= hotelBridgewood.weekRegular):
                    if lowestPriceHotel.weekRegular == hotelBridgewood.weekRegular:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelBridgewood)
                    elif lowestPriceHotel.weekRegular > hotelBridgewood.weekRegular:
                        lowestPriceHotel = hotelBridgewood
                if (lowestPriceHotel.weekRegular >= hotelRidgewood.weekRegular):
                    if lowestPriceHotel.weekRegular == hotelRidgewood.weekRegular:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelRidgewood)
                    elif lowestPriceHotel.weekRegular > hotelRidgewood.weekRegular:
                        lowestPriceHotel = hotelRidgewood
            else:
                lowestPriceHotel = hotelLakewood
                if (lowestPriceHotel.weekendRegular >= hotelBridgewood.weekendRegular):
                    if lowestPriceHotel.weekendRegular == hotelBridgewood.weekendRegular:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelBridgewood)
                    elif lowestPriceHotel.weekendRegular > hotelBridgewood.weekendRegular:
                        lowestPriceHotel = hotelBridgewood
                if (lowestPriceHotel.weekendRegular >= hotelRidgewood.weekendRegular):
                    if lowestPriceHotel.weekendRegular == hotelRidgewood.weekendRegular:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelRidgewood)
                    elif lowestPriceHotel.weekendRegular > hotelRidgewood.weekendRegular:
                        lowestPriceHotel = hotelRidgewood
        else:
            if (isWeekDay(dates[i])):
                lowestPriceHotel = hotelLakewood
                if (lowestPriceHotel.weekReward >= hotelBridgewood.weekReward):
                    if lowestPriceHotel.weekReward== hotelBridgewood.weekReward:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelBridgewood)
                    elif lowestPriceHotel.weekReward> hotelBridgewood.weekReward:
                        lowestPriceHotel = hotelBridgewood
                if (lowestPriceHotel.weekReward >= hotelRidgewood.weekReward):
                    if lowestPriceHotel.weekReward == hotelRidgewood.weekReward:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelRidgewood)
                    elif lowestPriceHotel.weekReward> hotelRidgewood.weekReward:
                        lowestPriceHotel = hotelRidgewood
            else:
                lowestPriceHotel = hotelLakewood
                if (lowestPriceHotel.weekendReward >= hotelBridgewood.weekendReward):
                    if lowestPriceHotel.weekendReward == hotelBridgewood.weekendReward:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelBridgewood)
                    elif lowestPriceHotel.weekendReward > hotelBridgewood.weekendReward:
                        lowestPriceHotel = hotelBridgewood
                if (lowestPriceHotel.weekendReward >= hotelRidgewood.weekendReward):
                    if lowestPriceHotel.weekendReward == hotelRidgewood.weekendReward:
                        lowestPriceHotel = getHighestClassification(lowestPriceHotel, hotelRidgewood)
                    elif lowestPriceHotel.weekendReward > hotelRidgewood.weekendReward:
                        lowestPriceHotel = hotelRidgewood
    return lowestPriceHotel

def get_cheapest_hotel(number):   #DO NOT change the function's name
    dates = []

    number = number.split(" ")
    client = isReward(number[0])
    for i in range(len(number)-1):
        day = getDay(number[i+1])
        dates.append(day)
    cheapest_hotel = getHotel(client, dates).name
    print(cheapest_hotel)
    return cheapest_hotel
