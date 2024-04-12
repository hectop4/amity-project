const express = require("express");
const app = express();

// Ruta principal que envía la página HTML
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

// API para obtener un número aleatorio
app.get("/random", (req, res) => {
  const randomNumber = Math.floor(Math.random() * 100); // Genera un número aleatorio entre 0 y 99
  res.json({ number: randomNumber }); // Envía el número aleatorio como JSON
});

// Iniciar el servidor en la dirección 127.0.0.1 en el puerto 3000
const port = 3000;
app.listen(port, "127.0.0.1", () => {
  console.log(`Servidor escuchando en http://127.0.0.1:${port}`);
});
