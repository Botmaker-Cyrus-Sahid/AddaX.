const { Client, GatewayIntentBits } = require("discord.js");
const { DisTube } = require("distube");

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildVoiceStates,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

const distube = new DisTube(client);

const TOKEN ="MTUxNzE3NjAzNjc4MDE0NjY5OA.G3duOi.c_pLT6d8sc7rvM91NK7wtkaUyCZdfz9lFmpgYY";

client.once("ready", () => {
  console.log(`${client.user.tag} online!`);
});

client.on("messageCreate", (message) => {
  console.log("Message:", message.content);
});

client.on("messageCreate", async (message) => {
  if (message.author.bot) return;

  const args = message.content.split(" ");

  if (args[0] === "!play") {
    const voiceChannel = message.member.voice.channel;

    if (!voiceChannel)
      return message.reply("আগে voice channel এ join করো!");

    const song = args.slice(1).join(" ");

    if (!song)
      return message.reply("গানের নাম দাও!");

    distube.play(voiceChannel, song, {
      textChannel: message.channel,
      member: message.member
    });
  }

  if (args[0] === "!skip") {
    distube.skip(message);
    message.channel.send("⏭️ Skipped");
  }

  if (args[0] === "!stop") {
    distube.stop(message);
    message.channel.send("⏹️ Stopped");
  }
});

client.login(TOKEN);
