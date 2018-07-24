_bitcoin_price(){
    echo -n $(python3 ${ZSH}/plugins/zsh-crypto-prices/crypto_prices.py)
}

POWERLEVEL9K_CUSTOM_BITCOIN_PRICE="_bitcoin_price"
