length, ana, bia, time, distance = map(int, raw_input().split())

ana /= 100.0
bia /= 100.0
time *= 60.0

ana_position = float(((length - distance) + (ana * time)) % length)
bia_position = float(((length - distance) + (bia * time)) % length)

if ana_position == 0:
    ana_position = length*1.0
if bia_position == 0:
    bia_position = length*1.0
try:
    ana_tta = (length - ana_position) / ana
except ZeroDivisionError:
    ana_tta = 999999
try:
    bia_tta = (length - bia_position) / bia
except ZeroDivisionError:
    bia_tta = 999999

#print ana, ana_position, ana_tta
#print bia, bia_position, bia_tta
"""
if ana_position == bia_position:
    print "Ana" if ana >= bia else "Bia"
else:
"""
print "Ana" if ana_tta <= bia_tta else "Bia"