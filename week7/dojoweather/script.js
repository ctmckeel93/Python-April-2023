console.log("page loading...");

var cookieDiv = document.querySelector(".cookie-policy");
const API = 'ad19147a17d290864b375c566f1eb41e'



function loading() {
    alert("Loading weather report...")
}

function accept() {
    cookieDiv.remove();
}

function c2f(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function f2c(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function convert(element) {
    console.log(element.value);
        var tempSpanHigh = document.querySelector("#high");
        var tempSpanLow = document.querySelector("#low");
        var tempValHigh = parseInt(tempSpanHigh.innerText);
        var tempValLow = parseInt(tempSpanLow.innerText);
        if(element.value == "°C") {
            tempSpanHigh.innerText = f2c(tempValHigh);
            tempSpanLow.innerText = f2c(tempValLow);
        } else {
            tempSpanHigh.innerText = c2f(tempValHigh);
            tempSpanLow.innerText = c2f(tempValLow);
        }
}

async function getWeather(lat, lon) {

    let response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API}`)
    let data = await response.json()
    setWeather(data)
}

function setWeather(weatherData) {
    const highTemp = document.getElementById("high")
    const lowTemp = document.getElementById("low")
    const currentWeather = document.getElementById("currentWeather")

    let high = weatherData.main.temp_max
    let low = weatherData.main.temp_min
    let weather = weatherData.weather[0].description

    console.log(high)
    console.log(low)
    console.log(weather)

    highTemp.innerText = Math.floor(convertFromKelvin(high))
    lowTemp.innerText = Math.floor(convertFromKelvin(low))
    currentWeather.innerText = weather



}

function convertFromKelvin(kelvin) {
    let dropdown = document.querySelector("#dropdown").value

    if (dropdown == "°C") {
        return kelvin - 273.15
    } else {
        return (kelvin - 273.15) * 9/5 + 32
    }
}
