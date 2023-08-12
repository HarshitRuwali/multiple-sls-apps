console.log('Loading function');

exports.handler = async (event, context) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));
    console.log('value1 =', event.key1);
    console.log('value2 =', event.key2);
    console.log('value3 =', event.key3);
    return {
      statusCode: 200,
      body: JSON.stringify(
        {
          message: `This is from the node1 image`,
        },
        null,
        2
      ),
    }; // Echo back the first key value
    // throw new Error('Something went wrong');
};
