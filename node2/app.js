'use strict';

module.exports.handler = async (event) => {
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        message: `This is from the node2 image`,
      },
      null,
      2
    ),
  };
};
