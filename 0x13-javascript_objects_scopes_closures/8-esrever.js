exports.esrever = function (list) {
  list = [];
  const aar1 = [];
  list.forEach(element => {
    aar1.unshift(element);
  });
  return (aar1);
};
