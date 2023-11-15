const express = require("express");
const router = express.Router();

const data_db = require('./.data_db.js');

const { Sequelize, DataTypes } = require("sequelize");
const { status } = require("express/lib/response");
console.log("data", data_db, data_db.username)
const sequelize = new Sequelize(
  data_db.database,
  data_db.username,
  data_db.password,
  {
    dialect: "mysql",
    host: "localhost",
    port: data_db.port,
  }
);

try {
  console.log("Trying to connect to MySql database...");
  sequelize.authenticate();
  console.log("Connected to MySql database!");
} catch (error) {
  console.error("Unable to connect", error);
}

router.use((req, res, next) => {
  next();
});

module.exports = router;