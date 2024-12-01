library(tidyverse)

input = as.matrix(read.table("Day 1/input.txt", sep = ""))

sorted = apply(input, 2, sort)

subtracted = cbind(sorted,abs(sorted[,1]-sorted[,2]))

solution_1_A = sum(subtracted[,3])

#-------------------------------------------------------------------------------
df = as.data.frame(sorted)

count_v2 = df %>% count(V2)
unique_v1 = as.data.frame(unique(df$V1))

count_in_both_unique = unique_v1 %>% 
  mutate(unique_v1_c = `unique(df$V1)`) %>% 
  select(unique_v1_c) %>% 
  inner_join(.,count_v2, by = c("unique_v1_c" = "V2")) %>% 
  mutate(multiplied = unique_v1_c * n)

count_in_both = df %>% 
  select(V1) %>% 
  inner_join(.,count_v2, by = c("V1" = "V2")) %>% 
  mutate(multiplied = V1 * n)

solution_1_B = sum(count_in_both$multiplied, na.rm = TRUE)
