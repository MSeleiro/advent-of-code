def matches(arr, pattern)
  arr.scan(pattern).size
end

def diagonal(letters, size, t)
  ret = ""
  (0..size * 2 - 1).each do |k|
    (0..k).each do |j|
      i = k - j
      if i < size && j < size
        ret << letters[i][(t - j).abs]
      end
    end
    ret << " "
  end
  ret.strip
end

def diagonals(letters)
  return diagonal(letters, letters.size, 0), diagonal(letters, letters.size, letters.size - 1)
end

def part_1(puzzle)
  num_p1 = matches(puzzle, /(?=(XMAS|SAMX))/) # horizontal
  letters = puzzle.split("\n").map { |line| line.strip.chars }
  num_p1 += matches(letters.transpose.map { |line| line.join }.join(' '), /(?=(XMAS|SAMX))/) # verical
  num_p1 += diagonals(letters).map { |diag| matches(diag, /(?=(XMAS|SAMX))/) }.inject(:+) # diagonals
  p "part 1 => #{num_p1}"
end

def part_2(puzzle)
  num_p2 = 0

  letters = puzzle.split("\n").map { |line| line.strip.chars }

  letters.each_cons(3) do |l1,l2,l3|
    l2.each_index.select { |i| l2[i] == 'A' }.each do |i|
      if i > 0 && i < letters.size - 1
        num_p2 += matches("#{l1[i-1]}#{l1[i+1]}#{l3[i-1]}#{l3[i+1]}", /(?=(MMSS|MSMS|SMSM|SSMM))/)
      end
    end
  end

  p "part 2 => #{num_p2}"
end

puzzle = File.read("./lib/input.txt")

part_1(puzzle)
part_2(puzzle)