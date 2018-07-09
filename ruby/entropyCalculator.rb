class String
  def entropy
      self
      .each_char
      .group_by(&:to_s)
      .values
      .map { 
        |x| 
        x.length / self.length.to_f 
      }.reduce(0) { 
        |e, x| 
        e - x * Math.log2(x) 
      }
  end
end


words = [
  "aba17a8c1041b4b4", 
  "fT$e-'U_78~Ol:yNp", 
  "aaaaaaaaaaaaaaaa", 
  "password", 
  "caro sempre fu quest ermo colle e questa siepe che tanta parte del guardo esclude", 
  "Mario1968", 
  "Gennaio2017", 
  "Nullam id dolor id nibh ultricies vehicula ut id elit.",
  "correct horse battery staple", 
  "correct horse battery staple!", 
  "correct horse battery staple123", 
  "correct horse battery staple123!"
]

words.each do |w|
  print 'entropy("%s") #=> %f' % [w, w.entropy]
  print "\n"
end

