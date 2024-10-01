import express from "express";
import fetch from "node-fetch"; // Ensure to import fetch if you're using Node.js

const app = express();

const PORT = 3000;

app.listen(PORT, async function () {
    try {
        const response = await fetch("http://127.0.0.1:8080", {
            headers: {
                // Broswer often add the Origin, Referer, Host. Mostly over HTTPS
                Origin: `http://localhost:${PORT}`, 
                Referer: `http://localhost:${PORT}/full/path`
            }
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
    console.log(`The server is listening at http://localhost:${PORT}`);
});
