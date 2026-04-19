# Contributing Guide

Gracias por contribuir a este proyecto.

## Alcance

Este repositorio contiene un trabajo academico reproducible basado en notebooks y un script de carga de datos. Las contribuciones deben mejorar claridad, mantenibilidad o reproducibilidad sin alterar el objetivo analitico del trabajo.

## Requisitos Previos

1. Usar Python 3.12+.
2. Crear y activar entorno virtual.
3. Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

## Flujo Recomendado

1. Crea una rama desde `main` con nombre descriptivo.
2. Realiza cambios pequenos y atomicos.
3. Escribe commits claros en imperativo.
4. Abre una pull request con contexto y validacion.

## Estilo De Cambios

- Respeta la estructura actual de carpetas y nombres.
- No incluyas refactors no relacionados.
- No subas archivos temporales, caches ni checkpoints.
- Si cambias documentacion, verifica rutas y comandos.

## Checklist Antes De Abrir PR

1. `requirements.txt` refleja dependencias reales usadas.
2. README y documentacion siguen siendo consistentes.
3. El flujo de ejecucion de notebooks se mantiene reproducible.
4. No se han anadido archivos locales accidentales.

## Pull Request

Incluye en la descripcion:

- Resumen breve de cambios.
- Motivacion del cambio.
- Validacion realizada.
- Impacto esperado (si aplica).

Al enviar una contribucion, aceptas que se distribuya bajo la licencia del repositorio (MIT).
