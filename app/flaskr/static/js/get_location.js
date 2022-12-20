navigator.geolocation.getCurrentPosition(user_location => {
    const url = 'http://127.0.0.1:5000/set_location'
    const params = {
        lat: user_location.coords.latitude,
        long: user_location.coords.longitude
    }

    fetch(url, { 
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(params)
    })

    console.log('sent')
}, () => {
    console.log('error')
})

