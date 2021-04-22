const express = require("express");
const router = express.Router();
const { spawn } = require("child_process");

router.get("/script", (req, res) => {
  const python = spawn("python3", ["Run.py"]);
  res.send("Script Executed");
  console.log("Request Recieved");
});

router.get("/", (req, res) => {
  res.send({ response: "I am alive" }).status(200);
});

module.exports = router;
