const express = require("express");
const router = express.Router();
const { spawn } = require("child_process");

router.get("/startscript", (req, res) => {
  const python = spawn("python3", ["Run.py"]);
  res.send("Script Executed");
  console.log("Request Recieved");
});

router.get("/resumescript", (req, res) => {
  const python = spawn("python3", ["Resume.py"]);
  res.send("Script Executed");
  console.log("Request Recieved");
});

router.get("/restartscript", (req, res) => {
  const python = spawn("python3", ["Restart.py"]);
  res.send("Script Executed");
  console.log("Request Recieved");
});

router.get("/", (req, res) => {
  res.send({ response: "Server is live" }).status(200);
});

module.exports = router;
