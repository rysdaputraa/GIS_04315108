import mapnik
m = mapnik.Map(2340,3100)
m.background = mapnik.Color('blue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('yellow')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 8)
line_symbolizer.stroke_width = 1

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="D:\GIS\SHP_Indonesia_provinsi\INDONESIA_PROP.shp")
layer = mapnik.Layer('provinsi')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m, 'rysda_04315108_provinsi.jpeg', 'jpeg')
print "sudah jadi file nya = 'rysda_04315108_provinsi.jpeg"


