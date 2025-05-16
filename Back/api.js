const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const cors = require('cors');

app.use(express.json());
app.use(cors());

app.post('/save-data', (req, res) => {

    try{
        const data = req.body;

        const filePath = path.join(__dirname, '../dataSearch.json');

        if( fs.existsSync(filePath)){
            console.log(data)
            fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
            res.send('Data saved successfully!');
        }
        else{
            fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
            console.log('File created and data written successfully.');
            res.send('File created and data written successfully.');

            ////CHAMAR O CMD PARA INICIAR O BUSCADOR
        }

    }
    catch(error){
        console.error('An error occurred:', error);
        res.status(500).send('An error occurred while saving data.');
    }
});

app.listen(3001, () => console.log('Server running on http://localhost:3001'));