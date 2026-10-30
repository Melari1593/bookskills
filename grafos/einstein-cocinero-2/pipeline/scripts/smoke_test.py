#!/usr/bin/env python3
"""Prueba visual del HTML generado: carga la página en Chromium (Playwright),
recorre las tres vistas, busca un término, abre su panel y traza prerrequisitos.
Falla si hay errores de JavaScript. Deja capturas para revisarlas con Read.

Uso:
  python smoke_test.py grafo.html carpeta_capturas/ [--buscar "darcy"]

Si el HTML carga d3 desde la CDN y no hay internet, constrúyelo con
build_graph.py --d3 ruta/d3.min.js (npm i d3@7 deja el archivo en
node_modules/d3/dist/d3.min.js).
"""
import argparse, asyncio, os, sys


async def run(html, outdir, term):
    from playwright.async_api import async_playwright
    os.makedirs(outdir, exist_ok=True)
    url = "file://" + os.path.abspath(html)
    errs = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, vp in [("escritorio", {"width": 1280, "height": 800}), ("movil", {"width": 390, "height": 760})]:
            pg = await b.new_page(viewport=vp)
            pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto(url)
            await pg.wait_for_timeout(1500)
            n = await pg.locator("g.node").count()
            print(f"[{name}] nodos en la vista de capítulos: {n}")
            await pg.screenshot(path=f"{outdir}/{name}_1_capitulos.png")
            for view, wait in (("eq", 3000), ("all", 3500)):
                await pg.click(f"[data-view={view}]")
                await pg.wait_for_timeout(wait)
                await pg.screenshot(path=f"{outdir}/{name}_2_{view}.png")
            if term:
                await pg.fill("#q", term)
                await pg.wait_for_timeout(300)
                if await pg.locator("#results [data-go]").count():
                    await pg.click("#results [data-go]")
                    await pg.wait_for_timeout(1800)
                    if await pg.locator("#traceBtn").count():
                        await pg.click("#traceBtn")
                        await pg.wait_for_timeout(1200)
                    await pg.screenshot(path=f"{outdir}/{name}_3_traza.png")
                else:
                    print(f"[{name}] la búsqueda '{term}' no dio resultados")
        await b.close()
    for e in errs:
        print("ERROR JS:", e)
    print("OK" if not errs else "FALLÓ")
    return 1 if errs else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("outdir")
    ap.add_argument("--buscar", default="")
    a = ap.parse_args()
    sys.exit(asyncio.run(run(a.html, a.outdir, a.buscar)))
