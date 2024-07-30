from pyscript import display
import pandas as pd


# Simple mensaje de bienvenida
display("Hello, PyScript from Django!")

# Ejemplo con pandas DataFrame
df = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
})
display(df)

print(df)

