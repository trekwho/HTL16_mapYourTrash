var map = L.map('map',{
    center: [51.4752006531,-3.1733899117],
    zoom: 13
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	    maxZoom: 18,
	    id: 'trekwho.o0pmdp8k',
	    accessToken: 'pk.eyJ1IjoidHJla3dobyIsImEiOiJjaWdhcTVyZW8wM2N1d2RtN2E5ZHB1bWdkIn0.Hp0qtRYfZegcf4rn4FL70Q'
	}).addTo(map);

// map.on('popupopen', function(centreMarker) {
//     var cM = map.project(centreMarker.popup._latlng);
//     cM.y -= centreMarker.popup._container.clientHeight/2
//     map.panTo(map.unproject(cM),{animate: true});
// });

// var collisionLayer = L.layerGroup.collision({margin:2});
// collisionLayer.addTo(map);
