def part_1(memory)
  memory.scan(/mul\(\d{1,3},\d{1,3}\)/).map { |mul| mul.scan(/\d{1,3}/).map(&:to_i).inject(:*) }.inject(:+)
end

def part_2(line)
  discard = false

  func = lambda do |val|
    discard = val == "don't()" ? true : val == "do()" ? false : discard
    val == "do()" ? true : discard
  end

  line.scan(/mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)/).reject { |mul| func.call(mul) }.map { |mul| mul.scan(/\d{1,3}/).map(&:to_i).inject(:*) }.inject(:+)
end

memory = File.read("./lib/input.txt") 

puts "part 1 => #{part_1(memory)}"
puts "part 2 => #{part_2(memory)}"
