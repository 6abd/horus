# Project | Horus



<p align="center">
  <img src="https://i.ibb.co/LSYgyHh/Screenshot-2024-06-30-at-12-51-09-AM.png"/>
</p>
<div align="center">
  
[![6abd - horus](https://img.shields.io/static/v1?label=6abd&message=horus&color=crimson&logo=github)](https://github.com/6abd/horus "Go to GitHub repo")
[![GitHub tag](https://img.shields.io/github/tag/6abd/horus?include_prereleases=&sort=semver&color=crimson)](https://github.com/6abd/horus/releases/)
[![stars - horus](https://img.shields.io/github/stars/6abd/horus?style=social&logoColor=crimson)](https://github.com/6abd/horus)
[![forks - horus](https://img.shields.io/github/forks/6abd/horus?style=social&logoColor=crimson)](https://github.com/6abd/horus)
[![issues - horus](https://img.shields.io/github/issues/6abd/horus?color=crimson)](https://github.com/6abd/horus/issues)
[![License](https://img.shields.io/badge/License-GNU_General_Public_License_v3.0-crimson)](#license)


</div>

# Table of Contents

* [🚀 About Horus](#-about-horus)
* [⚡ Installation and Usage Instructions](#-installation-and-usage-instructions)
* [⚙️ API Configuration](#%EF%B8%8F-api-configuration)
* [🔮 Intended Features](#-intended-features)
* [🤝 Current Maintainers](#-current-maintainers)
* [🛠️ Contributing](#%EF%B8%8F-contributing)
* [📧 Contact Me](#-contact-me)
* [🤝 Acknowledgements](#-acknowledgements)


## 🚀 About Horus

Horus is an all-in-one encompassing tool for investigations assistance, from API leveraging to compiling data too. Its your pre-ops buddy! 

## ⚡ Installation and Usage Instructions
To get started with this project, you will need Python installed on your device.
Once it is installed, follow these steps:

1. Clone this repository.
2. `cd` to the 'horus' directory. (Make sure it isn't the outermost folder)
3. Install dependencies using the following command: ```pip install -r requirements.txt```
4. In the 'horus' directory, run ```python3 horus.py``` on Linux/MacOS, or ```py horus.py``` on Windows

*Note: protonvpn-cli is a requirement for the 'pvpn' command*

## ⚙️ API Configuration
To configure the APIs necessary for usage of certain commands, you can either manually enter them, or use the 'apicon' command

To manually configure API keys, navigate to ```/src/modules/var/pipes/api_config.json```. Enter your API keys in their corresponding entries.

**⚠️ Warning: If you are contributing to this repository or are testing it through a public fork, make sure to remove your API keys from the JSON file before pushing changes.**

  
## 🔮 Intended Features
```  
🟢 = Fully implemented or more than 80% done

🟡 = Partially implemented / In development

🔴 = To be implemented
```

<p align="center">
  <img src="https://i.ibb.co/M75HnnL/Screenshot-2024-06-30-at-12-49-53-AM.png"/>
</p>

*On Shodan: Shodan is a paid API, so in order for your API to work you need to subscribe to them. A lot of its feature's location-related functionality is available in 'geolock', but more detailed features require that API.*
## 🤝 Current Maintainers

- [6abd](https://github.com/6abd) (Me) | Project Lead and Developer


## 🛠️ Contributing
- If you notice a bug or want to request a feature, make an issue with the appropriate tag
- If you would like to fix a bug or add a feature yourself, make a PR and I'll take a look
- If you would like to become a long-term maintainer/contributor, contact me
- For any other inquiries, you may also contact me

## 📧 Contact Me
- Email: digitalizedsnake@gmail.com
- Discord: maestro.hq or through the [community server](https://discord.gg/PhkqXAT7Ax)

## 🤝 Acknowledgements

- [Fox](https://github.com/FoxIDK) | Was Previously Project Manager
- [Tornado](https://github.com/digitalsilicon) | Was Previously QA
- [Mart](https://github.com/marvhus) | Was Previously Sr Dev
- [Mu](https://github.com/IamMU) | Was Previously Jr Dev

*Some code used can be attributed to [Fox](https://github.com/FoxIDK) and [Askerdyne Ltd.](https://askerdyne.com/), specifically the 'Loki' encryption toolset.*

*Some `.github` files were made by [Jesse Squires](https://github.com/jessesquires)*

<a href="https://www.producthunt.com/posts/horus?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-horus" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=453469&theme=light" alt="Horus - An&#0032;OSINT&#0032;&#0047;&#0032;digital&#0032;forensics&#0032;tool&#0032;built&#0032;in&#0032;Python | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
