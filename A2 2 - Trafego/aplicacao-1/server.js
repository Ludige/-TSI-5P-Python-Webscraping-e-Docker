const express = require('express');

const redis = require('redis');
const redisClient = redis.createClient({
    host: 'test-redis',
    port: 6379
});

const app = express();
app.get('/', function(req,res){
    redisClient.get('numVisits', function(err, numVisits){
        numVisitsToDisplay = parseInt(numVisits) + 1;

        if(isNaN(numVisitsToDisplay)){
            numVisitsToDisplay = 1;
        }
        res.send('App 1: O numero de visitantes é: ' + numVisitsToDisplay);
        redisClient.set('numVisits', numVisitsToDisplay);
    });
});

app.listen(4001, function(){
    console.log("Escutando porta 4001");
});