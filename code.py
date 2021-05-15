Criar uma matriz nxm (n = 5, m =7)
a. faça a matriz transposta desta matriz
import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])
print(x)

b. somar toda matrix
import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])
x.sum()

c.somar todas as colunas
  import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])
x.sum(axis=0)

d.somar todas as linhas.
import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])
x.sum(axis=1)

e. retorne o maior valor
import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])

f.retorne o menor valor. 
import numpy as np
x = np.array([(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7)])
x.min()


