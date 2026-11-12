function initialState(index) {
  return (index * 2654435761 >>> 9) % STATES.length;
}
