"""West sdk commands"""

import argparse

from west import log
from west.commands import WestCommand, CommandError

SDK_DESCRIPTION = """\
West SDK installer helper.

This command can be used to install Zephyr SDKs.

By default, it will install the latest Zephyr SDK to ~/zephyr-sdks .

See --help for options.
"""
from pathlib import Path

# Note:
#
# As of 2022-06-10, there are 3 different Zephyr SDK installation methods:
#
# 1. https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.10.0
#    Single installer; need to test if it works on linux/macos
# 2. https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.11.0
#    Installers are split into per-target versions, but there's still an "all" version
# 3. https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.14.0
#    Adds a "bundle" installer, which lets you pick which SDKs to install.


DEFAULT_INSTALL_LOCATION = Path.home() / "zephyr-sdks"

class Sdk(WestCommand):
    def __init__(self):
        super().__init__(
            "sdk", "install Zephyr SDKs", SDK_DESCRIPTION, requires_workspace=False
        )

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(
            self.name,
            help=self.help,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description=self.description,
        )

        parser.add_argument(
            "-l", "--list", action="store_true", help="list installed SDKs"
        )
        # parser.add_argument("--uninstall", help="uninstall an installed SDK")
        parser.add_argument("--sdk-version", help="install a particular Zephyr SDK version")
        parser.add_argument(
            "-t", "--toolchain", help='install a particular toolchain instead of "all"'
        )
        parser.add_argument(
            "-h", "--install-host-tools", help="install host tools", action="store_true"
        )
        parser.add_argument("--location", help="install location", default=DEFAULT_INSTALL_LOCATION)

        return parser

    def do_run(self, args, user_args):
        if args.list:
            self.list(args)
        elif args.uninstall:
            self.uninstall(args)
        elif args.value is None:
            self.read(args)
        else:
            self.write(args)

    def list(self, args):
        what = args.configfile or ALL
        for option, value in self.config.items(configfile=what):
            log.inf(f"{option}={value}")

    def uninstall(self, args):
        pass

    def install(self, args):
        pass
