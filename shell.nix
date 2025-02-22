{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs =
    [ pkgs.python312 pkgs.python312Packages.flask pkgs.nodePackages.vercel ];
}
