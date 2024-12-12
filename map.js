var map = L.map('map').setView([33.3152, 44.3661], 5);  // Center on Iraq

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Fetch city data from Flask API
fetch('/api/cities')
    .then(response => response.json())
    .then(data => {
        // Add markers for each city
        for (let city in data) {
            let cityData = data[city];
            L.marker([33.3152, 44.3661])  // Example coordinates for Baghdad, can update per city
                .addTo(map)
                .bindPopup(`<b>${city}</b><br>GDP: $${cityData.gdp}M<br>Industry: ${cityData.industry}<br>Population: ${cityData.population}`)
                .on('click', function() {
                    document.getElementById('city-info').innerHTML = `
                        <h3>${city}</h3>
                        <p><strong>GDP:</strong> $${cityData.gdp}M</p>
                        <p><strong>Industry:</strong> ${cityData.industry}</p>
                        <p><strong>Population:</strong> ${cityData.population}</p>
                    `;
                });
        }
    })
    .catch(error => console.log(error));
