const search_input = document.querySelector('#search')

// https://api.geoapify.com/v1/geocode/autocomplete?apiKey=da825532c8614a4db984b18ba9be005a&text=Atlanta&type=city

const autocomplete_url = 'https://api.geoapify.com/v1/geocode/autocomplete?apiKey=da825532c8614a4db984b18ba9be005a&type=city'

search_input.addEventListener('change', () => {
    console.log(autocomplete_url + `&text=${search_input.value}`)
})