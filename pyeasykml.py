'''
[X] - Feito por Eric Drumond em 2017/04 - Versão 0.1
[X] - Alterado por Eric Drumond em 2019/09 - Versão 0.2
'''

def InicioKML():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
            #'<Placemark>\n'
            '<Document>\n'
            '<name>DWGtoKML</name>'
            '<atom:author>Eric Drumond - ed9bh</atom:author>'
            #'<phoneNumber>+55(31)9 9758-2378</phoneNumber>\n'
            '<description>DWGtoKML foi elaborado por Eric Drumond em 2017/04. Programa gratuito. Quer sua marca aqui, outras opções de DATUM e mais personalização? Entre em contato e solicite um orçamento.</description>\n'
            '<address>"http://br.linkedin.com/in/ericdrumond"</address>\n'
            '<atom:link href="http://br.linkedin.com/in/ericdrumond"/>\n'
            #+ Styles
            )

def FinalKML():
    return ('</Document>\n'
            '</kml>')

def Ponto(Descricao=str, Latitude=float, Longitude=float):#
    ponto = ('\n<Placemark>\n'
             '<name>{}</name>\n'
             '<description>DWGtoPDF - RS(ed9bh) - By:Eric Drumond(2017/04)</description>\n'
             '<Point>'
             '<coordinates>{},{}</coordinates>'
             '</Point>\n'
             '</Placemark>\n'
             ).format(Descricao, Latitude, Longitude)
    return ponto

def Polilinha(Descricao=str, ListaLatitudeLongitude=[], StyleName=str):
    polylinha = ('\n<Placemark>\n'
                 '<name>{0}</name>\n'
                 '<description>DWGtoPDF - RS(ed9bh) - By:Eric Drumond(2017/04)</description>\n'
                 '<styleUrl>#{1}</styleUrl>\n'
                 '<LineString>\n'
                 '<tessellate>1</tessellate>\n'
                 '<altitudeMode>clampToGround</altitudeMode>\n'
                 '<coordinates>'
                 ).format(Descricao, StyleName)

    for coord in ListaLatitudeLongitude:
        polylinha += ("\n{},{}".format(coord[0], coord[1]))

    polylinha = polylinha + ('\n</coordinates>\n'
                             '</LineString>\n'
                             '</Placemark>\n'
                             )
    return polylinha


def Hatch(Descricao=str, ListaLatitudeLongitude=[], StyleName=str):
    hatch = ('\n<Placemark>\n'
             '<name>{0}</name>\n'
             '<description>DWGtoPDF - RS(ed9bh) - By:Eric Drumond(2017/04)</description>\n'
             '<styleUrl>#{1}</styleUrl>\n'
             '<Polygon id="LAYER">\n'
             '<extrude>1</extrude>\n'
             #'<tessellate>1</tessellate>\n'
             '<altitudeMode>clampToGround</altitudeMode>\n'
             '<outerBoundaryIs>\n'
             '<LinearRing>'
             ).format(Descricao, StyleName)

    for coord in ListaLatitudeLongitude:
            hatch += ("\n{},{}".format(coord[0], coord[1]))
    hatch = hatch + ('\n</LinearRing>\n'
                     '</outerBoundaryIs>\n'
                     '<innerBoundaryIs>\n'
                     '<LinearRing>'
                     )
    for coord in ListaLatitudeLongitude:
            hatch += ("\n{},{}".format(coord[0], coord[1]))
    hatch = hatch +('\n</LinearRing>\n'
                    '</innerBoundaryIs>\n'
                    '</Polygon>\n'
                    '</Placemark>\n'
                    )
    return hatch

def cor_RGB_TO_HEX(cor=str):
  red, green, blue = cor.split('_')
  red, green, blue = int(red), int(green), int(blue)
  Color_Hex = '%02x%02x%02x' % (red, green, blue)
  return Color_Hex

def corCadHex(cor):
    if cor == 1:
      return "red"
    elif cor == 2:
      return "yellow"
    elif cor == 3:
      return "green"
    elif cor == 4:
      return "cyan"
    elif cor == 5:
      return "blue"
    elif cor == 6:
      return "magenta"
    elif cor == 7:
      return "white"
    elif cor == 8:
      return "grey"
    elif cor == 9:
      return "darkGrey"
    elif cor >= 10 and cor <= 29:
      return "darkRed"
    elif cor >= 30 and cor <= 52:
      return "darkYellow"
    elif cor >= 53 and cor <= 119:
      return "darkGreen"
    elif cor >= 120 and cor <= 149:
      return "darkCyan"
    elif cor >= 150 and cor <= 199:
      return "darkBlue"
    elif cor >= 200 and cor <= 249:
      return "pink"
    elif cor >= 250 and cor <= 255:
      return "darkGrey"
    else:
        return "black"

Styles = (
            # Estilos de Linha
            # Vermelho / 1
            '<Style id="red">\n'
            '<LineStyle>\n'
            '<color>ff0000ff</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff0000ff</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Amarelo / 2
            '<Style id="yellow">\n'
            '<LineStyle>\n'
            '<color>ff00ffff</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff00ffff</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Verde / 3
            '<Style id="green">\n'
            '<LineStyle>\n'
            '<color>ff00ff00</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff00ff00</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Cyan / 4
            '<Style id="cyan">\n'
            '<LineStyle>\n'
            '<color>ffff7e10</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ffff7e10</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Blue / 5
            '<Style id="blue">\n'
            '<LineStyle>\n'
            '<color>ffff0010</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ffff0010</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Magenta / 6
            '<Style id="magenta">\n'
            '<LineStyle>\n'
            '<color>ffff00cc</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ffff00cc</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Branco / 7
            '<Style id="white">\n'
            '<LineStyle>\n'
            '<color>ffffffff</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ffffffff</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Cinza claro / 8
            '<Style id="grey">\n'
            '<LineStyle>\n'
            '<color>ff808080</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff808080</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Cinza Escuro / 9
            '<Style id="darkGrey">\n'
            '<LineStyle>\n'
            '<color>ff505050</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff505050</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Vermelho Escuro / 10
            '<Style id="darkRed">\n'
            '<LineStyle>\n'
            '<color>ff0000ff</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff000000</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
            # Preto / > 10
            '<Style id="black">\n'
            '<LineStyle>\n'
            '<color>ff000000</color>\n'
            '<width>2</width>\n'
            '</LineStyle>\n'
            '<PolyStyle>\n'
            '<color>ff000000</color>\n'
            '<colorMode>normal</colorMode>\n'
            '<fill>1</fill>\n'
            '<outline>1</outline>\n'
            '</PolyStyle>\n'
            '</Style>\n'
)


def make_New_Style(Name, Hex_Color):
  style = (
    f'\n\n<Style id="{Name}">\n'
    '\t<LineStyle>\n'
    f'\t\t<color>{Hex_Color}</color>\n'
    '\t\t<width>2</width>\n'
    '\t</LineStyle>\n'
    '\t<PolyStyle>\n'
    f'\t\t<color>{Hex_Color}</color>\n'
    '\t\t<width>2</width>\n'
    '\t<colorMode>normal</colorMode>\n'
    #'\t<fill>1</fill>\n'
    #'\t<outline>1</outline>\n'
    '\t</PolyStyle>\n'
    '</Style>\n\n'
  )
  return style




'''
<Polygon id="ID">
  <!-- specific to Polygon -->
  <extrude>0</extrude>                       <!-- boolean -->
  <tessellate>0</tessellate>                 <!-- boolean -->
  <altitudeMode>clampToGround</altitudeMode>
        <!-- kml:altitudeModeEnum: clampToGround, relativeToGround, or absolute -->
        <!-- or, substitute gx:altitudeMode: clampToSeaFloor, relativeToSeaFloor -->
  <outerBoundaryIs>
    <LinearRing>
      <coordinates>...</coordinates>         <!-- lon,lat[,alt] -->
    </LinearRing>
  </outerBoundaryIs>
  <innerBoundaryIs><LinearRing>
      <coordinates>...</coordinates>         <!-- lon,lat[,alt] -->
    </LinearRing></innerBoundaryIs>
</Polygon>
'''

'''
<Polygon>
      <extrude>1</extrude>
      <altitudeMode>relativeToGround</altitudeMode>
      <outerBoundaryIs>
        <LinearRing>
          <coordinates>
            -122.3662784465226,37.81884427772081,30
            -122.3652480684771,37.81926777010555,30
            -122.365640222455,37.81986126286519,30
            -122.36666937925,37.81942987753481,30
            -122.3662784465226,37.81884427772081,30
          </coordinates>
        </LinearRing>
      </outerBoundaryIs>
      <innerBoundaryIs>
        <LinearRing>
          <coordinates>
            -122.366212593918,37.81897719083808,30
            -122.3654241733188,37.81929450992014,30
            -122.3657048517827,37.81973175302663,30
            -122.3664882465854,37.81940249291773,30
            -122.366212593918,37.81897719083808,30
          </coordinates>
        </LinearRing>
      </innerBoundaryIs>
    </Polygon>
'''