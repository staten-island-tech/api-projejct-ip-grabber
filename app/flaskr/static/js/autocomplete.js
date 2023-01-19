const search_input = document.querySelector('#search')
const autocomplete_list = document.querySelector('#autocomplete_list')

// https://api.geoapify.com/v1/geocode/autocomplete?apiKey=da825532c8614a4db984b18ba9be005a&text=Atlanta&type=city

const autocomplete_url = 'https://api.geoapify.com/v1/geocode/autocomplete?apiKey=da825532c8614a4db984b18ba9be005a&type=city'

timeoutID = 0

search_input.addEventListener('keydown', () => {
    clearTimeout(timeoutID)
    while(autocomplete_list.firstChild) {
        autocomplete_list.removeChild(autocomplete_list.firstChild)
    }
    if(search_input.value != '') {
        timeoutID = setTimeout(() => {
            fetch(autocomplete_url + `&text=${search_input.value}`)
            .then(res => res.json())
            .then(data => {
                console.log(data)
                for(let feature in data.features) {
                    feature = data.features[feature]
                    autocomplete_option = document.createElement('button')
                    autocomplete_option.append(`${feature.properties.city}, ${feature.properties.state}, ${feature.properties.country}`)
                    autocomplete_list.append(autocomplete_option)
                }
            })
        }, 200);
    }
})