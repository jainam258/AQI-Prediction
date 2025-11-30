async function searchAQI() {
    const city = document.getElementById("city-input").value.trim();

    if (!city) {
        document.getElementById("result").innerHTML = "Enter a city!";
        return;
    }

    const response = await fetch("data/aqi.json");
    const dataset = await response.json();

    const found = dataset.find(item => 
        item.city.toLowerCase() === city.toLowerCase()
    );

    if (!found) {
        document.getElementById("result").innerHTML = "City not found!";
        return;
    }

    document.getElementById("result").innerHTML =
        `AQI in <b>${found.city}</b>: <span class="text-red-600">${found.aqi}</span>`;
}
