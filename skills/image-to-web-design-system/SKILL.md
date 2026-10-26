---
name: image-to-web-design-system
version: 1.0.0
description: Convierte cualquier imagen o diseño en un sistema de diseño web reutilizable con componentes originales, SVG, CSS, relieves y animaciones.
---
# Image to Web Design System

## Activación
Utilizar cuando se proporciona una fotografía, ilustración, captura, referencia de marca o diseño y se solicita una página web o componentes visuales.

## Entradas
- Imagen(es) de referencia.
- Objetivo, público y contenido, cuando se conozcan.
- Stack opcional; predeterminado React + TypeScript + CSS.
- Fidelidad: inspiración original por defecto; reconstrucción únicamente cuando esté autorizada.

## Procedimiento
1. Analizar composición, jerarquía, color, tipografía, formas, texturas, materiales, luz y profundidad.
2. Distinguir hechos observables de estimaciones; no inventar fuentes o medidas exactas.
3. Extraer tokens: paleta aproximada HEX, tipografía, escala, espacios, radios, sombras, capas y animaciones.
4. Identificar motivos decorativos y controles funcionales. Elegir SVG, CSS, recursos originales, Canvas o WebGL según complejidad.
5. Diseñar ilustraciones y elementos originales. Evitar copiar marcas, logotipos y activos protegidos sin autorización.
6. Construir componentes semánticos y reutilizables con props tipadas, estados, variantes y navegación por teclado.
7. Implementar bajorrelieve, altorrelieve o texturas solo si la imagen lo requiere; combinar luces, sombras y filtros SVG moderados.
8. Añadir movimiento opcional y respetar prefers-reduced-motion.
9. Aplicar diseño mobile-first y revisar a 360, 768 y 1440 px.
10. Validar accesibilidad WCAG AA, rendimiento, contraste, foco, texto alternativo y desbordamientos.

## Entregables
- design-analysis.md: observaciones, inferencias y decisiones.
- design-tokens.json y/o CSS variables.
- Componentes React + TypeScript y assets SVG originales.
- Demo responsive con instrucciones de instalación.
- Nota de limitaciones de fidelidad y derechos de uso.

## Reglas
- No afirmar equivalencia píxel a píxel sin validación.
- No usar imágenes externas sin licencia apropiada.
- No transformar contenido meramente visual en supuestas funcionalidades.
- Evitar parallax pesado y efectos que afecten accesibilidad.
- Mantener componentes independientes de un estilo específico.
- Si se necesita reconstrucción exacta de una marca, confirmar derechos de uso.
