# Prompt Log — Atualização de Imagens no Relatório

## Date

2026-07-12

## Tool

Antigravity (Gemini)

## Goal

Copiar os novos gráficos gerados para a pasta `Report/` e inseri-los no arquivo `Report/relatorio.md` de forma inline.

## Prompt

```text
keep the @[ed-group1-avl-sosd-benchmark/Report/relatorio.md] updated, you can insert the images within (also present in the folder, which are the results)
```

## Result

1. Copiados os gráficos atualizados (`scale_comparison.png`, `order_comparison.png`, `theta_sensitivity.png`) para a pasta `Report/`.
2. Editado o arquivo `Report/relatorio.md` para incluir os marcadores markdown de imagem inline em suas respectivas seções.
3. Removido o arquivo duplicado `relatorio.md` na raiz para evitar redundância.

## Notes

- As imagens agora são referenciadas relativamente dentro da própria pasta `Report/`.
