{ pkgs }: {
    deps = [
        pkgs.unixtools.ping
        pkgs.python39Packages.flask
        pkgs.python39Packages.pip
        pkgs.cowsay
    ];
}