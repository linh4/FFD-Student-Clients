const { MatrixManager } = require('./MatrixManager.js')

var teamID = 16

const matrix = new MatrixManager(teamID)

for(let x = 400; x < 500; x++){
  for(let y = 100; y < 200; y++){
    matrix.setTile({x: x, y: y, c: "FFB6C1"})
      .then(console.log)
  }
}




// Write your code here!
// all functions return a promise.
