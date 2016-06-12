
var map = L.map('map',{
    center: [51.4892006531,-3.1733899117],
    zoom: 14
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	    maxZoom: 18,
	    id: 'trekwho.o0pmdp8k',
	    accessToken: 'pk.eyJ1IjoidHJla3dobyIsImEiOiJjaWdhcTVyZW8wM2N1d2RtN2E5ZHB1bWdkIn0.Hp0qtRYfZegcf4rn4FL70Q'
	}).addTo(map);

var tweets =[];

d3.csv("mapTrash.csv", function(d) {
  return {
    tweet_text : d.tweet_text,
    picture_url : d.picture_url,
    location : d["location"]
  };
}, function(data) {
  drawMarker(data);
});

function drawMarker(data){
  console.log(data);
  map.on('popupopen', function(centreMarker) {
    var cM = map.project(centreMarker.popup._latlng);
    cM.y -= centreMarker.popup._container.clientHeight/2
    map.panTo(map.unproject(cM),{animate: true});
  });

var markerClusters = L.markerClusterGroup();

for ( var i = 0; i < data.length; ++i )
{
  if(data[i]['location'] != ''){
  var loc = JSON.parse(data[i]['location']);
  var content = '<p class="text">' + data[i]['tweet_text'] + '</p><img class="pic" src="' + data[i]['picture_url']+ '">';

  var m = L.marker([loc[0], loc[1]])
                  .bindPopup(content);

  markerClusters.addLayer(m);
  }
}

map.addLayer( markerClusters );

}
