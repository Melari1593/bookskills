# Recetas de profundidad y relieve

## Bajorrelieve CSS
Aplicar sombras internas clara y oscura, gradiente sutil y fondo similar al contenedor. Ajustar dirección de luz consistentemente.

```css
.relief-inset {
  background: linear-gradient(145deg, #f4f0e8, #e9e3da);
  box-shadow: inset 3px 3px 6px #d5cfc6, inset -3px -3px 6px #fffdf8;
}
```

## Altorrelieve CSS
```css
.relief-raised {
  background: #f2ede5;
  box-shadow: 4px 4px 9px #d8d1c7, -4px -4px 9px #ffffff;
}
```

## SVG
Usar paths originales con gradientes y filtros feGaussianBlur, feOffset y feComposite cuando sea necesario. No incrustar logos ajenos.

## Rendimiento y accesibilidad
No aplicar blur pesado a grandes superficies; medir en móvil. Evitar animar filtros costosos. Respetar `prefers-reduced-motion`. Mantener contraste y foco visibles.

Estas recetas son opcionales: elegir técnicas según la imagen, no imponer estética de porcelana.
