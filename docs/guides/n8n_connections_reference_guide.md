# n8n Connections & Token Reference Guide

A comprehensive technical guide for connecting cloud platforms and APIs to n8n workflow automation engines.

## Overview of Authentication Types

| Connection Type | Description | App Required? | Native n8n Node? | Example Platforms |
|---|---|---|---|---|
| **OAuth 2.0** | Token refresh flow via developer client ID & secret | Yes | Yes | Google, LinkedIn, Meta, X, Dropbox |
| **Bearer Token** | Long-lived system user access token | Yes | Yes (HTTP) | WhatsApp Business Cloud, Meta API |
| **API Key** | Static API key passed via headers | No | Some | Notion, ElevenLabs, HeyGen, Claude API |

## Platform Connection Details

### 1. Meta / WhatsApp Business Cloud
- **Auth Type:** Bearer Token / OAuth 2.0
- **App Required:** Meta Developer App (`developers.facebook.com`)
- **Key Fields:** Access Token, Phone Number ID, Business Account ID, Webhook Verify Token.

### 2. Google (YouTube & Gmail)
- **Auth Type:** OAuth 2.0
- **App Required:** Google Cloud Console Project (`console.cloud.google.com`)
- **Key Fields:** Client ID, Client Secret, Authorised Redirect URIs.

### 3. LinkedIn
- **Auth Type:** OAuth 2.0
- **App Required:** LinkedIn Developer Portal (`developer.linkedin.com`)
- **Key Fields:** Client ID, Client Secret, Product: "Share on LinkedIn".

### 4. ElevenLabs
- **Auth Type:** API Key
- **Header:** `xi-api-key: YOUR_ELEVENLABS_API_KEY`
- **Endpoint:** `https://api.elevenlabs.io/v1/text-to-speech/{voice_id}`

### 5. HeyGen
- **Auth Type:** API Key
- **Header:** `X-Api-Key: YOUR_HEYGEN_API_KEY`
- **Endpoint:** `https://api.heygen.com/v2/template/{template_id}/generate`
