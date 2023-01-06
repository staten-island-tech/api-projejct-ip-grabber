function get_location() {
    location_input = document.querySelector('#location')
    console.log(location_input)
    navigator.geolocation.getCurrentPosition(pos => {
        coords = { lat: pos.coords.latitude, long: pos.coords.longitude }
        location_input.value = JSON.stringify(coords)
        console.log(location_input.value)
}

document.addEventListener('DOMContentLoaded', 
    () => {
        get_location()
    }, err => {
        alert('We need your location to display your local weather. Please accept the request.')
        get_location()
    })
})

