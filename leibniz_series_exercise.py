def approximate_pi(n_terms):
  apx_pi = 0
  for i in range(n_terms):
     apx_pi += ((-1)**i)/(2*i +1)*4

  return apx_pi

