# ZSH Crypto Prices

Oh My Zsh plugin adding a Powerlevel9k segment to display crypto prices in Zsh

## Requirements

1. Install Zsh
2. Install [Oh My Zsh](https://ohmyz.sh/)
3. Install [Powerlevel9k](https://github.com/bhilburn/powerlevel9k)

## Installation

1. `git clone https://github.com/vincentdnl/zsh-crypto-prices.git`
2. `mv zsh-crypto-prices ${ZSH}/plugins/`
3. Add plugin in `$HOME/.zshrc`
```
plugins=(
  ...
  zsh-crypto-prices
  ...
)

source $ZSH/oh-my-zsh.sh

POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(custom_bitcoin_price)
```
