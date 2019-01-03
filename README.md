# FDR-controlling-procedures

## A bref introduction
A python scipt about false discovery rate controlling procedure

`import fdrp.py`

### Procedures
Benjamini & Hochberg procedure

`bhp(p_values)`

Benjamini & Yekutieli procedure
To deal with too many true positives

`byp(p_values)`

Bonferroni correction (familywise error rate controlling procedure)

`bon(p_values)`

### reference
Benjamini, Y., and Yekutieli, D. (2001). The control of the false discovery rate in multiple testing under dependency. Annals of Statistics 29, 1165–1188.

