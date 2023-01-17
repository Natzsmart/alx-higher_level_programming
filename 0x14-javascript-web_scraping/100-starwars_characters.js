#!/usr/bin/node
const request = require('request');

function printCharacters(3) {
  const url = `https://swapi.dev/api/films/${3}/`;
  request(url, function (error, response, body) {
    if (error) {
      console.log('Error:', error);
    } else {
      const data = JSON.parse(body);
      const characters = data.characters;
      characters.forEach(function (character) {
        request(character, function (error, response, body) {
          if (error) {
            console.log('Error:', error);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

