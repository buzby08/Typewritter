{pkgs}: {
  deps = [
    pkgs.unzip
    pkgs.openal
    pkgs.libpulseaudio
    pkgs.libGLU
    pkgs.libGL
    pkgs.gtk2-x11
    pkgs.gdk-pixbuf
    pkgs.freetype
    pkgs.fontconfig
    pkgs.ffmpeg-full
    pkgs.xvfb-run
    pkgs.scrot
  ];
}
