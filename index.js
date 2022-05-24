// Require the necessary discord.js classes
const { Client, Intents } = require('discord.js');
const { token } = require('./pythonDIR/config.json');
let resultText;
let forceText = "Only for Test";

const py = "../watchComment/venv/bin/python3.8"
const spawn = require('child_process').spawn;
const python = spawn(py,["main.py"]);
python.stdout.on('data', function(result) {
	resultText = result.toString('utf-8');
});
python.stderr.on('data', function(data) {
    console.log('Python error!');
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
		await interaction.reply(resultText);
	} else if (commandName === 'status') {
		await interaction.reply(forceText);
	} else if (commandName === 'user') {
		await interaction.reply('User info.');
	}
});

// Login to Discord with your client's token
client.login(token);