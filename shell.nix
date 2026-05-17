{ pkgs ? import <nixpkgs> {
    config.allowUnfree = true;
    config.cudaSupport = true;
  }
}:

pkgs.mkShell rec {
  name = "comfyui-gpu";

  buildInputs = with pkgs; [
    git
    python311
    stdenv.cc.cc.lib
    gcc
    ncurses5
    binutils
    gnumake
    unzip
    libGL
    libGLU
    glib
    zlib
    curl

    # CUDA
    cudaPackages.cudatoolkit
    linuxPackages.nvidia_x11

    # X11 / graphics libs PyTorch & friends often link against
    xorg.libXi
    xorg.libXmu
    xorg.libXext
    xorg.libX11
    xorg.libXv
    xorg.libXrandr
    xorg.libxcb
    freeglut
  ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath buildInputs;
  CUDA_PATH = pkgs.cudaPackages.cudatoolkit;
  EXTRA_LDFLAGS = "-L${pkgs.linuxPackages.nvidia_x11}/lib";

  shellHook = ''
    export SSL_CERT_FILE="/etc/ssl/certs/ca-certificates.crt"
  '';
}
