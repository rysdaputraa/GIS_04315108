import mapnik
m = mapnik.Map(1080,720)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
r.symbols.append(line_symbolizer)

basinlabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',10,mapnik.Color('white'))
basinlabels.halo_fill = mapnik.Color('black')
basinlabels.halo_radius = 2
r.symbols.append(basinlabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('red')
japan = mapnik.Rule()
japan.filter = mapnik.Expression("[NAME]='Japan'")
japan.symbols.append(highlight)
s.rules.append(japan)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/SHP_Country/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)
m.zoom_all()

s = mapnik.Style()
r = mapnik.Rule()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 0.1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()

s = mapnik.Style()
r = mapnik.Rule()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/brazil-coastline/brazil_coastline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)
m.zoom_all()

s = mapnik.Style()
r = mapnik.Rule()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('grey'), 0.1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/madagascar-roads-shape/roads.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)
m.zoom_all()

s = mapnik.Style()
r = mapnik.Rule()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('grey'), 0.8)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/antartica-roads/roads.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)
m.zoom_all()

mapnik.render_to_file(m, 'kuis.pdf', 'pdf')
print "iki wes metu 'kuis.pdf'"