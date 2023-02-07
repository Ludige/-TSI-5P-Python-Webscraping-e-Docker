const express = require('express');
const app = express();

app.get('/', (req,res)=>{
    res.send("Olá!!");
});

app.listen(8080,()=>{
    console.log("Escutando a porta 8080");
})