# autograde:all-correct a11111 time:2022-11-14T04:28:30+00:00 UTC
def year_dates(dates):
    d={}
    for element in dates:
        Key=element.split("-")[2]
        Value=element
        
        if Key not in d:
            d[Key]=[]
        d[Key].append(Value)
    return d

