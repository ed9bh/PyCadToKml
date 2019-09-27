# %%
from os import chdir, remove
from glob import glob
from numpy import sin, cos, deg2rad
from csv import reader
from utm import to_latlon
from zipfile import ZipFile
#chdir('./PyCadToKml')
import pyeasykml as KML
from pyeasykml import cor_RGB_TO_HEX, make_New_Style
# %%
# Funções


def coordenadasCirculo(CenterX=float, CenterY=float, Radious=float):
    angles = [ang for ang in range(1, 360)]
    pointList = []
    for ang in angles:
        azm = deg2rad(ang)
        calcX = (sin(azm) * Radious) + CenterX
        calcY = (cos(azm) * Radious) + CenterY
        pointList.append([calcX, calcY])
    return pointList


# %%
dirTestes = r'A:/_Projetos/DwgDeTestes/CSVExtraction_20190917'
outFile = r'A:/_Projetos/DwgDeTestes/Out.kml'
# chdir(dirTestes)
Entidades = glob(dirTestes + '/' + '*.csv')
ZONE_NUMBER = 22
ZONE_LETTER = 'k'

# %%

if __name__ == '__main__':

    with open(outFile, 'w', encoding='UTF-8') as target:
        target.write(KML.InicioKML())
        pass

    styleNames = []
    content = ''

    for ENT in Entidades:

        #print(ENT)

        with open(ENT, 'r') as csvFile:
            ENT = ENT.replace(dirTestes + '\\', '')
            EntyType = ENT.split('_')[0]

            StyleName = ENT
            StyleName = StyleName.replace('.csv', '')
            StyleName = StyleName.replace('_', '')

            Raw = reader(csvFile)
            Content = []

            for item in Raw:
                Content.append(item)
                pass
            del Content[0]
            coords = []

            if EntyType == 'Circle':
                for line in Content:
                    cont = line[0].split(';')
                    describe = cont[0]
                    color = cont[1]
                    TrueColor_HEX = cor_RGB_TO_HEX(color)
                    x, y, rad = float(cont[2]), float(cont[3]), float(cont[5])
                    CircunferencePoints = coordenadasCirculo(x, y, rad)
                    for item in CircunferencePoints:
                        point = to_latlon(
                            easting=item[0], northing=item[1], zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                        coords.append([point[1], point[0]])
                        pass
                    TrueColor_HEX = cor_RGB_TO_HEX(color)
                    Style = make_New_Style(StyleName, TrueColor_HEX)
                    with open(outFile, 'a+') as target:
                        target.write(Style)
                    content += KML.Polilinha(describe, coords, StyleName)
                    pass
                pass
            elif EntyType == 'LWPolyline':
                for item in Content:
                    cont = item[0].split(';')
                    describe = cont[0]
                    color = cont[1]
                    x, y = float(cont[2]), float(cont[3])
                    point = to_latlon(
                        easting=x, northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                TrueColor_HEX = cor_RGB_TO_HEX(color)
                Style = make_New_Style(StyleName, TrueColor_HEX)
                with open(outFile, 'a+') as target:
                    target.write(Style)
                content += KML.Polilinha(describe, coords, StyleName)
                pass
            elif EntyType == 'Line':
                for item in Content:
                    cont = item[0].split(';')
                    describe = cont[0]
                    color = cont[1]
                    x, y = float(cont[2]), float(cont[3])
                    point = to_latlon(
                        easting=x, northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                TrueColor_HEX = cor_RGB_TO_HEX(color)
                Style = make_New_Style(StyleName, TrueColor_HEX)
                with open(outFile, 'a+') as target:
                    target.write(Style)
                content += KML.Polilinha(describe, coords, StyleName)
                pass
            elif EntyType == 'Point':
                for item in Content:
                    cont = item[0].split(';')
                    describe = cont[0]
                    color = cont[1]
                    x, y = float(cont[2]), float(cont[3])
                    point = to_latlon(
                        easting=x, northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                for item in coords:
                    content += KML.Ponto(describe,
                                         Latitude=item[0], Longitude=item[1])
                    pass
                pass
            #print(TrueColor_HEX)
            pass
        pass

    with open(outFile, 'a+', encoding='UTF-8') as target:
        target.write(content)
        target.write(KML.FinalKML())
        pass

    KMZ_Name = outFile.replace('.kml', '.kmz')
    with ZipFile(KMZ_Name, 'w') as target:
        target.write(outFile)
        pass

# %%
