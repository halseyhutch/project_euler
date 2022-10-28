library(Rcpp)
library(bench)

#### Helpers ####

get_sieve <- function(n) {
  stopifnot(n > 4)
  integers <- 2:n
  p <- 2
  while(p < sqrt(n)) {
    integers <- integers[integers %% p != 0 | integers == p]
    p <- integers[which(integers == p) + 1]
  }
  return(integers)
}


divisor_count <- function(n, primes) {
  
  total <- 1
  
  for (p in primes) {
    counter <- 0
    if (n %% p == 0) {
      n_t <- n
      while (n_t %% p == 0) {
        n_t = n_t/p
        counter <- counter + 1
      }
      total = total * (counter + 1)
    }
  }
  
  return(total)
  
}


#### Problems ####

p12_r <- function(divisors) {
  primes_cached <- get_sieve(10000)
  numbers <- 5:20000  # skip the first few since my sieve is annoying on those
  triangle_numbers <- unlist(lapply(numbers, function(x) sum(1:x)))
  div_counts <- unlist(lapply(triangle_numbers, function(x) divisor_count(x, primes_cached)))
  return(triangle_numbers[which(div_counts > divisors)[1]])
}

sourceCpp("p12.cpp")
# p12_c(6)

mark(
  p12_r(500),
  p12_c(500)
)




sourceCpp("p21.cpp")

mark(p21_c(10000))
