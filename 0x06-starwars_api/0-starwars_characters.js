#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
// A callback function that is called when the request is completed
request(url, async function (error, response, body) {
  // If an error occurred, print it and quit
  if (error) {
    console.log(error);
  } else {
    // Parse the body of the response
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await new Promise((resolve, reject) => {
        request(character, (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
