#include <Rcpp.h>
#include <math.h>
using namespace Rcpp;


// [[Rcpp::export]]
int divisor_count_c(int n, LogicalVector primes) {
  
  int total = 1;
  int p_max = primes.size();
  int counter, n_t;
  
  for (int i = 2; i < p_max; i++) {
    if (primes[i]) {
      // Rcout << "prime: " << i << ". ";
      counter = 0;
      if (n % i == 0) {
        n_t = n;
        while (n_t % i == 0) {
          // Rcout << n_t << " ";
          n_t /= i;
          counter++;
        }
        total *= (counter + 1);
      }
      // Rcout << "n = " << n << ". ";
    }
  }
  
  return total;
  
}

// [[Rcpp::export]]
LogicalVector get_sieve_c(int n) {
  
  LogicalVector primes(n, true);
  primes[0] = false;
  primes[1] = false;

  for (int i=2; i*i<n; i++) { 
    if (primes[i] == true) { 
      for (int j=i*i; j<n; j += i) 
        primes[j] = false; 
    } 
  }
  
  return primes;
  
}

// [[Rcpp::export]]
int p12_c(int divisors) {

  int n = 3;
  int t_n = 6;
  LogicalVector primes = get_sieve_c(10000);  // hardcoded, idk

  while (divisor_count_c(t_n, primes) < divisors) {
    n++;
    t_n += n;
  }

  return t_n;

}


