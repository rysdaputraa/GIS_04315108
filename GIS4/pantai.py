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

basinlabels = mapnik.TextSymbolizer(mapnik.Expression('[Nama]'), 'DejaVu Sans Bold',15,mapnik.Color('black'))
basinlabels.halo_fill = mapnik.Color('yellow')
basinlabels.halo_radius = 2
r.symbols.append(basinlabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

#highlight = mapnik.PolygonSymbolizer()
#highlight.fill = mapnik.Color('red')
#japan = mapnik.Rule()
#japan.filter = mapnik.Expression("[NAME]='Japan'")
#japan.symbols.append(highlight)
#s.rules.append(japan)

#highlight = mapnik.PolygonSymbolizer()
#highlight.fill = mapnik.Color('blue')
#Canada = mapnik.Rule()
#Canada.filter = mapnik.Expression("[NAME]='Canada'")
#Canada.symbols.append(highlight)
#s.rules.append(Canada)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="C:/Users/ryswan/Documents/GitHub/GIS_04315108/GIS4/SHP_Indonesia_pantai/IND_PNT_polyline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()


mapnik.render_to_file(m, 'kuis.pdf', 'pdf')
print "iki wes metu 'kuis.pdf'"