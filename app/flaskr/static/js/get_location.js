document.addEventListener('DOMContentLoaded', () => {
    location_input = document.querySelector('#location')
    console.log(location_input)
    navigator.geolocation.getCurrentPosition(pos => {
        coords = { lat: pos.coords.latitude, long: pos.coords.longitude }
        location_input.value = JSON.stringify(coords)
        console.log(location_input.value)
    })
})

