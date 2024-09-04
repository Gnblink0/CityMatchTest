const City = require("../models/City");

exports.getAllCities = async (req, res) => {
  try {
    const cities = await City.find();
    res.json(cities);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.getCityById = async (req, res) => {
  try {
    const city = await City.findById(req.params.id);
    if (city == null) {
      return res.status(404).json({ message: "City not found" });
    }
    res.json(city);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

exports.createCity = async (req, res) => {
  const city = new City({
    name: req.body.name,
    country: req.body.country,
    population: req.body.population,
    // Add other fields as necessary
  });

  try {
    const newCity = await city.save();
    res.status(201).json(newCity);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

exports.updateCity = async (req, res) => {
  try {
    const city = await City.findById(req.params.id);
    if (city == null) {
      return res.status(404).json({ message: "City not found" });
    }

    if (req.body.name != null) {
      city.name = req.body.name;
    }
    if (req.body.country != null) {
      city.country = req.body.country;
    }
    if (req.body.population != null) {
      city.population = req.body.population;
    }
    // Update other fields as necessary

    const updatedCity = await city.save();
    res.json(updatedCity);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

exports.deleteCity = async (req, res) => {
  try {
    const city = await City.findById(req.params.id);
    if (city == null) {
      return res.status(404).json({ message: "City not found" });
    }

    await city.remove();
    res.json({ message: "City deleted" });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};
