console.log('*');

function addHouse() {
    console.log('-');
    const data = {
        longitude: document.getElementById('longitude').value,
        latitude: document.getElementById('latitude').value,
        housing_median_age: document.getElementById('housing_median_age').value,
        total_rooms: document.getElementById('total_rooms').value,
        total_bedrooms: document.getElementById('total_bedrooms').value,
        population: document.getElementById('population').value,
        households: document.getElementById('households').value,
        median_income: document.getElementById('median_income').value,
        median_house_value: document.getElementById('median_house_value').value,
        ocean_proximity: document.getElementById('ocean_proximity').value,
    };

    $.ajax({
        type: "POST",
        url: "/create_house/",
        data: data,
        success: function(response){
            window.location.href = '/';
        }
    })
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
