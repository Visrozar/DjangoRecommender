var map;
var latlngBounds;

window.onload = function () {
    initializeMaps();
}

function initializeMaps() {
    var mapOptions = {
        center: new google.maps.LatLng('37.7219', '-122.4572'),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoom: 8,
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            position: google.maps.ControlPosition.TOP_RIGHT
        },
        styles: [{ "featureType": "all", "elementType": "geometry", "stylers": [{ "color": "#eae9e1" }, { "gamma": "5.27" }] },
        { "featureType": "all", "elementType": "labels", "stylers": [{ "color": "#eae9e1" }, { "visibility": "off" }, { "gamma": "5.27" }] },
        { "featureType": "all", "elementType": "labels.text.fill", "stylers": [{ "gamma": 0.01 }, { "lightness": 20 }] },
        { "featureType": "all", "elementType": "labels.text.stroke", "stylers": [{ "saturation": -31 }, { "lightness": -33 }, { "weight": 2 }, { "gamma": 0.8 }] },
        { "featureType": "all", "elementType": "labels.icon", "stylers": [{ "visibility": "off" }] },
        { "featureType": "landscape", "elementType": "geometry", "stylers": [{ "lightness": 30 }, { "saturation": 30 }] },
        { "featureType": "poi", "elementType": "geometry", "stylers": [{ "saturation": 20 }] },
        { "featureType": "poi.park", "elementType": "geometry", "stylers": [{ "lightness": 20 }, { "saturation": -20 }] },
        { "featureType": "road", "elementType": "geometry.fill", "stylers": [{ "gamma": "0.54" }] },
        { "featureType": "road", "elementType": "geometry.stroke", "stylers": [{ "saturation": "10" }, { "lightness": "-1" }] },
        { "featureType": "road.highway", "elementType": "geometry.fill", "stylers": [{ "color": "#eae9e1" }, { "lightness": "37" }] },
        { "featureType": "road.highway", "elementType": "geometry.stroke", "stylers": [{ "color": "#e1ddc0" }, { "visibility": "off" }] },
        { "featureType": "road.arterial", "elementType": "geometry.fill", "stylers": [{ "color": "#f3f3ed" }] },
        { "featureType": "road.arterial", "elementType": "geometry.stroke", "stylers": [{ "visibility": "off" }, { "color": "#c8bb96" }] },
        { "featureType": "road.local", "elementType": "geometry.fill", "stylers": [{ "color": "#eae9e1" }] },
        { "featureType": "road.local", "elementType": "geometry.stroke", "stylers": [{ "lightness": "2" }, { "visibility": "off" }, { "color": "#e5e1c5" }] },
        { "featureType": "road.local", "elementType": "labels.text.stroke", "stylers": [{ "color": "#f7f7f2" }, { "visibility": "off" }] },
        { "featureType": "water", "elementType": "all", "stylers": [{ "lightness": "0" }, { "color": "#e9e9e9" }, { "saturation": "-24" }] }]
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    latlngBounds = new google.maps.LatLngBounds();
}
