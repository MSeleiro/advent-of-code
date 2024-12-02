# frozen_string_literal: true

$safe_p1 = 0
$safe_p2 = 0

def verify(report)
  func = if report[0] > report[1] then lambda {|l1,l2| (l1 - l2)} else lambda {|l1,l2| (l2 - l1)} end
  
  report.each_cons(2).all? { |l1,l2| func.call(l1,l2).between?(1 ,3) }
end

def manipulate(report, arr_err)
  if arr_err.count(false).between?(1,2)
    err_idx = arr_err.index(false)
    val = report.delete_at(err_idx)
    
    if verify(report)
      $safe_p2 += 1
    else
      val = report.insert(err_idx, val).delete_at(err_idx + 1)

      $safe_p2 += (verify(report) ? 1 : 0 )
      
      report.insert(err_idx + 1, val)
    end
  end
end

def part_1(report)
  if verify(report)
    $safe_p1 += 1
    $safe_p2 += 1
  end
end

def part_2(report)
  err_dec = []
  err_inc = []
  
  report.each_cons(2) do |l1,l2|
    err_dec.append((l1 - l2).between?(1,3))
    err_inc.append((l2 - l1).between?(1,3))
  end

  manipulate(report, err_dec)
  manipulate(report, err_inc)
end

File.open("./lib/input.txt", "r") do |f|
  f.each_line do |line|
    report = line.strip.split(' ').map(&:to_i)
    part_1(report)
    part_2(report)
  end
end

puts "part 1 => #{$safe_p1}"
puts "part 2 => #{$safe_p2}"
