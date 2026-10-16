"""Delega la interfaz de línea de comandos en el Graphify original."""


def main() -> None:
    from graphify.__main__ import main as upstream_main

    upstream_main()


if __name__ == "__main__":
    main()
