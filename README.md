<h1>Build an MCP Server with Python</h1>

<h2>Watch the full tutorial on my YouTube Channel</h2>
<div>

<a>
    <img src="thumbnail_small.png" alt="Thomas Janssen Youtube" width="200"/>
</a>
</div>

<h2>Prerequisites</h2>
<ul>
  <li>Python 3.13</li>
</ul>

<h2>Installation</h2>


<h3>1. Install UV</h3>


On Windows: 
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

On MacOS/Linix: 
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

More info: https://docs.astral.sh/uv/getting-started/installation/

<h3>2. Download Claude Desktop</h3>

Download Claude Desktop here: https://claude.ai/download

<h3>3. Clone the repository:</h3>

```
git clone https://github.com/ThomasJanssen-tech/MCP_Server
cd MCP_Server
```


<h3>4. Add Bright Data API Key</h3>
<ul>
<li>Get your $15 Bright Data credits: https://brdta.com/tomstechacademy</li>
<li>Rename the .env.example file to .env</li>
<li>Add your Bright Data API key</li>
</ul>

<h3>Configure Claude Desktop</h3>

In the project directory, now run the following command to automatically configure Claude Desktop, where main.py is the name of your MCP Server Script.

```
uv run mcp install main.py
```

<h2>Executing the scripts</h2>

- Open a terminal in VS Code

- Execute the following command:

```
uv run download_data.py
uv run ingest_data.py
```

<h2>Start asking questions to Claude Desktop</h2>
You can now ask questions to Claude Desktop about companies listed on Crunchbase!

<h2>Further reading</h2>
<ul>
<li>https://github.com/modelcontextprotocol/python-sdk</li>
</ul>
