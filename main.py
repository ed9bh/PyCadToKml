# %%
from os import chdir, remove
from glob import glob
from numpy import sin, cos, deg2rad
from csv import reader
chdir(r'A:\_Projetos\PyCadToKml')
import pyeasykml as KML
from utm import to_latlon
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
dirTestes = r'A:\_Projetos\DwgDeTestes\CSVExtraction_20190915'
outFile = r'A:\_Projetos\DwgDeTestes\Out.kml'
chdir(dirTestes)
Entidades = glob('*.csv')
ZONE_NUMBER = 22
ZONE_LETTER = 'k'

# %%

if __name__ == '__main__':

    with open(outFile, 'w') as target:
        target.write(KML.InicioKML())
        pass

    for ENT in Entidades:

        with open(ENT, 'r') as csvFile:
            EntyType = ENT.split('_')[0]

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
                    x, y, rad = float(cont[0]), float(cont[1]), float(cont[3])
                    CircunferencePoints = coordenadasCirculo(x, y, rad)
                    pass
                for item in CircunferencePoints:
                    point = to_latlon(easting=item[0],northing=item[1], zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                pass
            elif EntyType == 'LWPolyline':
                for item in Content:
                    cont = item[0].split(';')
                    x, y = float(cont[0]), float(cont[1])
                    point = to_latlon(easting=x,northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                pass
            elif EntyType == 'Line':
                for item in Content:
                    cont = item[0].split(';')
                    x, y = float(cont[0]), float(cont[1])
                    point = to_latlon(easting=x,northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                pass
            elif EntyType == 'Point':
                for item in Content:
                    cont = item[0].split(';')
                    x, y = float(cont[0]), float(cont[1])
                    point = to_latlon(easting=x,northing=y, zone_number=ZONE_NUMBER, zone_letter=ZONE_LETTER)
                    coords.append([point[1], point[0]])
                    pass
                pass
            
            with open(outFile, 'a+') as target:
                if EntyType == 'LWPolyline':
                    target.write(KML.Polilinha('teste', KML.corCadHex(2) , coords))
                    pass
                if EntyType == 'Circle':
                    target.write(KML.Polilinha('teste', KML.corCadHex(3) , coords))
                    pass
                if EntyType == 'Line':
                    target.write(KML.Polilinha('teste', KML.corCadHex(6) , coords))
                    pass
                if EntyType == 'Point':
                    for item in coords:
                        target.write(KML.Ponto(Descricao=EntyType,Latitude=item[0],Longitude=item[1]))
                    pass
                

    
    with open(outFile, 'a+') as target:
        target.write(KML.FinalKML())
