def add_time(start, duration,day=None):
  new_time = ''
  noOfDays = 0
  am_pm_change = {'AM':'PM', 'PM':'AM'}

  #Retrieving Hour, Min data from given values
  startSplit = start.split(' ')
  am_pm = startSplit[1]
  startSplit = startSplit[0].split(':')
  startHr = int(startSplit[0])
  startMin = int(startSplit[1])

  durSplit = duration.split(':')
  durHr = int(durSplit[0])
  durMin = int(durSplit[1])
  
  #print(startHr,startMin,am_pm)
  #print(durHr,durMin)

  #Calculating new hour and minutes
  noOfDays = durHr//24
  newMin = startMin+durMin
  if newMin > 60:
    durHr += 1
    newMin = newMin%60

  newHr = startHr+durHr
  if newHr > 12:
    newHr = newHr%12
    if newHr == 0:
      newHr = 12

  #AM/PM change
  am_pm_flips = (startHr+durHr)//12  
  if(am_pm == 'PM' and startHr+(durHr%12) >= 12):
    noOfDays += 1
  if am_pm_flips % 2 == 1:
    am_pm = am_pm_change[am_pm]
  #print(newHr,newMin,am_pm,noOfDays)

  if newMin < 10:
    newMin = '0'+str(newMin)
  newMin = str(newMin)
  newHr = str(newHr) 
     
  new_time = newHr + ':' + newMin + ' ' + am_pm

  #if Start of week day is given
  if day:
    dayDict = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
    dayList = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day = day.lower()
    newDay = dayList[(dayDict[day]+noOfDays)%7]
    new_time += ', '+newDay

  if noOfDays == 1:
    new_time += ' (next day)' 
  elif noOfDays >= 1:
    new_time += ' ({0} days later)'.format(noOfDays)

  
  return new_time