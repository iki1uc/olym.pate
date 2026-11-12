function radicalize(layer) {
  const heads = [0,1,2].map(g => majority(layer.slice(g*3, g*3+3)));
  return heads.every(v => v === heads[0])
    ? Array(9).fill(heads[0])
    : heads.flatMap(v => [v,v,v]);
}
