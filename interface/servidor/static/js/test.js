var chart;
var chart2;
var mycharts;

$("#forward").on("touchstart", function () {
  // Code to execute when the forward button is pressed
  // Enviar una solicitud POST al servidor Flask
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "f" }), // Enviar la letra 'f' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "f" al servidor.');
      } else {
        console.error('Error al enviar la letra "f" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

$("#left").on("touchstart", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "l" }), // Enviar la letra 'f' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "l" al servidor.');
      } else {
        console.error('Error al enviar la letra "l" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

$("#right").on("touchstart", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "r" }), // Enviar la letra 'f' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "r" al servidor.');
      } else {
        console.error('Error al enviar la letra "r" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

$("#backward").on("touchstart", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "b" }), // Enviar la letra 'f' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "b" al servidor.');
      } else {
        console.error('Error al enviar la letra "b" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

$(".control-button").on("touchend", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "s" }), // Enviar la letra 's' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "s" al servidor.');
      } else {
        console.error('Error al enviar la letra "s" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});
$("#servo-right").on("touchstart", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "z" }), // Enviar la letra 's' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "z" al servidor.');
      } else {
        console.error('Error al enviar la letra "z" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

$("#servo-left").on("touchstart", function () {
  fetch("/action", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ key: "x" }), // Enviar la letra 's' como JSON al servidor
  })
    .then((response) => {
      if (response.ok) {
        console.log('Se envió la letra "s" al servidor.');
      } else {
        console.error('Error al enviar la letra "s" al servidor.');
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
});

// Code to execute when the forward button is pressed
// Enviar una solicitud POST al servidor Flask

document.addEventListener("keydown", function (event) {
  if (event.key === "w") {
    // Enviar una solicitud POST al servidor Flask
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "f" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "f" al servidor.');
        } else {
          console.error('Error al enviar la letra "f" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  } else if (event.key == "a") {
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "l" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "l" al servidor.');
        } else {
          console.error('Error al enviar la letra "l" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }

  if (event.key == "d") {
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "r" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "r" al servidor.');
        } else {
          console.error('Error al enviar la letra "r" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }

  if (event.key == "s") {
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "b" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "b" al servidor.');
        } else {
          console.error('Error al enviar la letra "b" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }

  if (event.key == "z") {
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "z" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "z" al servidor.');
        } else {
          console.error('Error al enviar la letra "z" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }

  if (event.key == "x") {
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "x" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "x" al servidor.');
        } else {
          console.error('Error al enviar la letra "x" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }
});

$(document).keyup(function (event) {
  var key = event.key;
  if (key) {
    $("#forward").css("color", "white");
    fetch("/action", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ key: "s" }), // Enviar la letra 'f' como JSON al servidor
    })
      .then((response) => {
        if (response.ok) {
          console.log('Se envió la letra "s" al servidor.');
        } else {
          console.error('Error al enviar la letra "s" al servidor.');
        }
      })
      .catch((error) => {
        console.error("Error de red:", error);
      });
  }
});

function requestData() {
  var requests = $.get("/data");
  var tm = requests.done(function (result) {
    var series = chart.series[0],
      shift = series.data.length > 20;

    chart.series[0].addPoint(result, true, shift);

    setTimeout(requestData, 100);

    var series2 = chart2.series[0],
      shift2 = series2.data.length > 20;

    chart2.series[0].addPoint(result, true, shift2);

    setTimeout(requestData, 10);
  });
}

$(document).ready(function () {
  chart = new Highcharts.Chart({
    chart: {
      renderTo: "data-container",
      defaultSeriesType: "spline",
      events: {
        load: requestData,
      },
    },
    title: {
      text: "Amity-Charts",
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: "Value",
        margin: 80,
      },
    },
    series: [
      {
        name: "Random data",
        data: [],
      },
    ],
  });
});

$(document).ready(function () {
  chart2 = new Highcharts.Chart({
    chart: {
      renderTo: "temperature-chart",
      defaultSeriesType: "spline",
      events: {
        load: requestData,
      },
    },
    title: {
      text: "Amity-Charts",
    },
    xAxis: {
      type: "datetime",
      tickPixelInterval: 150,
      maxZoom: 20 * 1000,
    },
    yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
        text: "Temperature",
        margin: 80,
      },
    },
    series: [
      {
        name: "Random data",
        data: [],
      },
    ],
  });
});
