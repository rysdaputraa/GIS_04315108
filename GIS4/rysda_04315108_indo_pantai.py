import mapnik
m = mapnik.Map(2300,1200)
m.background = mapnik.Color('yellow')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('black')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('purple'), 1)
line_symbolizer.stroke_width =  1
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:\GIS\SHP_Indonesia_pantai\IND_PNT_polyline.shp")
layer = mapnik.Layer('pantai')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'rysda_04315108_pantai.jpeg', 'jpeg')
print "sudah jadi file nya = 'rysda_04315108_pantai.jpeg"


