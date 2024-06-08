require("dotenv").config();
const express = require("express");
require("express-async-errors");
const cors = require("cors");

const { OpenAI } = require("openai");
const app = express();

const openai = new OpenAI();

app.use(cors({ origin: "*" }));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.post("/api/generate-ai", async (req, res) => {
  console.log(req.body);
  const prompt = req.body.prompt;
  const temperature = req.body.temperature;
  const completion = await openai.chat.completions.create({
    temperature,
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: prompt },
    ],
    model: "gpt-3.5-turbo",
  });

  console.log(completion);

  res.json({ content: completion.choices[0].message.content });
});

app.listen(3000, () => {
  console.log("api is up in port 3000");
});
