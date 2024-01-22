# Given 3 positive integers (k = # homozygous dom, m = # heterozygous, n = # homozygous recessive individuals in a population)
# Return the probabilty 2 randomly selected organisms will produce an offspring with a dominant allele (thus displaying the dominant phenotype). Assume that any two organisms can mate.


def calculateDomPhenotype(k, m, n):
  total_pop = k + m + n
  double_hetero = float(m / total_pop) * float(
    (m - 1) / (total_pop - 1)) * float(1 / 4)

  double_rec = float(n / total_pop) * float((n - 1) / (total_pop - 1))

  hetero_x_rec = float(m / total_pop) * float(n /
                                              (total_pop - 1)) * float(1 / 2)

  rec_x_hetero = float(n / total_pop) * float(m /
                                              (total_pop - 1)) * float(1 / 2)

  rec_pheno = double_hetero + double_rec + hetero_x_rec + rec_x_hetero

  return 1 - rec_pheno


print(calculateDomPhenotype(20, 30, 29))
