const LANDSCAPE = "landscape";
const PORTRAIT = "potrait";

export const getCurrentOrientation = () => {
  return window.matchMedia(`(orientation: ${PORTRAIT})`).matches ? PORTRAIT : LANDSCAPE;
}

