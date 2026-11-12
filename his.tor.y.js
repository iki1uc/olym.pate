const payload = {
  format: "WURZEL-Q-729",
  version: 2,
  created: new Date().toISOString(),
  dimensions: { cells: 81, layers: 3, rootsPerLayer: 9, total: 2187 },
  activeCell, activeLayer, zoom, roots,
  hash: computeHash(roots),
  history: history
};
