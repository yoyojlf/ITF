var total = document.getElementById("totalSlider");

var slider = document.getElementById("rangeSlider");
var output = document.getElementById("valor");

output.innerHTML = slider.value;

slider.oninput = function () {
    output.innerHTML = this.value;

    total.innerHTML = parseInt(slider.value, 10) +
        parseInt(slider2.value, 10) +
        parseInt(slider3.value, 10) +
        parseInt(slider4.value, 10) +
        parseInt(slider5.value, 10);
}

// -------------------------------------------------------
var slider2 = document.getElementById("rangeSlider2");
var output2 = document.getElementById("valor2");

output2.innerHTML = slider2.value;

slider2.oninput = function () {
    output2.innerHTML = this.value;

    total.innerHTML = parseInt(slider.value, 10) +
        parseInt(slider2.value, 10) +
        parseInt(slider3.value, 10) +
        parseInt(slider4.value, 10) +
        parseInt(slider5.value, 10);
}

// -------------------------------------------------------


var slider3 = document.getElementById("rangeSlider3");
var output3 = document.getElementById("valor3");

output3.innerHTML = slider3.value;

slider3.oninput = function () {
    output3.innerHTML = this.value;

    total.innerHTML = parseInt(slider.value, 10) +
        parseInt(slider2.value, 10) +
        parseInt(slider3.value, 10) +
        parseInt(slider4.value, 10) +
        parseInt(slider5.value, 10);
}

// -------------------------------------------------------

var slider4 = document.getElementById("rangeSlider4");
var output4 = document.getElementById("valor4");

output4.innerHTML = slider4.value;

slider4.oninput = function () {
    output4.innerHTML = this.value;

    total.innerHTML = parseInt(slider.value, 10) +
        parseInt(slider2.value, 10) +
        parseInt(slider3.value, 10) +
        parseInt(slider4.value, 10) +
        parseInt(slider5.value, 10);
}

// -------------------------------------------------------

var slider5 = document.getElementById("rangeSlider5");
var output5 = document.getElementById("valor5");

output5.innerHTML = slider5.value;

slider5.oninput = function () {
    output5.innerHTML = this.value;

    total.innerHTML = parseInt(slider.value, 10) +
        parseInt(slider2.value, 10) +
        parseInt(slider3.value, 10) +
        parseInt(slider4.value, 10) +
        parseInt(slider5.value, 10);
}

// -------------------------------------------------------

total.innerHTML = parseInt(slider.value, 10) +
    parseInt(slider2.value, 10) +
    parseInt(slider3.value, 10) +
    parseInt(slider4.value, 10);