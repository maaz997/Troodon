const express = require("express");
// const bodyParser = require('body-parser')
const path = require("path");
const http = require("http");
const app = express();
app.use(express.static(path.join(__dirname, "build")));
const fs = require("fs");
const socketIo = require("socket.io");
const index = require("./routes.js");
var parse = require("csv-parse");
const PORT = 8080;

app.use(index);
const server = http.createServer(app);

const io = socketIo(server);

let interval;

io.on("connection", (socket) => {
  console.log("New client connected");
  if (interval) {
    clearInterval(interval);
  }
  interval = setInterval(() => getApiAndEmit(socket), 1000);
  socket.on("disconnect", () => {
    console.log("Client disconnected");
    clearInterval(interval);
  });
});

const getApiAndEmit = (socket) => {
  // const response = new Date();
  let dataResponse = [];
  let historyResponse = [];
  let executionResponse = [];
  let modelResponse = [];
  fs.readFile(
    "./TroodonParts/Data/1/Execution_Data.csv",
    function (err, fileData) {
      parse(fileData, { columns: false, trim: true }, function (err, rows) {
        executionResponse = [...executionResponse, rows];
        socket.emit("ExecutionData", executionResponse);
      });
    }
  );
  fs.readFile(
    "./TroodonParts/Data/2/Classification_data.csv",
    function (err, fileData) {
      parse(fileData, { columns: false, trim: true }, function (err, rows) {
        modelResponse = [...modelResponse, rows];
        socket.emit("ModelData", modelResponse);
      });
    }
  );
  fs.readFile(
    "./TroodonParts/Data/3/Exec_History.csv",
    function (err, fileData) {
      parse(fileData, { columns: false, trim: true }, function (err, rows) {
        historyResponse = [...historyResponse, rows];
        socket.emit("HistoryData", historyResponse);
      });
    }
  );

  // Emitting a new message. Will be consumed by the client
};

server.listen(PORT, () => console.log(`Listening on port ${PORT}`));
// app.listen(PORT);
