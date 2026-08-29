# n8n Connections & Token Reference Guide

A comprehensive technical guide for connecting cloud platforms and APIs to n8n workflow automation engines.

## Overview of Authentication Types

| Connection Type | Description | App Required? | Native n8n Node? | Example Platforms |
|---|---|---|---|---|
| **OAuth 2.0** | Token refresh flow via developer client ID & secret | Yes | Yes | Google, LinkedIn, Meta, X, Dropbox |
| **Bearer Token** | Long-lived system user access token | Yes | Yes (HTTP) | WhatsApp Business Cloud, Meta API |
| **API Key** | Static API key passed via headers | No | Some | Notion, ElevenLabs, HeyGen, Claude API |
