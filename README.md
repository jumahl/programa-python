# programa-python

Ejercicio académico de Python — clasificación de nivel de compromiso de sesiones de clientes.

## Descripción

El programa toma una matriz con datos de sesiones (ID Cliente, duración en segundos, eventos clics) y clasifica cada una en **Alto**, **Medio** o **Bajo** según las siguientes reglas:

- **Alto**: duración > 180s y clics > 8
- **Bajo**: duración < 60s o clics < 3
- **Medio**: cualquier otro caso

Genera un informe tabulado con el ID y su clasificación.

## Uso

```bash
python F5_ejercicio_1.py
```

## Autor

Juan Manuel Hernandez Loaiza — Ingeniería de Sistemas  
Grupo: 213022_225
