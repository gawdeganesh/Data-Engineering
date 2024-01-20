def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s':
    if totalSeconds == 0:
        return '0s'
    if totalSeconds >=3600:
        hours = totalSeconds//3600
        totalSeconds= totalSeconds %3600
    else:
        hours=0

    if totalSeconds>=60:
        minutes = totalSeconds//60
        totalSeconds= totalSeconds%60
    else:
        minutes= 0

    seconds = totalSeconds

    hms= []
    if hours>0:
        hms.append(str(hours)+'h')  
    if minutes>0:
        hms.append(str(minutes)+'m')  
    if seconds>0:
        hms.append(str(seconds)+'s')    
        
    #return ' '.join(hms)
    return hms

print(getHoursMinutesSeconds(60))