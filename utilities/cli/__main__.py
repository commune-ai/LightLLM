# Licensed under the Apache License, Version 2.0 (the "License");
#     http://www.apache.org/licenses/LICENSE-2.0
#
import fire

from utilities.cli.dependencies import prune_pkgs_in_requirements, replace_oldest_ver


def main() -> None:
    """CLI entry point."""
    fire.Fire({
        "requirements": {
            "prune-pkgs": prune_pkgs_in_requirements,
            "set-oldest": replace_oldest_ver,
        }
    })


if __name__ == "__main__":
    main()
