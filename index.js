// Require the necessary discord.js classes
const { Client, Intents } = require('discord.js');
const { token } = require('./pythonDIR/config.json');
const util = require("util");

const py = "../watchComment/venv/bin/python3.8"
const spawn = require('child_process').spawn;
const python = spawn(py,["main.py"]);
python.stdout.on('data', function(result) {
	let resultText = result.toString('utf-8');
	console.log(resultText);
});
python.stderr.on('data', function(data) {
    nosuccess(data);
});

// Create a new client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

// When the client is ready, run this code (only once)
client.once('ready', () => {
	console.log('Ready!');
});

client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const { commandName } = interaction;

	if (commandName === 'ping') {
		await interaction.reply('Pong!');
	} else if (commandName === 'status') {
		await interaction.reply('이상 없음');
	} else if (commandName === 'user') {
		await interaction.reply('User info.');
	}
});

// Login to Discord with your client's token
client.login(token);