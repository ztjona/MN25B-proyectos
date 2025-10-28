# Proyecto Blackbox *S*

La red neuronal **Blackbox *S*** es una función paramétrica $f_\theta:\mathbb{R}^2 \rightarrow \mathbb{B}; (x_1, x_2) \mapsto f(x_1, x_2) \forall x_1 \ge 0$.

Ejecute el siguiente código para cargar el modelo y predecir la salida de un punto $(x_1, x_2)$.

```python
from Blackbox import load_model, predict_point
model = load_model()
predict_point(model, 0.2, 0.4)
```
Output:
```
1.0
```
# Objetivo
* Determine la relación analítica entre $x_1$ y $x_2$.
* Utilice y compare dos métodos numéricos para aproximar dicha relación.

# Instrucciones
Instale las dependencias:
```bash
$ pip install -r requirements.txt
```

Más ejemplos en [este notebook](blackbox_s.ipynb).