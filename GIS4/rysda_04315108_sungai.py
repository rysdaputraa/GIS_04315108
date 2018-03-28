import mapnik
m = mapnik.Map(1520,1300)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('blue')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 15)
line_symbolizer.stroke_width =  50

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:\GIS\SHP_Indonesia_pantai\IND_PNT_polyline.shp")
layer = mapnik.Layer('Sungai')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'rysda_04315108_sungai.jpeg', 'jpeg')
print "sudah jadi file nya = 'rysda_04315108_sungai.jpeg"

