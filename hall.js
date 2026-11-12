function assertPayload(data) {
  if (!data || typeof data !== "object") throw Error("JSON muss ein Objekt sein.");
  if (data.format !== "WURZEL-Q-729") throw Error("Unbekanntes Datenformat.");
  if (data.version !== 2) throw Error("Nicht unterstützte Version.");
  if (data.dimensions.cells !== 81 || data.dimensions.layers !== 3 ||
      data.dimensions.rootsPerLayer !== 9 || data.dimensions.total !== 2187)
    throw Error("dimensions müssen 81 x 3 x 9 = 2187 sein.");
  assertState(data.roots);
  if (!Number.isInteger(data.activeCell) || data.activeCell < 0 || data.activeCell > 80)
    throw Error("activeCell muss zwischen 0 und 80 liegen.");
  if (!Number.isInteger(data.activeLayer) || data.activeLayer < 0 || data.activeLayer > 2)
    throw Error("activeLayer muss zwischen 0 und 2 liegen.");
  if (!ZOOMS.includes(data.zoom)) throw Error("Ungültige Zoomstufe.");
}
