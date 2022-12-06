# Apex Legends Data Tool (apex-dt)

[![platform-support](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20osx-blue)](platform) [![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine#alternatives) [![license](https://img.shields.io/github/license/1npo/apex-dt)](LICENSE) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) 

A cross-platform text-based client for the [Apex Legends Status](https://apexlegendsstatus.com) [API](https://apexlegendsapi.com/#introduction) written in Python.

*This is a new work in progress as of 2022-Dec-4 and has been uploaded for tracking purposes. Current version is unreleased. This message will be removed when version 0.0.1 is released.*

## Table of Contents

1. [Background](#background)
2. [Install](#install)
	- [Via PyPI](#via-pypiorg)
	- [Via GitHub](#via-github)
	- [Setting up your credentials](#setting-up-your-credentials)
3. [Usage](#usage)
4. [Information currently available through `apex-dt`](#information-currently-available-through-apex-dt)
5. [Requirements](#requirements)
6. [Limitations](#limitations)
7. [Acknowledgements](#acknowledgements)
8. [Contributing](#contributing)
9. [License](#license)

## Background

I made `apex-dt` to solve two problems:

- I wanted to be able to get useful information quickly while I'm in a game or matchmaking queue, without needing to open my browser, navigate to some website, search for the info, distinguish ads from content, etc.

- I also wanted to capture my match history and save it in a structured database, so that I can do my own analysis with tools of my choice, and not need to rely on third party tools.

## Install

Install `apex-dt` using one of the following methods.

### Via PyPI.org

***TODO. Coming soon!***

```
pip install apex-dt
```

### Via GitHub

```
git clone https://github.com/1npo/apex-dt.git
cd apex-dt
pip install .
```

### Setting up your credentials

***TODO:*** ... 

## Usage

***TODO:*** ...

## Information currently available through `apex-dt`

`apex-dt` makes the following information available:

- All the information made available through my [`apex-wiki-get`](http://github.com/1npo/apex-wiki-get) package.
- Information made available through Hugo's Apex Legends API:
	- General player stats for the players you're tracking
	- Match history for the players you're tracking
	- Current crafting rotation
	- Current map rotation
	- Predator/other leaderboards
	- Server status
	- Apex Legends News

Please see [the TODO file](TODO.md) for features I'm working on, and [the change log](CHANGELOG.md) for the features added in each version.

## Requirements

*This section was last updated on 2022-Dec-4.*

- You must link your Apex Legends account to Apex Legends Status.
	1. Create a [free account](https://apexlegendsstatus.com/register) at the Apex Legends Status website.
	2. Follow the instructions on the ["Link Apex Legends Account"](https://apexlegendsstatus.com/account/claim) page of your account page.
- You must have an API key.
	- You can create one for free at the API [portal](https://portal.apexlegendsapi.com/).
- To use the "Match History" and "Shop History" endpoints:
	- You must be a Tier3 subscriber to [Hugo's Patreon page](https://www.patreon.com/hugodev/posts).
	- You must be whitelisted to use each API.
		1. Once you're a T3 Patreon subscriber, submit a ticket in the `#open-ticket` channel on the [Apex Legends Status Discord Server](https://discord.gg/zsm52M7).
		2. Ask to be whitelisted for each API you plan to use, and give Hugo your API key and Patreon email address.

## Limitations

- The "Match History" endpoint will only return data for the legend you currently have selected.
	- To get data for another legend:
		1. Open Apex Legends
		2. Click "Legends" on the top bar
		3. Pick the legend that you want to get data for
		4. Refresh your match history data in `apex-dt`

## Acknowledgements

A big thanks to [Hugo Derave](https://github.com/HugoDerave) for creating, maintaining, and hosting both [Apex Legends Status](https://apexlegendsstatus.com/) and the unofficial [Apex Legends API](https://apexlegendsapi.com/#introduction). This project wouldn't be possible without his efforts.

## Contributing

PRs are welcome. Please see [the contributing file](CONTRIBUTING.md) before submitting a PR.

## License

[MIT](LICENSE) © 1npo
