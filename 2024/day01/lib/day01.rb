# frozen_string_literal: true

list1 = []
list2 = []

File.open("./lib/input.txt", "r") do |f|
  f.each_line do |line|
    nums = line.strip.split('   ')
    list1 << Integer(nums[0])
    list2 << Integer(nums[1]) 
  end
end

def part_1(list1, list2)
  l1 = list1.sort
  l2 = list2.sort

  sum = 0

  l1.each_with_index { |val, index| sum += (val - l2[index]).abs }

  puts "part 1 => #{sum}"
end

def part_2(list1, list2)
  hash = list2.tally
  hash.default = 0

  sum = 0

  list1.each { |val| sum += (val * hash[val]) }

  puts "part 2 => #{sum}"
end

part_1(list1, list2)
part_2(list1, list2)
