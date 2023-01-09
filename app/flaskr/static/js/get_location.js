function get_location() {
    location_input = document.querySelector('#location')
    alert('Please allow location, it lets us show your local weather. This is required to create your account.')
    navigator.geolocation.getCurrentPosition(pos => {
        coords = { lat: pos.coords.latitude, long: pos.coords.longitude }
        location_input.value = JSON.stringify(coords)
    }, () => {
        location.href = '/';
    })
}

document.addEventListener('DOMContentLoaded', 
    () => {
        get_location()
    }
)