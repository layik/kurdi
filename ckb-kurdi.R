# get a fresh dump from Wikipedia
# then decompress
# library(data.table)
df = XML::xmlToDataFrame("~/Downloads/data.xml")
# df = as.data.table(df)
t = df$title

ku_v = readLines("https://raw.githubusercontent.com/layik/kurdi/master/corpus/letters_lines.txt")

title_chars = Reduce(function(x, y) unique(unlist(
  strsplit(paste0(x, y), ''))), t)
length(title_chars)

# only Kurdi chars
valid_chars = title_chars[title_chars %in% ku_v]
setdiff(valid_chars, ku_v)
setdiff(ku_v, valid_chars) # remember وو was split

# popularity
letters_used = sapply(ku_v, function(x){
  length(grep(x, t))
})

letters_used = sort(letters_used, decreasing = TRUE)
letters_used['ه']

unique(t[grep("ڤ", t)])[10:20]

library(ggplot2)
ggplot() + 
  geom_bar(aes(x=names(letters_used),y=letters_used), stat='identity') + 
  xlab('Alphabet') + ylab('Frequency') + 
  theme(axis.text.x = element_text(face = "bold", size = 18)) + 
  scale_y_continuous(labels = scales::comma) + 
  scale_x_discrete(limits=names(letters_used))
