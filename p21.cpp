#include <Rcpp.h>
using namespace Rcpp;

// This is a simple example of exporting a C++ function to R. You can
// source this function into an R session using the Rcpp::sourceCpp 
// function (or via the Source button on the editor toolbar). Learn
// more about Rcpp at:
//
//   http://www.rcpp.org/
//   http://adv-r.had.co.nz/Rcpp.html
//   http://gallery.rcpp.org/
//

// [[Rcpp::export]]
int get_sum_proper_divisors(int n) {
  
  int out = 1;
  int i = 2;
  
  for(i = 2; i <= floor(sqrt(n)); i++) {
    if (n % i == 0) {
      out += i;
      if (n/i != i) {
        out += (n/i);
      }
    }
  }
  
  return out;
  
}

// [[Rcpp::export]]
int p21_c(int n) {
  
  int pd_sums[n + 1];
  
  for (int i = 2; i <= n; i++) {
    pd_sums[i] = get_sum_proper_divisors(i);  
  }
  
  std::unordered_set<int> amicable_numbers;
  
  for (int i = 2; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      if (i == pd_sums[j] && j == pd_sums[i]) {
        amicable_numbers.insert(i);
        amicable_numbers.insert(j);
      }  
    }
  }
  
  return(std::accumulate(amicable_numbers.begin(), amicable_numbers.end(), 0));
  
}