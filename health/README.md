سەنتەرەکانی تەندروستی هەرێم و شوێنەکانیان
================
<div style="direction:rtl">
لائق حەمە
</div>
2019-02-23

<div style="direction:rtl">
بۆ بینینی داتاکە بە زمانی ئاڕ و زانینی هەندێ ژمارە:
</div>

``` r
x = read.csv("data.csv")
summary(x$type)
```

    ##    branch   centers emergency  hospital      main maternity 
    ##       624        73         9        53       259         9

``` r
coords = c("longitude", "latitude")
x_sf = sf::st_as_sf(x, coords = coords, crs = 4326)
geojson = geojsonio::geojson_json(x_sf)
# write(geojson, "data.geojson")
```
<div style="direction:rtl">
ئەنجا بۆ ئەوەی لەم پەڕەیە بیبینین
</div>

``` r
library(htmltools)
data = geojsonio::geojson_json(x_sf[, c("type", "arabic_name", "directorate")], 
factors_as_string = TRUE)
template = paste0('
<html lang="ku">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" integrity="sha512-puBpdR0798OZvTTbP4A8Ix/l+A4dHDD0DGqYW6RQ+9jxkRFclaxxQb/SJAWZfWAkuyeQUytO7+7N4QKrDh+drA==" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js" integrity="sha512-QVftwZFqvtRNi0ZyCtsznlKSWOStnDORoefr1enyq5mVL4tmKB3S/EnC3rRJcxCPavG10IcrVGSmPh6Qw5lwrg==" crossorigin=""></script>
</head>
<body>
<div id="mapid" style="width: 100%; height: 400px;">
<script>
    var map = L.map("mapid");
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw", {
        maxZoom: 18,
        attribution: \'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>\',
        id: "mapbox.streets"
  }).addTo(map);   
  var json = ', data, ';', 
  '
  var geojsonMarkerOptions = {
    radius: 6,
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.5
  };
  var layer = L.geoJSON(json, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, geojsonMarkerOptions);
    },
    style: function(feature) {
      switch (feature.properties.type) {
          case "branch": return {color: "#FEB24C"};
          case "centers":   return {color: "#BD0026"};
          case "emergency":   return {color: "#FF0000"};
          case "hospital":   return {color: "#00FF00"};
          case "main":   return {color: "#0000FF"};
          case "maternity":   return {color: "#FF0026"};
       }
    }
  }).addTo(map);
  map.fitBounds(layer.getBounds());
  var legend = L.control({position: "bottomright"});
    legend.onAdd = function (map) {
        var div = L.DomUtil.create("div", "info legend"), labels = [];
        labels.push("<i style=\'background:#FEB24C\'></i>branch");
        labels.push("<i style=\'background:#BD0026\'></i>centers");
        labels.push("<i style=\'background:#FF0000\'></i>emergency");
        labels.push("<i style=\'background:#00FF00\'></i>hospital");
        labels.push("<i style=\'background:#0000FF\'></i>main");
        labels.push("<i style=\'background:#FF0026\'></i>maternity");
        div.innerHTML = labels.join("<br>");
        return div;
    };
  legend.addTo(map);
  var info = L.control();
  info.onAdd = function (map) {
    this._div = L.DomUtil.create("div", "info");
    this.update();
    return this._div;
  };
  info.update = function (props) {
    this._div.innerHTML = "<h6>بنکە تەندروستیەکان</h6>";
  };
  info.addTo(map);
</script>
<style>
.info { padding: 6px 8px; font: 14px/16px Arial, Helvetica, sans-serif; background: white; background: rgba(255,255,255,0.8); box-shadow: 0 0 15px rgba(0,0,0,0.2); border-radius: 5px; } .info h4 { margin: 0 0 5px; color: #777; }
.legend { text-align: left; line-height: 18px; color: #555; } .legend i { width: 18px; height: 18px; float: left; margin-right: 8px; opacity: 0.7; }</style>
</div></body></html>')
write(template, "view.html")
includeHTML("view.html")
```


