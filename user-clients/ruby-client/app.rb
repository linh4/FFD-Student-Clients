require_relative "./MatrixManager.rb"
# require 'chunky_png'

matrix = MatrixManager.new

# Code here!
# ex. matrix.set_tile(x: 6, y: 4, c: "ffffff")
while true
  for i in 420..445
    for j in 470..495
      matrix.set_tile(x: i, y: j, c:"885577")
    end
  end
end
