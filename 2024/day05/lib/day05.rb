def validate(rev_rules, pages, page, idx)
  (idx..pages.size).each do |i| 
    return false if rev_rules[page].include? (pages[i])
  end
  true
end

def validate_upd(pages, rev_rules)
  pages.each_with_index do |page, idx|
    return false if !validate(rev_rules, pages, page, idx)
  end
  true
end

def part_1(rev_rules, updates)
  sum_p1 = 0

  invalid = updates.split("\n").delete_if do |upd|
    pages = upd.split(",")
    if validate_upd(pages, rev_rules)
      sum_p1 += Integer(pages[pages.size / 2])
      true
    end
  end

  puts "part 1 => #{sum_p1}"

  invalid
end

def part_2(rev_rules, invalid)
  sum_p2 = 0

  invalid.each do |upd|
    pages = upd.split(",")
    pages.delete_if.with_index do |page, idx|
      if !validate(rev_rules, pages, page, idx)
        pages << page
        true
      end
    end
    sum_p2 += Integer(pages[pages.size / 2])
  end

  puts "part 2 => #{sum_p2}"
end

#---------------------------------------------------------------------------#

ordering, updates = File.read("./lib/input.txt").split("\n\n")

rev_rules = Hash.new{|hsh, key| hsh[key] = []}

ordering.split("\n").each do |rule|
  v1, v2 = rule.split("|")
  rev_rules[v2] << v1
end

part_2(rev_rules, part_1(rev_rules, updates))