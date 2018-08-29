# C# Version of Discord Bot

## Setup Development

```bash
dotnet restore
cp secrets-template.json secrets.json
# Edit the secrets.json file, then
cat ./secrets.json | dotnet user-secrets set
```