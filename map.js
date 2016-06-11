var map = L.map('map',{
    center: [1.505, -0.09],
    zoom: 1
});


L.tileLayer('http://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
}).addTo(map);

// map.on('popupopen', function(centreMarker) {
//     var cM = map.project(centreMarker.popup._latlng);
//     cM.y -= centreMarker.popup._container.clientHeight/2
//     map.panTo(map.unproject(cM),{animate: true});
// });

// var collisionLayer = L.layerGroup.collision({margin:2});
// collisionLayer.addTo(map);
